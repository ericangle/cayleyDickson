# TO DO
# 1. All functions should check that list1.len ==
#    list2.len, or should promote the shorter one
#    to the length of the longer one, i.e. complex
#    becomes a quaternion, octonion, etc.

import math

# Returns list nums as nested lists as
# in the Cayley Dickson construction
def alg(nums):
  if len(nums) == 1:
    return nums[0]
  else:
    # powerOfTwo = 1,2,3,... = complex,quaternion,octonion,...
    powerOfTwo = math.log(len(nums))/math.log(2)
    if powerOfTwo != int(powerOfTwo):
      print "number list must be a length that is a power of 2"
      return 0
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

# Pretty print
def prettyPrint(myList):
  output = "[ "
  tempList = tempPrettyPrint(myList)
  for i in xrange(len(tempList)):
    output = output + tempList[i] + " "
  output = output + "]"
  print output
  return 0

def tempPrettyPrint(myList):
  if isinstance(myList, (int, long, float)):
    return str(myList)
  else:
    output = ""
    for i in xrange(len(myList)):
      output = output + tempPrettyPrint(myList[i])
    return output

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
    total.append(sub(mult(a,c),mult(conj(d),b)))
    total.append(add(mult(d,a),mult(b,conj(c))))
    return total

# Modulus
# |a| = (a a*)^1/2
def mod(myList):
  if isinstance(myList, (int, long, float)):
    return myList
  else:
    sum = 0
    for i in xrange(len(myList)):
      sum = sum + pow(mod(myList[i]),2.0)
    return pow(sum,0.5)

# Division
# a / b = ab* / (bb*)
def div(a,b):
  invBBconj = list()
  invBBconj.append(1.0/pow(mod(b),2.0))
  for i in range(1,listLen(a)):
    invBBconj.append(0.0)
  return mult(mult(a,conj(b)),alg(invBBconj))

# Conjugation
# (a,b)* = (a*,-b)
def conj(myList):
  if listLen(myList) == 1:
    return myList
  else:
    if listLen(myList) == 2:
      zeroes = 0.0
    else:
      zeroes = list()
      for i in xrange(listLen(myList)/2):
        zeroes.append(0.0)
      zeroes = alg(zeroes)
    result = list()
    result.append(conj(myList[0]))
    result.append(sub(zeroes,myList[1]))
    return result
