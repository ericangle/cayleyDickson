# make a pretty print function at some point

def complex(a,b):
# check that a and b are numbers not lists
  myComplex = list()
  myComplex.append(a)
  myComplex.append(b)
  return myComplex

def quat(a,b,c,d):
  myQuat = list()
  myComplex1 = list()
  myComplex2 = list()
  myComplex1.append(a)
  myComplex1.append(b)
  myComplex2.append(c)
  myComplex2.append(d)
  myQuat.append(myComplex1)
  myQuat.append(myComplex2)
  return myQuat

def octon(a,b,c,d,e,f,g,h):
  myOcton = list()
  myQuat1 = list()
  myQuat2 = list()
  myComplex1 = list()
  myComplex2 = list()
  myComplex3 = list()
  myComplex4 = list()
  myComplex1.append(a)
  myComplex1.append(b)
  myComplex2.append(c)
  myComplex2.append(d)
  myComplex3.append(e)
  myComplex3.append(f)
  myComplex4.append(g)
  myComplex4.append(h)
  myQuat1.append(myComplex1)
  myQuat1.append(myComplex2)
  myQuat2.append(myComplex3)
  myQuat2.append(myComplex4)
  myOcton.append(myQuat1)
  myOcton.append(myQuat2)
  return myOcton

# Calculates total length of nested list
def listLen(myList):
  if isinstance(myList, (int, long, float)):
    return 1
  else:
    sum = 0
    for i in xrange(len(myList)):
      sum = sum + listLen(myList[i])
    return sum

# Addition
# (a,b)+(c,d) = (a+c,b+d)
def add(list1,list2):
  if listLen(list1) == 1:
    return list1 + list2
  else:
    return [add(list1[i],list2[i]) for i in xrange(len(list1))]

# Subtraction
# (a,b)-(c,d) = (a-c,b-d)
def sub(list1,list2):
  if listLen(list1) == 1:
    return list1 - list2
  else:
    return [sub(list1[i],list2[i]) for i in xrange(len(list1))]

# Multiplication
# (a,b)(c,d) = (ac-d*b,da+bc*)
def mult(list1,list2):
  if listLen(list1) == 1:
    return list1*list2
  else:
    total = list()
    a = list1[0]
    b = list1[1]
    c = list2[0]
    d = list2[1]
    left = sub(mult(a,c),mult(conj(d),b))
    right = add(mult(d,a),mult(b,conj(c)))
    total.append(left)
    total.append(right)
    return total

# Modulus
# |a| = (a a*)^1/2
def mod(myList):
  if listLen(myList) == 2:
    return pow(mult(myList,conj(myList))[0],0.5)
  if listLen(myList) == 4:
    return pow(mult(myList,conj(myList))[0][0],0.5)
  if listLen(myList) == 8:
    return pow(mult(myList,conj(myList))[0][0][0],0.5)

# Division
# a / b = ab* / (bb*)
# def div(list1,list2)
def div(list1,list2):
  modSqList2 = pow(mod(list2),2.0)
  invModSqList2 = list()
  if listLen(list1) == 2:
    invModSqList2 = complex(1.0/modSqList2,0.0)
  if listLen(list1) == 4:
    invModSqList2 = quat(1.0/modSqList2,0,0,0)
  if listLen(list1) == 8:
    invModSqList2 = octon(1.0/modSqList2,0.0)
  return mult(mult(list1,conj(list2)),invModSqList2)

# Conjugation
# (a,b)* = (a*,-b)
def conj(myList):
  if listLen(myList) == 1:
    return myList
  else:
    left = conj(myList[0])
    if listLen(left) == 1:
      zeroes = 0
    elif listLen(left) == 2:
      zeroes = list()
      zeroes = complex(0,0)
    elif listLen(left) == 4:
      zeroes = list()
      zeroes = quat(0,0,0,0)
    right = sub(zeroes,myList[1])
    result = list()
    result.append(left)
    result.append(right)
    return result
