import math

# First attempt: assume all operations are done with Algebras
# of the same length

class Algebra:
  # constructor
  def __init__(self,a,b=None):
    if b is None:
      if type(a) == float or type(a) == int:
        self.a = a
        self.b = b
        self.isReal = True
      elif type(a) == list:
        if len(a) == 1:
          self.a = a[0]
          self.b = b
          self.isReal = True
        else:
          powerOfTwo = math.log(len(a))/math.log(2)
          if powerOfTwo == int(powerOfTwo):
            self.a = Algebra(a[:len(a)/2])
            self.b = Algebra(a[len(a)/2:])
            self.isReal = False
          else:
            print "error: ..."
            exit()
      else:
        # a is an Algebra or something else
        # which isn't allowed
        print "error: ..."
        exit()

    # b != None
    else:
      if type(a) == list:
        print "error"
        exit()
      else:
        #if len(a) == len(b):
        if type(a) == int or type(a) == float:
          self.a = Algebra(a)
          self.b = Algebra(b)
          self.isReal = False
        else:
          self.a = a
          self.b = b
          self.isReal = False
     # else:
     #   print "error: .."
     #   exit()

#  def isReal(self):
#    return (type(self.a) == int or type(self.a) == float) and (self.b == None)

  # override equality
  def __eq__(self,other):
    if self.isReal:
      return self.a == other.a
    else:
      return self.a == other.a and self.b == other.b

  # override length
  def __len__(self):
    if self.isReal:
      return 1
    else:
      return len(self.a) + len(self.b)

  def neg(self):
    if self.isReal:
      return Algebra(-self.a)
    else:
      return Algebra(self.a.neg(),self.b.neg())
    
  # override addition
  # (a,b)+(c,d) = (a+c,b+d)
  def __add__(self,other):
    if self.isReal:
      return Algebra(self.a + other.a)
    else:
      return Algebra(self.a + other.a, self.b + other.b)

  # override subtraction
  # (a,b)-(c,d) = (a-c,b-d)
  def __sub__(self,other):
    return self + other.neg()

  # override multiplication
  # (a,b)(c,d) = (ac-d*b,da+bc*)
  def __mul__(self,other):
    if self.isReal:
      return Algebra(self.a * other.a)
    else:
      return Algebra(self.a * other.a - other.b.conj() * self.b,
                     other.b * self.a + self.b * other.a.conj())

  # override division
  # a / b = a b* (1/(bb*))
  def __div__(self,other):
    if self.isReal:
      return Algebra(self.a / other.a)
    else:
      return self * other.conj() * Algebra([1.0/pow(other.norm(),2.0)] + [0.0 for i in xrange(len(other)-1)])   
  # norm / modulus
  def norm(self):
    if self.isReal:
      return abs(self.a)
    else:
      return pow((self * self.conj()).asList()[0],0.5)

  # Conjugation
  # (a,b)* = (a*,-b)
  def conj(self):
    if self.isReal:
      return self
    else:
      return Algebra(self.a.conj(),self.b.neg())

  def asList(self):
    if self.isReal:
      return [self.a]
    else:
      return self.a.asList() + self.b.asList()
