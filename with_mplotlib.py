import matplotlib.pyplot as plt
import numpy as np
# Sample data
a = 0 ; b = 0
x = 1 ; y = 1

plt.scatter(a, b)
plt.scatter(x, y)

theta = np.pi/4
new_x = (x-a)*np.cos(theta)-(y-b)*np.sin(theta)+a
new_y = (x-a)*np.sin(theta)+(y-b)*np.cos(theta)+b

plt.scatter(new_x, new_y)

plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Plotting Points')

plt.savefig("mygraph.png")