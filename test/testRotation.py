from rotation import rotate as rot
from math import pi,cos,sin

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

def test_rotate():
  def compare(calc,accept):
    for i in range(len(calc)):
      assert abs(calc[i] - accept[i]) < 1.0e-6

  compare(rot(V1,T1,n1),V1rot)
  compare(rot(V2,T2,n2),V2rot)
  compare(rot(V3,T3,n3),V3rot)
