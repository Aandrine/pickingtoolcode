# Andrine Haugdal

import numpy as np
np.set_printoptions(legacy='1.25')

# Thic code calculates the centers of rectangle chips in some grid based on the coordinates of four chipcorners

def find_direction_vectors(point_1: list,point_2: list):

    """
    Takes two points (x,y) and returns the normalized direction vector from point 1 to point 2
    """

    vector = list(map(lambda x, y: x - y, point_1, point_2))

    norm = vector/np.linalg.norm(vector)

    return norm


def find_first_centers(corners: list,chipwidth: float, chipheight: float)-> list:

    """
    Takes four points  (corner of the chips) and the size of a chip
    and calculates the positions of the centers of the chips 
    """

    norm_1 = -find_direction_vectors(corners[0],corners[2])
    norm_2 = find_direction_vectors(corners[1],corners[3])

    center_list = [(i+(norm_1*chipwidth/2+norm_2*chipheight/2)) for i in corners]

    return center_list


def find_step_vector(points,chipnum: int):

    """
    Takes two points and a number of steps and calculates the size and direction of the step
    """
    ##should i merge this with find direction vector??

    xdiff = points[1]-points[0]
    #divide by zero
    
    step_vector = xdiff/chipnum

    return step_vector


def make_grid(init_centers: list,chipcolumns: int,chiprows: int,removed: list) -> list:

    """
    Takes four initial points and creates the coordinates for the rest of the centers
    """

    step_1 = find_step_vector([init_centers[0],init_centers[2]],chipcolumns-1)
    step_2 = -find_step_vector([init_centers[1],init_centers[3]],chiprows-1)

    #must take odd numbers into account
    if chiprows % 2:
        range_y = range(int(chiprows/2))
    else:
        range_y = range(-int(chiprows/2)+1,int(chiprows/2)+1)

    all_centers = []

    for j in range (chipcolumns):
        for i in range_y:
            
            all_centers.append(np.add(init_centers[0],j*step_1+i*step_2))

    for i in sorted(removed, reverse=True):
        del all_centers[i] #must check that the grid is chipx * chiprows

    return all_centers

##taken from google
def angle(vec1, vec2):
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

def find_W_angle(corners):

    vector = find_direction_vectors(corners[1],corners[3])
    
    wangle = angle(vector,(0,1))
    return wangle

####################################################################

def whole_process(point1,point2,point3,point4, height: float,width: float,chipcolumns: int,chiprows: int,removed: list):
    """
    Does the whole process from start to finish.

    Args:
        height (float) : Height of the chip.
        width (float) : Width of the chip.
        chipcolumns (int) : number of chips in x direction
        chiprows (int) : Number of chips in y direction
        removed (list) : The potential chip in the rectangle grid that are removed

    Returns:
        all_center: the coordinates for the center of all the chips.
    """

    corners =[point1,point2,point3,point4]

    init_centers = find_first_centers(corners,height,width)

    all_centers = make_grid(init_centers,chipcolumns,chiprows,removed)


    return all_centers



###############################################################################################

ex_point1 = [143.682,322.178]
ex_point2 = [207.436,403.629]
ex_point3 = [303.693,322.630]
ex_point4 = [207.069,261.128]


ex_corners =[ex_point1,ex_point2,ex_point3,ex_point4]

not_included = [0,1,2,5,6,7,8,15,40,41,46,47]

ex_chipwidth = 19.2
ex_chipheight = 19.4

ex_chiprows = 6
ex_chipcolumns = 8

###############################################################################################
if __name__ == "__main__":
    test = whole_process(ex_point1,ex_point2,ex_point3,ex_point4,ex_chipwidth,ex_chipheight,ex_chiprows,ex_chipcolumns,not_included)

    def print_coords(coords):
        num = 1
        for i in coords:
            print(f"CHIP {num} : {(round(coords[num-1][0],2),round(coords[num-1][1],2))}")
            num = num + 1

    #print_coords(test)
    def prepare(centers):
        testcoords = []
        for i in centers:
            x = list(i)
            x.append(find_W_angle(ex_corners))
            testcoords.append(tuple(x))
        return testcoords


    Andrine_vision_data = prepare(test)

    print(Andrine_vision_data)