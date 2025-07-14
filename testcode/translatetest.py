import matplotlib.pyplot as plt
import math

plt.close('all')
#Example information
excord = [(0.96,4.78),(5.38,6.1),(6.7,1.68),(2.28,0.36)]
target_point = excord[0]

zeroorigin = (0,0)
x1=0
y1=1

#Functions

def shifting(coords, target):
    shifted_coords = [(x-target[0],y-target[1]) for (x,y) in coords]
    return shifted_coords

def xy_vals(points):
    x_vals =[a[0] for a in points]
    y_vals = [a[1] for a in points]
    return x_vals,y_vals

def calculate_angle(x1, y1, x2, y2): 
    dot_product = x1 * x2 + y1 * y2
    magnitude1 = math.sqrt(x1 ** 2 + y1 ** 2)
    magnitude2 = math.sqrt(x2 ** 2 + y2 ** 2)

    cosine_theta = dot_product / (magnitude1 * magnitude2)

    angle = math.acos(cosine_theta)

    return angle

def rotate(origin, point, angle):

    ox, oy = origin
    px, py = point

    qx = ox + math.cos(angle) * (px - ox) - math.sin(angle) * (py - oy)
    qy = oy + math.sin(angle) * (px - ox) + math.cos(angle) * (py - oy)
    return qx, qy

def rotate_all(coords,rotate,angle,origin):
    rotcoords = []
    for i in coords:
        rotcoords.append(rotate(origin,i,angle))
    return rotcoords






x_vals = [a[0] for a in excord]
y_vals = [a[1] for a in excord]

shiftres = shifting(excord,target_point)


shiftx_vals = [a[0] for a in shiftres]
shifty_vals = [a[1] for a in shiftres]

x2=shiftx_vals[1]
y2=shifty_vals[1]

angle=calculate_angle(x1,y1,x2,y2)




final_points = rotate_all(shiftres,rotate,angle,zeroorigin)

rotx_vals = [a[0] for a in final_points]
roty_vals = [a[1] for a in final_points]

if __name__=='__main__':
    plt.scatter(x_vals,y_vals,color='b',label="original")
    plt.scatter(shiftx_vals,shifty_vals,color='r',label="translated")
    plt.scatter(rotx_vals,roty_vals,color='k',label='aligned')
    plt.legend()
    plt.axis('equal')
    plt.show()
