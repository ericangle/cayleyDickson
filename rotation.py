import algebra
from math import *

def rotate(vec,theta,n):
  nMag = sqrt(pow(n[0],2.0) + pow(n[1],2.0) + pow(n[2],2.0))
  for i in xrange(3):
    n[i] = n[i]/nMag
  Qvec = algebra.alg([0.0,vec[0],vec[1],vec[2]])
  R = algebra.alg([cos(theta/2.0), sin(theta/2.0)*n[0], sin(theta/2.0)*n[1], sin(theta/2.0)*n[2]])
  Q = algebra.mult(R,algebra.mult(Qvec,algebra.conj(R)))
  return [Q[0][1],Q[1][0],Q[1][1]]

n = [0.0,0.0,1.0]
V = [1.0,0.0,0.0]
V_rotated = rotate(V,pi/2.0,n)

print V_rotated
