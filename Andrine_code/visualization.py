import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from Calculation import  *
from matplotlib.patches import Affine2D
import mpl_toolkits.axisartist.floating_axes as floating_axes



def xy_vals(points: list) -> list:
    """
    unzips (or zips idk) the coordinates

    Args:
        points : A list of (x,y) coordinates

    Returns:
        x_vals : a list of the x-coordinates
        y_vals : a list of the y-coordinates
    """
    x_vals =[a[0] for a in points]
    y_vals = [a[1] for a in points]

    return x_vals,y_vals



ex_point1 = [143.682,322.178]
ex_point2 = [207.436,403.629]
ex_point3 = [303.693,322.630]
ex_point4 = [207.069,261.128]


ex_corners =[ex_point1,ex_point2,ex_point3,ex_point4]

not_included = [0,2,4,6,8,10,12,14,16,18,20]

ex_chipwidth = 10 #2.1 
ex_chipheight = 9

ex_chiprows = 10
ex_chipcolumns =8
corners =[ex_point1,ex_point2,ex_point3,ex_point4]

centers1 =find_first_centers(corners,ex_chipwidth,ex_chipheight)
now_all = whole_process(ex_point1,ex_point2,ex_point3,ex_point4,ex_chipwidth,ex_chipheight,ex_chiprows,ex_chipcolumns,not_included)


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

    ax2.scatter(xy_vals(corners)[0],xy_vals(corners)[1],label = "chip corners",color="k",marker='+')
    ax2.scatter(xy_vals(now_all)[0],xy_vals(now_all)[1],label="calculated centers",s=10,color="r")

    height = ex_chipwidth
    width = ex_chipheight

    deg = angle_between_vectors(find_direction_vectors(corners[1],corners[3]),(1,0))

    
    for point in now_all:
        rec = Rectangle((point[0]-width/2,point[1]-height/2), width=width, height=height, alpha=1,fill=False)
        transform = Affine2D().rotate_deg_around(point[0], point[1], deg)
        rec.set_transform(transform + plt.gca().transData) # Apply the transformation
        ax2.add_patch(rec)

    ax1.axis('scaled')
    ax2.axis('scaled')
    ax1.set_title("Initial coordinates for corners")
    ax2.set_title("Inferred centers of all chips")
    ax1.legend()
    ax2.legend()
    plt.figtext(0.5, 0.95, f"Centers found \n for chip height {height} and chip width {width}", ha="center", fontsize=16) 
    plot_extents = 0, 10, 0, 10
    transform = Affine2D().rotate_deg(45)
    helper = floating_axes.GridHelperCurveLinear(transform, plot_extents)
    ax = floating_axes.FloatingSubplot(fig, 111, grid_helper=helper)

    plt.show()
    

if __name__ == "__main__":
    plotting()
