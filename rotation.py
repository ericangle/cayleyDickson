from algebra import Algebra
from math import *

# vec  3d vector to rotate
# T    angle to rotate vector by
# n    axis to rotate vector about
def rotate(vec,T,n):
  # Normalize n
  nMag = sqrt(pow(n[0],2.0) + pow(n[1],2.0) + pow(n[2],2.0))
  for i in range(3):
    n[i] = n[i]/nMag

  # Embed vec in a quaternion Q
  Qvec = Algebra([0.0,vec[0],vec[1],vec[2]])

  # Construct rotation quaternion R
  cosHT = cos(0.5*T)
  sinHT = sin(0.5*T)
  R = Algebra([cosHT, sinHT*n[0], sinHT*n[1], sinHT*n[2]])

  # Rotate Qvec
  Q = R * ( Qvec * R.conj() )

  # Last 3 elements of Q are vec rotated
  return Q.asList()[1:]
