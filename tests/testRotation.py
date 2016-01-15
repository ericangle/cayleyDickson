import os
import sys
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + '/..')
from rotation import rotate as rot
from math import pi,cos,sin
import numpy as np

n1    = [1.0,1.0,1.0]
V1    = [1.0,0.0,0.0]
T1    = 2.0*pi/3.0
V1rot = [0.0,1.0,0.0]

n2    = [0.0,0.0,1.0]
V2    = [0.0,1.0,0.0]
T2    = pi/2.0
V2rot = [-1.0,0.0,0.0]

n3    = [1.0,1.0,0.0]
V3    = [1.0,0.0,0.0]
T3    = pi/2.0
V3rot = [cos(pi/4.0)*cos(pi/4.0),cos(pi/4.0)*sin(pi/4.0),-sin(pi/4.0)]

# Generators of rotations
Jx = np.array([[0,0,0],
               [0,0,-1.0],
               [0,1.0,0]])
Jy = np.array([[0,0,1.0],
               [0,0,0],
               [-1.0,0,0]])
Jz = np.array([[0,-1.0,0],
               [1.0,0,0],
               [0,0,0]])

iden = np.array([[1.0,0,0],
                 [0,1.0,0],
                 [0,0,1.0]])

def test_rotate():
  def useExp(V,T,n):
    return np.dot(np.linalg.matrix_power(iden + T*(n[0]*Jx + n[1]*Jy + n[2]*Jz)/10000,10000),np.array([[V[0]],[V[1]],[V[2]]]))

  def compare(calc,accept1,accept2):
    for i in range(len(calc)):
      assert abs(calc[i] - accept1[i]) < 1.0e-6
      assert abs(calc[i] - accept2[i][0]) < 1.0e-3

  compare(rot(V1,T1,n1),V1rot,useExp(V1,T1,n1))
  compare(rot(V2,T2,n2),V2rot,useExp(V2,T2,n2))
  compare(rot(V3,T3,n3),V3rot,useExp(V3,T3,n3))
