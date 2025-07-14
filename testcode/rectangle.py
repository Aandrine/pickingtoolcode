import matplotlib.pyplot as plt
import random

x_start_coordinate = random.uniform(0,10)
y_start_coordinate = random.uniform(0,10)

x_vector = random.uniform(0,5)

y_vector = random.uniform(0,5)

first_vector = [x_vector,y_vector]

normal = [y_vector,x_vector]

coord2 = [x_start_coordinate+x_vector,y_start_coordinate+y_vector]

coord3 = [y_vector-x_start_coordinate,y_vector-y_start_coordinate]

coord4 = [coord3[0]+x_vector,coord3[1]+y_vector]

plt.scatter(x_vector,y_vector)
plt.scatter(coord2[0],coord2[1])
plt.scatter(coord3[0],coord3[1])
plt.scatter(coord4[0],coord4[1])

plt.axis('equal')
plt.show()