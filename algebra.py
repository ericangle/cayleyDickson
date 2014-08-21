# make a pretty print function at some point

def complex(a,b):
# check that a and b are numbers not lists
  myComplex = list()
  myComplex.append(a)
  myComplex.append(b)
  return myComplex

def quat(a,b,c,d):
# check that a and b are complex numbers
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
# (a,b)(c,d) = (ac-db*,a*d+bc)
def mult(list1,list2):
  length = listLen(list1)
  if length == 1:
    return list1*list2
  else:
    total = list()
    a = list1[0]
    b = list1[1]
    c = list2[0]
    d = list2[1]
    left = sub(mult(a,c),mult(d,conj(b)))
    right = add(mult(conj(a),d),mult(b,c))
    total.append(left)
    total.append(right)
    return total

# Division
# a / b = ab* / (bb*)
# def div(list1,list2)

# Conjugation
# (a,b)* = (a*,-b)
def conj(myList):
  length = listLen(myList)
  if length == 1:
    return myList
  else:
    left = conj(myList[0])
    if listLen(left) == 1:
      right = sub(0,myList[1])
    else:
      zeroes = list()
      for i in xrange(listLen(left)):
        zeroes.append(0)
      right = sub(zeroes,myList[1])
    result = list()
    result.append(left)
    result.append(right)
    return result
