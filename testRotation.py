import rotation
from math import *
from numpy import *

print("Testing rotation.py")

def testComps(accept,compare):
  numPass = 0
  for i in range(3):
    if abs(accept[i]-compare[i]) < 1.0e-6:
      numPass = numPass + 1
  if numPass == 3:
    return "pass"
  else:
    return "fail"

n = [1.0,1.0,1.0]
V = [1.0,0.0,0.0]
T = 2.0*pi/3.0
#print rotation.rotate(V,T,n)

#dim = 3
#Jx = zeros(shape=(dim,dim))
#Jy = zeros(shape=(dim,dim))
#Jz = zeros(shape=(dim,dim))
#Jx[1][2] = -1.0
#Jx[2][1] = -Jx[1][2]
#Jy[0][2] = -1.0
#Jy[2][0] = -Jy[0][2]
#Jz[0][1] = -1.0
#Jz[1][0] = -Jz[0][1]
#J = [Jx,Jy,Jz]
#total = T*sum(n[i]*J[i] for i in xrange(3))

#R = sum(linalg.matrix_power(total,i)/factorial(i) for i in xrange(100))

#print R.dot(V)

print(testComps(rotation.rotate(V,2.0*pi/3.0,n),[0.0,1.0,0.0]))
