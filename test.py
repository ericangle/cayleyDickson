import algebra

A1 = algebra.complex(1,2)
A2 = algebra.complex(3,4)

print "[1,2] + [3,4] = " + str(algebra.add(A1,A2))
print "[1,2] - [3,4] = " + str(algebra.sub(A1,A2))
print "[1,2]* = " + str(algebra.conj(A1))
print "[3,4]* = " + str(algebra.conj(A2))
print "[1,2][3,4] = " + str(algebra.mult(A1,A2))

print " "

# Quaternion multiplication table
numTrue = 0
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
      numTrue = numTrue + (q3 == nE0)
    if (i == 0):
      numTrue = numTrue + (q3 == algebra.quat(j==0,j==1,j==2,j==3))
    elif (j == 0):
      numTrue = numTrue + (q3 == algebra.quat(i==0,i==1,i==2,i==3))
    if (i == 2 and j == 1):
      numTrue = numTrue + (q3 == nE3)
    if (i == 3 and j == 1):
      numTrue = numTrue + (q3 == E2)
    if (i == 3 and j == 2):
      numTrue = numTrue + (q3 == nE1)
    if (i == 1 and j == 2):
      numTrue = numTrue + (q3 == E3)
    if (i == 1 and j == 3):
      numTrue = numTrue + (q3 == nE2)
    if (i == 2 and j == 3):
      numTrue = numTrue + (q3 == E1)

print numTrue
print (numTrue == 16)
