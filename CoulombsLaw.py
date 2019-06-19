# # Coulomb's Law
# It's an experimental law of physics that quantifies the amount of force between two stationary, electrically charged particles.  
# 
# The formula is `F=k(q1*q2)/r^2`
# k is Coulomb's constant
# q1 and q2 are charges of the particles (we'll use 5 nC for this example)
# r is distance between particles in meters

import matplotlib.pyplot as plt
import numpy as np

def calc_coulomb(q1,q2,r):
    # Define Coulomb's Constant
    k = 8987551787.3681764
    return (k*q1*q2)/pow(r, 2)

# Now, as we have our function, let's calculate force for a given distance. 
# Starting with 0.001 meters up to 0.005 meters with a step of 0.0001 meters.

forces = []
distances = []
for i in range(10, 50):
    r = i/10000
    forces.append(calc_coulomb(0.0000000005, 0.0000000005, r))
    distances.append(r)

plt.xlabel('Distance [m]')
plt.ylabel('Force [N]')
plt.title("Change of force in relation to distance in Coulomb's Law")
plt.plot(distances, forces)
plt.show()
