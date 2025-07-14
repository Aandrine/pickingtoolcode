import cv2
import numpy as np
import tkinter as tk
from tkinter import messagebox
from globals import camera_index

# List to store selected corners (marked by the crosshair)
selected_corners = []


def darken_image(frame, factor=0.7):
    """Reduce the brightness of the image by a given factor."""
    return cv2.convertScaleAbs(frame, alpha=factor, beta=0)


def draw_crosshair(frame, center_x, center_y):
    """Draw a crosshair at given coordinates."""
    color = (0, 255, 0)  # Green
    thickness = 1
    length = 20  # Length of the crosshair lines

    # Horizontal line
    cv2.line(frame, (center_x - length, center_y), (center_x + length, center_y), color, thickness)
    # Vertical line
    cv2.line(frame, (center_x, center_y - length), (center_x, center_y + length), color, thickness)


def mouse_callback(event, x, y, flags, param):
    """Handle mouse click events to mark corners."""
    if event == cv2.EVENT_LBUTTONDOWN:
        if len(selected_corners) < 2:  # Only allow two corner selections
            selected_corners.append((x, y))
            print(f"Selected corner: ({x}, {y})")
        if len(selected_corners) == 2:  # If two corners are selected, calculate the center
            center_x, center_y = calculate_center(selected_corners[0], selected_corners[1])
            print(f"Center: ({center_x}, {center_y})")


def calculate_center(corner1, corner2):
    """Calculate the center between two corners."""
    center_x = (corner1[0] + corner2[0]) // 2
    center_y = (corner1[1] + corner2[1]) // 2
    return center_x, center_y


def find_marked_corners(frame):
    """Find and highlight the marked corners (based on the crosshairs)."""
    marked_corners = []

    # Only consider the marked corners (those from selected_corners)
    for corner in selected_corners:
        marked_corners.append(corner)
        cv2.circle(frame, corner, 5, (0, 0, 255), -1)  # Draw red circles at marked corners

    return marked_corners


def camera_video():
    global selected_corners  # Make sure to update the global variable

    cap = cv2.VideoCapture(camera_index)

    if not cap.isOpened():
        messagebox.showerror("Error", "Error opening video capture device.")
        return

    cv2.namedWindow("ELP Camera Feed", cv2.WINDOW_NORMAL)
    cv2.setMouseCallback("ELP Camera Feed", mouse_callback)

    while True:
        ret, frame = cap.read()
        if not ret:
            messagebox.showerror("Error", "Can't receive frame (stream end?). Exiting...")
            break

        # Find and draw only the marked corners
        marked_corners = find_marked_corners(frame)

        # Draw crosshairs at selected corners
        for corner in selected_corners:
            draw_crosshair(frame, corner[0], corner[1])

        # If two corners are selected, draw the center
        if len(selected_corners) == 2:
            center_x, center_y = calculate_center(selected_corners[0], selected_corners[1])
            draw_crosshair(frame, center_x, center_y)

        # Check for spacebar press to reset the corners
        key = cv2.waitKey(1)
        if key == 27:  # ESC key to exit
            break
        elif key == 32:  # Spacebar to reset the corners
            selected_corners = []  # Reset the list of selected corners
            print("Corners reset.")

        # Display the frame
        cv2.imshow("ELP Camera Feed", frame)

    cap.release()
    cv2.destroyAllWindows()


def start_camera():
    camera_video()


root = tk.Tk()
root.title("Camera App")

start_button = tk.Button(root, text="Start Camera", command=start_camera)
start_button.pack(pady=20)

root.mainloop()
