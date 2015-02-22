import algebra
from math import *

def rotate(vec,T,n):
  cosHT = cos(0.5*T)
  sinHT = sin(0.5*T)
  nMag = sqrt(pow(n[0],2.0) + pow(n[1],2.0) + pow(n[2],2.0))
  for i in xrange(3):
    n[i] = n[i]/nMag
  Qvec = algebra.alg([0.0,vec[0],vec[1],vec[2]])
  R = algebra.alg([cosHT, sinHT*n[0], sinHT*n[1], sinHT*n[2]])
  Q = algebra.mult(R,algebra.mult(Qvec,algebra.conj(R)))
  return [Q[0][1],Q[1][0],Q[1][1]]
