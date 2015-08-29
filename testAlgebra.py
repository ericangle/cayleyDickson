from algebra import Algebra as alg

R1 = alg(1)
R2 = alg(2)

def test_real_addition():
  assert R1 + R2 == alg(1+2)

def test_real_subtraction():
  assert R1 - R2 == alg(1-2)

def test_real_conjugation():
  assert R1.conj() == R1

def test_real_negation():
  assert R1.neg() == alg(-1)

def test_real_norm():
  assert R1.norm() == 1

def test_real_multiplication():
  assert R1 * R2 == alg(1*2)

def test_real_division():
  assert R1 / R2 == alg(1/2)

C1 = alg(1,2)
C2 = alg(3,4)

def test_complex_addition():
  assert C1 + C2 == alg(1+3,2+4)

def test_complex_subtraction():
  assert C1 - C2 == alg(1-3,2-4)

def test_complex_conjugation():
  assert C1.conj() == alg(1,-2)

def test_complex_negation():
  assert C1.neg() == alg(-1,-2)

def test_complex_norm():
  assert C1.norm() == pow(sum (pow(i,2.0) for i in range(1,2+1)),0.5)

def test_complex_multiplication():
  assert C1 * C2 == alg(1*3-2*4,1*4+2*3)

def test_complex_division():
  assert C1 / C2 == alg(11.0/25.0,2.0/25.0)

Q1 = alg(1,2,3,4)
Q2 = alg(5,6,7,8)

def test_quaternion_addition():
  assert Q1 + Q2 == alg(1+5,2+6,3+7,4+8)

def test_quaternion_subtraction():
  assert Q1 - Q2 == alg(1-5,2-6,3-7,4-8)

def test_quaternion_conjugation():
  assert Q1.conj() == alg(1,-2,-3,-4)

def test_quaternion_negation():
  assert Q1.neg() == alg(-1,-2,-3,-4)

def test_quaternion_norm():
  assert Q1.norm() == pow(sum (pow(i,2.0) for i in range(1,4+1)),0.5)

def test_quaternion_multiplication():
  E = [alg(1,0,0,0),alg(0,1,0,0),alg(0,0,1,0),alg(0,0,0,1)]
  assert E[0] * E[0] == E[0]
  assert E[0] * E[1] == E[1]
  assert E[0] * E[2] == E[2]
  assert E[0] * E[3] == E[3]
  assert E[1] * E[0] == E[1]
  assert E[1] * E[1] == E[0].neg()
  assert E[1] * E[2] == E[3]
  assert E[1] * E[3] == E[2].neg()
  assert E[2] * E[0] == E[2]
  assert E[2] * E[1] == E[3].neg()
  assert E[2] * E[2] == E[0].neg()
  assert E[2] * E[3] == E[1]
  assert E[3] * E[0] == E[3]
  assert E[3] * E[1] == E[2]
  assert E[3] * E[2] == E[1].neg()
  assert E[3] * E[3] == E[0].neg()

def test_quaternion_division():
  modSqQ2 = pow(5.0,2.0) + pow(6.0,2.0) + pow(7.0,2.0) + pow(8.0,2.0)
  assert Q1 / Q2 == alg((5+12+21+32)/modSqQ2,(-6+10-24+28)/modSqQ2,(-7+16+15-24)/modSqQ2,(-8-14+18+20)/modSqQ2)

O1 = alg(1,2,3,4,5,6,7,8)
O2 = alg(9,10,11,12,13,14,15,16)

def test_octonion_norm():
  assert O1 + O2 == alg(1+9,2+10,3+11,4+12,5+13,6+14,7+15,8+16)

def test_octonion_norm():
  assert O1 - O2 == alg(1-9,2-10,3-11,4-12,5-13,6-14,7-15,8-16)

def test_octonion_norm():
  assert O1.conj() == alg(1,-2,-3,-4,-5,-6,-7,-8)

def test_octonion_norm():
  assert O1.norm() == pow(sum (pow(i,2.0) for i in range(1,8+1)),0.5)

#def test_octonion_multiplication():
# add 8x8 mult table

#def test_octonion_division():
# Test 6: Division
#nTrueO = nTrueO + (alg.div(O1,O2) == alg.alg(place,holder,for,now))
