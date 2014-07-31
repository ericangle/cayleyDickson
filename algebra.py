
def listLen(myList):
  if isinstance(myList, (int, long, float)):
    return 1
  else:
    sum = 0
    for i in xrange(len(myList)):
      sum = sum + listLen(myList[i])
    return sum

# Addition
def add(list1,list2):
  if listLen(list1) == 1:
    return list1 + list2
  else:
    return [list1[i]+list2[i] for i in xrange(len(list1))]

# Subtraction
def sub(list1,list2):
  if listLen(list1) == 1:
    return list1 - list2
  else:
    return [list1[i]-list2[i] for i in xrange(len(list1))]

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

# Conjugation
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

A1 = list()
A2 = list()
A3 = list()

A1.append(1)
A1.append(2)

A2.append(3)
A2.append(4)

print "[1,2] + [3,4] = " + str(add(A1,A2))
print "[1,2] - [3,4] = " + str(sub(A1,A2))
print "[1,2]* = " + str(conj(A1))
print "[3,4]* = " + str(conj(A2))
print "[1,2][3,4] = " + str(mult(A1,A2))
