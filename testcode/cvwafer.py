import numpy as np
import cv2
import matplotlib.pyplot as plt

image = cv2.imread('wafer.jpg')

image_gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

image_blurred = cv2.medianBlur(image_gray,3)

# image_thresh = cv2.threshold(image_blurred,200,255,cv2.THRESH_BINARY)[1]
image_thresh = cv2.adaptiveThreshold(image_blurred,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
            cv2.THRESH_BINARY,15,2)

contours, _ = cv2.findContours(image_thresh.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

edges = cv2.Canny(image_thresh,50,150,apertureSize=3)

lines = cv2.HoughLinesP(edges,1,np.pi/180,200)

image2 = image.copy()

lines_list =[]
lines = cv2.HoughLinesP(
            edges, # Input edge image
            0.1, # Distance resolution in pixels
            np.pi/180, # Angle resolution in radians
            threshold=100, # Min number of votes for valid line
            minLineLength=5, # Min allowed length of line
            maxLineGap=10 # Max allowed gap between line for joining them
            )

# Iterate over points
for points in lines:
      # Extracted points nested in the list
    x1,y1,x2,y2=points[0]
    # Draw the lines joing the points
    # On the original image
    cv2.line(image2,(x1,y1),(x2,y2),(0,255,0),2)
    # Maintain a simples lookup list for points
    lines_list.append([(x1,y1),(x2,y2)])


# Loop over the contours
for contour in contours:
    # Approximate the contour
    peri = cv2.arcLength(contour, True)
    approx = cv2.approxPolyDP(contour, 0.08 * peri, True)

    # If the approximated contour has 4 vertices
    if len(approx) == 4:
        # Get bounding box and aspect ratio
        x, y, w, h = cv2.boundingRect(approx)
        aspect_ratio = float(w) / h

        # Draw the rectangle
        cv2.drawContours(image, [approx], -1, (0,255,0),2)

plt.figure(figsize=(20,8))

plt.subplot(1,3,1)
plt.imshow(image_thresh)
plt.title('Threshed image')
plt.axis('off')

plt.subplot(1,3,2)
plt.imshow(image)
plt.title('Detected rectangles')
plt.axis('off')


plt.subplot(1,3,3)
plt.imshow(image2)
plt.title('Detected lines')
plt.axis('off')

plt.show()