from algebra import Algebra as alg
import numpy as np

R1 = alg(1)
R2 = alg(2)

def test_real_addition():
  assert R1 + R2 == alg(R1.a + R2.a)

def test_real_subtraction():
  assert R1 - R2 == alg(R1.a - R2.a)

def test_real_conjugation():
  assert R1.conj() == R1

def test_real_negation():
  assert R1.neg() == alg(-R1.a)

def test_real_norm():
  assert R1.norm() == abs(R1.a)

def test_real_multiplication():
  assert R1 * R2 == alg(R1.a * R2.a)

def test_real_division():
  assert R1 / R2 == alg(R1.a / R2.a)

C1 = alg(1,2)
C2 = alg(3,4)

def test_complex_addition():
  assert C1 + C2 == alg(C1.a.a + C2.a.a,C1.b.a + C2.b.a)

def test_complex_subtraction():
  assert C1 - C2 == alg(C1.a.a - C2.a.a,C1.b.a - C2.b.a)

def test_complex_conjugation():
  assert C1.conj() == alg(C1.a.a,-C1.b.a)

def test_complex_negation():
  assert C1.neg() == alg(-C1.a.a,-C1.b.a)

def test_complex_norm():
  assert C1.norm() == pow(sum([pow(i,2.0) for i in C1.asList()]),0.5)

def test_complex_multiplication():
  assert C1 * C2 == alg(C1.a.a * C2.a.a - C1.b.a * C2.b.a,
                        C1.a.a * C2.b.a + C1.b.a * C2.a.a)

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
  # basis vectors
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

def test_octonion_multiplication():
  # basis vectors
  E = [alg(1,0,0,0,0,0,0,0),
       alg(0,1,0,0,0,0,0,0),
       alg(0,0,1,0,0,0,0,0),
       alg(0,0,0,1,0,0,0,0),
       alg(0,0,0,0,1,0,0,0),
       alg(0,0,0,0,0,1,0,0),
       alg(0,0,0,0,0,0,1,0),
       alg(0,0,0,0,0,0,0,1)]

  # we are only going to fill in the upper triangular part
  table = np.array([[0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 3,-2, 5,-4,-7, 6],
                    [0, 0, 0, 1, 6, 7,-4,-5],
                    [0, 0, 0, 0, 7,-6, 5,-4],
                    [0, 0, 0, 0, 0, 1, 2, 3],
                    [0, 0, 0, 0, 0, 0,-3, 2],
                    [0, 0, 0, 0, 0, 0, 0,-1],
                    [0, 0, 0, 0, 0, 0, 0, 0]])

  def testCase(i,j):
    if i == 0:
      assert E[i] * E[j] == E[j]
    else:
      if j == 0:
        assert E[i] * E[j] == E[i]
      else:
        if i == j:
          assert E[i] * E[j] == E[0].neg()
        else:
          if j > i:
            element = table[i][j]
          else:
            element = -table[j][i]
          if element > 0:
            assert E[i] * E[j] == E[element]
          else:
            assert E[i] * E[j] == E[abs(element)].neg() 

  for i in range(8):
    for j in range(8):
      testCase(i,j)

#def test_octonion_division():
# Test 6: Division
#nTrueO = nTrueO + (alg.div(O1,O2) == alg.alg(place,holder,for,now))
