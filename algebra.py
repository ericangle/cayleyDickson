
# Addition
def add(list1,list2):
  return [list1[i]+list2[i] for i in xrange(len(list1))]

# Subtraction
def sub(list1,list2):
  return [list1[i]-list2[i] for i in xrange(len(list1))]

# Multiplication
# (a,b)(c,d) = (ac-db*,a*d+bc)
def mult(list1,list2):
  

# Conjugation



A1 = list()
A2 = list()
A3 = list()

A1.append(1)
A1.append(2)


A2.append(3)
A2.append(4)

A3.append(A1)
A3.append(A2)

A4 = list()
A4.append(A1)
A4.append(A2)

A5 = list()
A5.append(A3)
A5.append(A4)

A6 = add(A1,-A2)

print A6
