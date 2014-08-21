import algebra

###########
# Complex #
###########

numTrueComp = 0
numTestsComp = 4

A1 = algebra.complex(1,2)
A2 = algebra.complex(3,4)

# Test 1: Addition
A1aA2 = algebra.complex(4,6)
if (algebra.add(A1,A2) == A1aA2): numTrueComp = numTrueComp + 1

# Test 2: Subtraction
A1sA2 = algebra.complex(-2,-2)
if (algebra.sub(A1,A2) == A1sA2): numTrueComp = numTrueComp + 1

# Test 3: Conjugate
A1conj = algebra.complex(1,-2)
if (algebra.conj(A1) == A1conj): numTrueComp = numTrueComp + 1

# Test 4: Multiplication
A1mA2 = algebra.complex(-5,10)
if (algebra.mult(A1,A2) == A1mA2): numTrueComp = numTrueComp + 1

# Results
if (numTrueComp == numTestsComp):
  print "Complex tests pass"
else:
  print "Complex tests fail: " + str(numTrueComp) + " passed out of " + str(numTestsComp)
  
##############
# Quaternion #
##############

numTrueQuat = 0
numTestsQuat = 3 + 16

Q1 = algebra.quat(1,2,3,4)
Q2 = algebra.quat(5,6,7,8)

# Test 1: Addition
Q1aQ2 = algebra.quat(6,8,10,12)
if (algebra.add(Q1,Q2) == Q1aQ2): numTrueQuat = numTrueQuat + 1

# Test 2: Subtraction
Q1sQ2 = algebra.quat(-4,-4,-4,-4)
if (algebra.sub(Q1,Q2) == Q1sQ2): numTrueQuat = numTrueQuat + 1

# Test 3: Conjugate
Q1conj = algebra.quat(1,-2,-3,-4)
if (algebra.conj(Q1) == Q1conj): numTrueQuat = numTrueQuat + 1

# Test: Multiplication
E0 = algebra.quat(1,0,0,0)
nE0 = algebra.quat(-1,0,0,0)
E1 = algebra.quat(0,1,0,0)
nE1 = algebra.quat(0,-1,0,0)
E2 = algebra.quat(0,0,1,0)
nE2 = algebra.quat(0,0,-1,0)
E3 = algebra.quat(0,0,0,1)
nE3 = algebra.quat(0,0,0,-1)

for i in xrange(4):
  for j in xrange(4):
    q1 = algebra.quat(i==0,i==1,i==2,i==3)    
    q2 = algebra.quat(j==0,j==1,j==2,j==3)
    q3 = algebra.mult(q1,q2)
    if (i == j and i != 0):
      numTrueQuat = numTrueQuat + (q3 == nE0)
    if (i == 0):
      numTrueQuat = numTrueQuat + (q3 == algebra.quat(j==0,j==1,j==2,j==3))
    elif (j == 0):
      numTrueQuat = numTrueQuat + (q3 == algebra.quat(i==0,i==1,i==2,i==3))
    if (i == 2 and j == 1):
      numTrueQuat = numTrueQuat + (q3 == nE3)
    if (i == 3 and j == 1):
      numTrueQuat = numTrueQuat + (q3 == E2)
    if (i == 3 and j == 2):
      numTrueQuat = numTrueQuat + (q3 == nE1)
    if (i == 1 and j == 2):
      numTrueQuat = numTrueQuat + (q3 == E3)
    if (i == 1 and j == 3):
      numTrueQuat = numTrueQuat + (q3 == nE2)
    if (i == 2 and j == 3):
      numTrueQuat = numTrueQuat + (q3 == E1)

# Results
if (numTrueQuat == numTestsQuat):
  print "Quaternion tests pass"
else:
  print "Quaternion tests fail: " + str(numTrueQuat) + " passed out of " + str(numTestsQuat)
