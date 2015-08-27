from algebra import Algebra

print(" ")
print("Testing Algebra.py")

numPass = 0
numTests = 0

########
# Real #
########

nTrueR = 0
nTestsR = 6

R1 = Algebra(1)
R2 = Algebra(2)

# Test 1: Addition
nTrueR = nTrueR + 1*(R1 + R2 == Algebra(1+2))

# Test 2: Subtraction
nTrueR = nTrueR + 1*(R1 - R2 == Algebra(1-2))

# Test 3: Conjugate
nTrueR = nTrueR + 1*(R1.conj() == R1)

# Test 4: Modulus
nTrueR = nTrueR + 1*(R1.norm() == 1)

# Test 5: Multiplication
nTrueR = nTrueR + 1*(R1 * R2 == Algebra(1*2))

# Test 6: Division
nTrueR = nTrueR + 1*(R1 / R2 == Algebra(1/2))

# Results
if (nTrueR == nTestsR):
  print("Real tests pass: ",str(nTrueR)," passed out of ",str(nTestsR))
else:
  print("Real tests fail: ",str(nTrueR)," passed out of ",str(nTestsR))

numPass = numPass + nTrueR
numTests = numTests + nTestsR

###########
# Complex #
###########

nTrueC = 0
nTestsC = 6

C1 = Algebra(1,2)
C2 = Algebra(3,4)

# Test 1: Addition
nTrueC = nTrueC + 1*(C1 + C2 == Algebra(1+3,2+4))

# Test 2: Subtraction
nTrueC = nTrueC + 1*(C1 - C2 == Algebra(1-3,2-4))

# Test 3: Conjugate
nTrueC = nTrueC + 1*(C1.conj() == Algebra(1,-2))

# Test 4: Modulus
nTrueC = nTrueC + 1*(C1.norm() == pow(sum (pow(i,2.0) for i in range(1,2+1)),0.5))

# Test 5: Multiplication
nTrueC = nTrueC + 1*(C1 * C2 == Algebra(1*3-2*4,1*4+2*3))

# Test 6: Division
nTrueC = nTrueC + 1*(C1 / C2 == Algebra(11.0/25.0,2.0/25.0))

# Results
if (nTrueC == nTestsC):
  print("Complex tests pass: ",str(nTrueC)," passed out of ",str(nTestsC))
else:
  print("Complex tests fail: ",str(nTrueC)," passed out of ",str(nTestsC))
  
numPass = numPass + nTrueC
numTests = numTests + nTestsC

##############
# Quaternion #
##############

nTrueQ = 0
nTestsQ = 5 + 4*4

Q1 = Algebra(1,2,3,4)
Q2 = Algebra(5,6,7,8)

# Test 1: Addition
nTrueQ = nTrueQ + (Q1 + Q2 == Algebra(1+5,2+6,3+7,4+8))

# Test 2: Subtraction
nTrueQ = nTrueQ + (Q1 - Q2 == Algebra(1-5,2-6,3-7,4-8))

# Test 3: Conjugate
nTrueQ = nTrueQ + (Q1.conj() == Algebra(1,-2,-3,-4))

# Test 4: Modulus
nTrueQ = nTrueQ + (Q1.norm() == pow(sum (pow(i,2.0) for i in range(1,4+1)),0.5))

# Test 5: Multiplication
E0  = Algebra(1,0,0,0)
nE0 = Algebra(-1,0,0,0)
E1  = Algebra(0,1,0,0)
nE1 = Algebra(0,-1,0,0)
E2  = Algebra(0,0,1,0)
nE2 = Algebra(0,0,-1,0)
E3  = Algebra(0,0,0,1)
nE3 = Algebra(0,0,0,-1)

for i in range(4):
  for j in range(4):
    q1 = Algebra((i==0)*1,(i==1)*1,(i==2)*1,(i==3)*1)    
    q2 = Algebra((j==0)*1,(j==1)*1,(j==2)*1,(j==3)*1)
    q3 = q1 * q2

    # 3 Tests: i,j = 1,2,3
    if (i == j and i != 0):
      nTrueQ = nTrueQ + (q3 == nE0)
    # 4 Tests: i = 0, j = 0,1,2,3
    if (i == 0):
      nTrueQ = nTrueQ + (q3 == Algebra((j==0)*1,(j==1)*1,(j==2)*1,(j==3)*1))
    # 3 Tests: j = 0, i = 1,2,3
    elif (j == 0):
      nTrueQ = nTrueQ + (q3 == Algebra((i==0)*1,(i==1)*1,(i==2)*1,(i==3)*1))
    # 6 Tests: off diag with i and j not 0
    nTrueQ = nTrueQ + (i == 2 and j == 1)*(q3 == nE3)
    nTrueQ = nTrueQ + (i == 3 and j == 1)*(q3 == E2)
    nTrueQ = nTrueQ + (i == 3 and j == 2)*(q3 == nE1)
    nTrueQ = nTrueQ + (i == 1 and j == 2)*(q3 == E3)
    nTrueQ = nTrueQ + (i == 1 and j == 3)*(q3 == nE2)
    nTrueQ = nTrueQ + (i == 2 and j == 3)*(q3 == E1)

# Test 6: Division
modSqQ2 = pow(5.0,2.0) + pow(6.0,2.0) + pow(7.0,2.0) + pow(8.0,2.0)
nTrueQ = nTrueQ + (Q1 / Q2 == Algebra([(5+12+21+32)/modSqQ2,(-6+10-24+28)/modSqQ2,(-7+16+15-24)/modSqQ2,(-8-14+18+20)/modSqQ2]))

# Results
if (nTrueQ == nTestsQ):
  print("Quaternion tests pass: ",str(nTrueQ)," passed out of ",str(nTestsQ))
else:
  print("Quaternion tests fail: ",str(nTrueQ)," passed out of ",str(nTestsQ))

numPass = numPass + nTrueQ
numTests = numTests + nTestsQ

############
# Octonion #
############

nTrueO = 0
nTestsO = 4

O1 = Algebra(1,2,3,4,5,6,7,8)
O2 = Algebra(9,10,11,12,13,14,15,16)

# Test 1: Addition
nTrueO = nTrueO + (O1 + O2 == Algebra(1+9,2+10,3+11,4+12,5+13,6+14,7+15,8+16))

# Test 2: Subtraction
nTrueO = nTrueO + (O1 - O2 == Algebra(1-9,2-10,3-11,4-12,5-13,6-14,7-15,8-16))

# Test 3: Conjugate
nTrueO = nTrueO + (O1.conj() == Algebra(1,-2,-3,-4,-5,-6,-7,-8))

# Test 4: Modulus
nTrueO = nTrueO + (O1.norm() == pow(sum (pow(i,2.0) for i in range(1,8+1)),0.5) )

# Test 5: Multiplication
# add 8x8 mult table

# Test 6: Division
#nTrueO = nTrueO + (Algebra.div(O1,O2) == Algebra.alg(place,holder,for,now))

# Results
if (nTrueO == nTestsO):
  print("Octonion tests pass: ",str(nTrueO)," passed out of ",str(nTestsO))
else:
  print("Octonion tests fail: ",str(nTrueO)," passed out of ",str(nTestsO))

numPass = numPass + nTrueO
numTests = numTests + nTestsO

if (numPass == numTests):
  print("All tests passed.")
else:
  print(str(numPass)," tests passed out of ",str(numTests))

print(" ")
