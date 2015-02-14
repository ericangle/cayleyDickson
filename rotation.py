import algebra
from math import *

# Rotation angle
theta = pi/2.0

# Direction to rotate about
n = [0.0,0.0,1.0]

# Rotation
R = algebra.alg([cos(theta/2), sin(theta/2.0)*n[0], sin(theta/2.0)*n[1], sin(theta/2.0)*n[2]])

# Initial vector
V = algebra.alg([0.0,1.0,0.0,0.0])
print V

# Rotated vector
V_rotated = algebra.mult(R,algebra.mult(V,algebra.conj(R)))
print V_rotated
