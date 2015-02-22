import rotation
from math import *

def testComps(accept,compare):
  numPass = 0
  for i in xrange(3):
    if abs(accept[i]-compare[i]) < 1.0e-6:
      numPass = numPass + 1
  if numPass == 3:
    return "pass"
  else:
    return "fail"

n = [1.0,1.0,1.0]
V = [1.0,0.0,0.0]

print testComps(rotation.rotate(V,2.0*pi/3.0,n),[0.0,1.0,0.0])
