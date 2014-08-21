import algebra

###########
# Complex #
###########

nTrueC = 0
nTestsC = 4

C1 = algebra.complex(1,2)
C2 = algebra.complex(3,4)

# Test 1: Addition
nTrueC = nTrueC + (algebra.add(C1,C2) == algebra.complex(1+3,2+4))

# Test 2: Subtraction
nTrueC = nTrueC + (algebra.sub(C1,C2) == algebra.complex(1-3,2-4))

# Test 3: Conjugate
nTrueC = nTrueC + (algebra.conj(C1) == algebra.complex(1,-2))

# Test 4: Multiplication
nTrueC = nTrueC + (algebra.mult(C1,C2) == algebra.complex(1*3-2*4,1*4+2*3))

# Results
if (nTrueC == nTestsC):
  print "Complex tests pass"
else:
  print "Complex tests fail: " + str(nTrueC) + " passed out of " + str(nTestsC)
  
##############
# Quaternion #
##############

nTrueQ = 0
nTestsQ = 3 + 16

Q1 = algebra.quat(1,2,3,4)
Q2 = algebra.quat(5,6,7,8)

# Test 1: Addition
nTrueQ = nTrueQ + (algebra.add(Q1,Q2) == algebra.quat(1+5,2+6,3+7,4+8))

# Test 2: Subtraction
nTrueQ = nTrueQ + (algebra.sub(Q1,Q2) == algebra.quat(1-5,2-6,3-7,4-8))

# Test 3: Conjugate
nTrueQ = nTrueQ + (algebra.conj(Q1) == algebra.quat(1,-2,-3,-4))

# Test 4: Multiplication
E0  = algebra.quat(1,0,0,0)
nE0 = algebra.quat(-1,0,0,0)
E1  = algebra.quat(0,1,0,0)
nE1 = algebra.quat(0,-1,0,0)
E2  = algebra.quat(0,0,1,0)
nE2 = algebra.quat(0,0,-1,0)
E3  = algebra.quat(0,0,0,1)
nE3 = algebra.quat(0,0,0,-1)

for i in xrange(4):
  for j in xrange(4):
    q1 = algebra.quat(i==0,i==1,i==2,i==3)    
    q2 = algebra.quat(j==0,j==1,j==2,j==3)
    q3 = algebra.mult(q1,q2)
    if (i == j and i != 0):
      nTrueQ = nTrueQ + (q3 == nE0)
    if (i == 0):
      nTrueQ = nTrueQ + (q3 == algebra.quat(j==0,j==1,j==2,j==3))
    elif (j == 0):
      nTrueQ = nTrueQ + (q3 == algebra.quat(i==0,i==1,i==2,i==3))
    nTrueQ = nTrueQ + (i == 2 and j == 1)*(q3 == nE3)
    + (i == 3 and j == 1)*(q3 == E2)
    + (i == 3 and j == 2)*(q3 == nE1)
    + (i == 1 and j == 2)*(q3 == E3)
    + (i == 1 and j == 3)*(q3 == nE2)
    + (i == 2 and j == 3)*(q3 == E1)

# Results
if (nTrueQ == nTestsQ):
  print "Quaternion tests pass"
else:
  print "Quaternion tests fail: " + str(nTrueQ) + " passed out of " + str(nTestsQ)

############
# Octonion #
############
