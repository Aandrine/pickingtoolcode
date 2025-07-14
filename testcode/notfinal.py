import numpy as np

def find_direction_vectors(point_1,point_2):
    """
    Takes two points (x,y) and returns the normalized direction vector from point 1 to point 2
    """
    vector = np.subtract(point_1,point_2)

    norm = vector/np.linalg.norm(vector)


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



    return x_val, y_val


def find_stepsize(points,chipnum: int):
    """
    Takes two points and a number of steps and calculates the size of the step
    """
    xdiff = np.subtract(np.array(points[1]),np.array(points[0]))

    delta =np.divide(xdiff,chipnum)



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


    return new_points_list

####################################################################

def whole_process(point1,point2,point3,point4, height: float,width: float,chipsx: int,chipsy: int,removed: list):

    points =np.array([point1,point2,point3,point4])

    init_centers = find_first_centers(points,height,width)

    all_centers = make_grid(init_centers,chipsx,chipsy,removed)

    final_coords = list(zip(all_centers[0],all_centers[1]))

    return final_coords



###############################################################################################

ex_point1 = [143.682,322.178]
ex_point2 = [207.436,403.629]
ex_point3 = [303.693,322.630]
ex_point4 = [207.069,261.128]

not_included = [0,1,2,5,6,7,8,15,40,41,46,47]

ex_chiplength_x = 19.2
ex_chiplegth_y = 19.4

ex_chipsx = 6
ex_chipsy = 8

###############################################################################################

test = whole_process(ex_point1,ex_point2,ex_point3,ex_point4,ex_chiplength_x,ex_chiplegth_y,ex_chipsx,ex_chipsy,not_included)

def print_coords(coords):
    num = 1
    for i in coords:
        print(f"RIKTIG CHIP {num} : {(round(coords[num-1][0],2),round(coords[num-1][1],2))}")
        num = num + 1

print_coords(test)