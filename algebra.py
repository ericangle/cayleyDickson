# TO DO
# 1. make a pretty print function at some point
# 2. modulus function is not general

import math

# Returns list nums as nested lists as
# in the Cayley Dickson construction
def alg(nums):
  powerOfTwo = math.log(len(nums))/math.log(2)
  if powerOfTwo != int(powerOfTwo):
    print "number list must be a length that is a power of 2"
    return 0
  elif len(nums) == 2:
    temp = list()
    temp.append(nums[0])
    temp.append(nums[1])
    return temp
  else:
    temp = list()
    temp.append(alg(nums[:len(nums)/2]))
    temp.append(alg(nums[len(nums)/2:]))
    return temp

# Calculates total length of a nested list
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
def div(list1,list2):
  modSqList2 = pow(mod(list2),2.0)
  temp = list()
  temp.append(1.0/modSqList2)
  for i in range(1,listLen(list1)):
    temp.append(0.0)
  invModSqList2 = alg(temp)
  return mult(mult(list1,conj(list2)),invModSqList2)

# Conjugation
# (a,b)* = (a*,-b)
def conj(myList):
  if listLen(myList) == 1:
    return myList
  else:
    left = conj(myList[0])
    if listLen(left) == 1:
      zeroes = 0.0
    else:
      temp = list()
      for i in xrange(listLen(left)):
        temp.append(0.0)
      zeroes = alg(temp) 
    right = sub(zeroes,myList[1])
    result = list()
    result.append(left)
    result.append(right)
    return result
