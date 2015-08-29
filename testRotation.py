from rotation import rotate as rot
from math import pi

n = [1.0,1.0,1.0]
V = [1.0,0.0,0.0]
T = 2.0*pi/3.0

def test_rotate():
  Vrotated_calc   = rot(V,2.0*pi/3.0,n)
  Vrotated_accept = [0.0,1.0,0.0]
  for i in range(len(Vrotated_calc)):
    assert abs(Vrotated_calc[i] - Vrotated_accept[i]) < 1.0e-6
