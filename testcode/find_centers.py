import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle
from matplotlib.patches import Affine2D

def find_direction_vectors(point_1,point_2):
    """
    Takes two points (x,y) and returns the normalized direction vector from point 1 to point 2
    """
    vector = np.subtract(point_1,point_2)

    norm = vector/np.linalg.norm(vector)

    print("find direction")
    return norm

def find_first_centers(points,chip_length_x: float, chip_length_y: float):

    """
    Takes four points  (corner of the chips) and the size of a chip
    and calculates the positions of the centers of the chips 
    """

    norm1 = -find_direction_vectors(points[0],points[2])
    norm2 = find_direction_vectors(points[1],points[3])

    center_list = []

    for i in points:
        newx = np.add(i,norm1*chip_length_x/2)

        center = np.add(newx,norm2*chip_length_y/2)

        center_list.append(center)

    x_val, y_val = zip(*center_list)

    print("find center")

    return x_val, y_val


def find_stepsize(points,chipnum: int):
    """
    Takes two points and a number of steps and calculates the size of the step
    """
    xdiff = np.subtract(np.array(points[1]),np.array(points[0]))

    delta =np.divide(xdiff,chipnum)

    print("find step")

    return delta

def make_grid(init_centers,chipsx: int,chipsy: int,removed: list):

    """
    Takes four initial points and creates the coordinates for the rest of the centers
    """

    coords = list(zip(init_centers[0],init_centers[1]))

    step1 = find_stepsize([coords[0],coords[2]],chipsx-1)
    step2 = -find_stepsize([coords[1],coords[3]],chipsy-1)


    new_points = []
    for j in range (chipsx):
        for i in range(int(-chipsy/2)+1,int(chipsy/2)+1):
        
            new_points.append(np.add(coords[0],j*step1+i*step2))

    for i in sorted(removed, reverse=True):
        del new_points[i]

    new_points_list = list(zip(*(new_points)))

    print("find grid")

    return new_points_list

####################################################################

def whole_process(points, height,width,chipsx,chipsy,removed):
    x_vals, y_vals = points.T

    init_centers = find_first_centers(points,height,width)

    test_coords = list(zip(test_centers[0],test_centers[1]))

    all_centers = make_grid(init_centers,chipsx,chipsy,removed)

    final_coords = list(zip(all_centers[0],all_centers[1]))

    return final_coords





###############################################################################################
#Initial points starting at the upper right corner of chip nr 1
# ex_point1 = [3.57,10.64]
# ex_point2 = [11.42,16.72]
# ex_point3 = [18.42,6.55]
# ex_point4 = [7.89,3.17]

ex_point1 = [143.682,322.178]
ex_point2 = [207.436,403.629]
ex_point3 = [303.693,322.630]
ex_point4 = [207.069,261.128]

not_included = [0,1,2,5,6,7,8,15,40,41,46,47]

ex_chiplength_x = 19.2
ex_chiplegth_y = 19.4

ex_chipsx = 6
ex_chipsy = 8

#################################
point_array =np.array([ex_point1,ex_point2,ex_point3,ex_point4])
x_vals, y_vals = point_array.T


test_centers = find_first_centers(point_array,ex_chiplength_x,ex_chiplegth_y)

test_coords = list(zip(test_centers[0],test_centers[1]))

expoint = make_grid(test_centers,ex_chipsx,ex_chipsy,not_included)

final_coords = list(zip(expoint[0],expoint[1]))

def testkode():
    print("dette er bare tull hihi")

testkode()


def print_coords(coords):
    num = 1
    for i in coords:
        print(f"Chip nr {num} has its center at {(round(final_coords[num-1][0],2),round(final_coords[num-1][1],2))}")
        num = num + 1

# print_coords(final_coords)


##TAKEN FROM GOOGLES AI AND IS JUST USED FOR MY VISUALIZATION##
def angle_between_vectors(vec1, vec2):
    """
    Calculates the angle between two vectors in degrees.

    Args:
        vec1 (numpy.ndarray): The first vector.
        vec2 (numpy.ndarray): The second vector.

    Returns:
        float: The angle between the vectors in degrees.
    """
    dot_product = np.dot(vec1, vec2)
    magnitude_vec1 = np.linalg.norm(vec1)
    magnitude_vec2 = np.linalg.norm(vec2)

    # Handle potential division by zero if a vector has zero magnitude
    if magnitude_vec1 == 0 or magnitude_vec2 == 0:
        return 0.0  # Or raise an error, depending on desired behavior

    cosine_angle = dot_product / (magnitude_vec1 * magnitude_vec2)

    # Clip the value to prevent numerical errors with arccos (e.g., values slightly outside [-1, 1])
    cosine_angle = np.clip(cosine_angle, -1.0, 1.0)

    angle_radians = np.arccos(cosine_angle)
    angle_degrees = np.degrees(angle_radians)
    return angle_degrees




def plotting():
    """
    Plots the gives centers and the inferred centers in separate plots, used 
    """
    fig,(ax1,ax2) = plt.subplots(1,2,figsize=(12,8),num="Finding centers")

    ax2.scatter(x_vals,y_vals,label = "chip corners",color="k",marker='+')
    ax2.scatter(expoint[0],expoint[1],label="calculated centers",s=10,color="r")

    height = ex_chiplength_x
    width = ex_chiplegth_y

    deg = angle_between_vectors(find_direction_vectors(point_array[1],point_array[3]),(1,0))

    
    for point in final_coords:
        rec = Rectangle((point[0]-width/2,point[1]-height/2), width=width, height=height, alpha=1,fill=False)
        transform = Affine2D().rotate_deg_around(point[0], point[1], deg)
        rec.set_transform(transform + plt.gca().transData) # Apply the transformation
        ax2.add_patch(rec)

    for i_x, i_y in zip(x_vals, y_vals):
        ax1.text(i_x, i_y, '({}, {})'.format(i_x, i_y),fontsize = 10,wrap=True)

    ax1.axis('scaled')
    ax2.axis('scaled')
    ax1.set_title("Initial coordinates for corners")
    ax2.set_title("Inferred centers of all chips")
   # ax1.legend()
    ax2.legend()
    plt.figtext(0.5, 0.95, f"Centers found \n for chip height {height} and chip width {width}", ha="center", fontsize=16) 
   # plt.tight_layout()
    plt.show()

if __name__== "__main__":
    plotting()