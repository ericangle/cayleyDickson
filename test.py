import algebra

print " "

###########
# Complex #
###########

nTrueC = 0
nTestsC = 6

C1 = algebra.alg([1,2])
C2 = algebra.alg([3,4])

# Test 1: Addition
nTrueC = nTrueC + (algebra.add(C1,C2) == algebra.alg([1+3,2+4]))

# Test 2: Subtraction
nTrueC = nTrueC + (algebra.sub(C1,C2) == algebra.alg([1-3,2-4]))

# Test 3: Conjugate
nTrueC = nTrueC + (algebra.conj(C1) == algebra.alg([1,-2]))

# Test 4: Modulus
nTrueC = nTrueC + (algebra.mod(C1) == pow(sum (pow(i,2.0) for i in range(1,2+1)),0.5))

# Test 5: Multiplication
nTrueC = nTrueC + (algebra.mult(C1,C2) == algebra.alg([1*3-2*4,1*4+2*3]))

# Test 6: Division
nTrueC = nTrueC + (algebra.div(C1,C2) == algebra.alg([11.0/25.0,2.0/25.0]))

# Results
if (nTrueC == nTestsC):
  print "Complex tests pass: " + str(nTrueC) + " passed out of " + str(nTestsC)
else:
  print "Complex tests fail: " + str(nTrueC) + " passed out of " + str(nTestsC)
  
##############
# Quaternion #
##############

nTrueQ = 0
nTestsQ = 4 + 4*4

Q1 = algebra.alg([1,2,3,4])
Q2 = algebra.alg([5,6,7,8])

# Test 1: Addition
nTrueQ = nTrueQ + (algebra.add(Q1,Q2) == algebra.alg([1+5,2+6,3+7,4+8]))

# Test 2: Subtraction
nTrueQ = nTrueQ + (algebra.sub(Q1,Q2) == algebra.alg([1-5,2-6,3-7,4-8]))

# Test 3: Conjugate
nTrueQ = nTrueQ + (algebra.conj(Q1) == algebra.alg([1,-2,-3,-4]))

# Test 4: Modulus
nTrueQ = nTrueQ + (algebra.mod(Q1) == pow(sum (pow(i,2.0) for i in range(1,4+1)),0.5))

# Test 5: Multiplication
E0  = algebra.alg([1,0,0,0])
nE0 = algebra.alg([-1,0,0,0])
E1  = algebra.alg([0,1,0,0])
nE1 = algebra.alg([0,-1,0,0])
E2  = algebra.alg([0,0,1,0])
nE2 = algebra.alg([0,0,-1,0])
E3  = algebra.alg([0,0,0,1])
nE3 = algebra.alg([0,0,0,-1])

for i in xrange(4):
  for j in xrange(4):
    q1 = algebra.alg([(i==0)*1,(i==1)*1,(i==2)*1,(i==3)*1])    
    q2 = algebra.alg([(j==0)*1,(j==1)*1,(j==2)*1,(j==3)*1])
    q3 = algebra.mult(q1,q2)

    # 3 Tests: i,j = 1,2,3
    if (i == j and i != 0):
      nTrueQ = nTrueQ + (q3 == nE0)
    # 4 Tests: i = 0, j = 0,1,2,3
    if (i == 0):
      nTrueQ = nTrueQ + (q3 == algebra.alg([(j==0)*1,(j==1)*1,(j==2)*1,(j==3)*1]))
    # 3 Tests: j = 0, i = 1,2,3
    elif (j == 0):
      nTrueQ = nTrueQ + (q3 == algebra.alg([(i==0)*1,(i==1)*1,(i==2)*1,(i==3)*1]))
    # 6 Tests: off diag with i and j not 0
    nTrueQ = nTrueQ + (i == 2 and j == 1)*(q3 == nE3) + (i == 3 and j == 1)*(q3 == E2) + (i == 3 and j == 2)*(q3 == nE1) + (i == 1 and j == 2)*(q3 == E3) + (i == 1 and j == 3)*(q3 == nE2) + (i == 2 and j == 3)*(q3 == E1)

# Test 6: Division
#nTrueQ = nTrueQ + (algebra.div(Q1,Q2) == algebra.alg(place,holder,for,now))

# Results
if (nTrueQ == nTestsQ):
  print "Quaternion tests pass: " + str(nTrueQ) + " passed out of " + str(nTestsQ)
else:
  print "Quaternion tests fail: " + str(nTrueQ) + " passed out of " + str(nTestsQ)

############
# Octonion #
############

nTrueO = 0
nTestsO = 4

O1 = algebra.alg([1,2,3,4,5,6,7,8])
O2 = algebra.alg([9,10,11,12,13,14,15,16])

# Test 1: Addition
nTrueO = nTrueO + (algebra.add(O1,O2) == algebra.alg([1+9,2+10,3+11,4+12,5+13,6+14,7+15,8+16]))

# Test 2: Subtraction
nTrueO = nTrueO + (algebra.sub(O1,O2) == algebra.alg([1-9,2-10,3-11,4-12,5-13,6-14,7-15,8-16]))

# Test 3: Conjugate
nTrueO = nTrueO + (algebra.conj(O1) == algebra.alg([1,-2,-3,-4,-5,-6,-7,-8]))

# Test 4: Modulus
nTrueO = nTrueO + (algebra.mod(O1) == pow(sum (pow(i,2.0) for i in range(1,8+1)),0.5) )

# Test 5: Multiplication
# add 8x8 mult table

# Test 6: Division
#nTrueO = nTrueO + (algebra.div(O1,O2) == algebra.alg(place,holder,for,now))

# Results
if (nTrueO == nTestsO):
  print "Octonion tests pass: " + str(nTrueO) + " passed out of " + str(nTestsO)
else:
  print "Octonion tests fail: " + str(nTrueO) + " passed out of " + str(nTestsO)

print " "
