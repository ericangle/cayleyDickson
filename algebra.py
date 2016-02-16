import math

# First attempt: assume all operations are done with Algebras
# of the same length

class Algebra:
  # constructor
  def __init__(self,*args):
    def allIntOrFloat(args):
      for arg in args:
        if not (type(arg) == int or type(arg) == float):
          return False
      return True

    def allAlgebra(args):
      for arg in args:
        if not (type(arg) == Algebra):
          return False
      return True

    if len(args) == 0:
      print("ERROR: Can't call constructor with 0 arguments.")
      exit()    
    elif len(args) == 1:
      arg = args[0]
      if type(arg) == int or type(arg) == float:
        self.a = arg
        self.b = None
      elif type(arg) == list or type(arg) == tuple:
        if len(arg) == 0:
          print("ERROR: Can't call constructor with empty list or tuple.")
          exit()    
        elif len(arg) == 1:
          self.a = arg[0]
          self.b = None
        else:
          self.a = Algebra(arg[:len(arg)//2])
          self.b = Algebra(arg[len(arg)//2:])
      else:
        print("ERROR: when calling constructor with single argument, must be number, list, or tuple.")
        exit()    
    else:
      if allIntOrFloat(args):
        self.a = Algebra(args[:len(args)//2])
        self.b = Algebra(args[len(args)//2:]) 
      elif allAlgebra(args):
        if len(args) == 2:
          algebra1 = args[0]
          algebra2 = args[1]
          if len(algebra1) != len(algebra2):
            # Could decide to handle this later, for now error
            print("ERROR: can't call constructor with algebras of different lengths.")
            exit()    
          else:
            self.a = algebra1
            self.b = algebra2
        else:
          print("ERROR: can call constructor with exactly 2 algebra instances only")
          exit()    
      else:
        print("ERROR: called constructor with 2 or more arguments that were not all either numbers or algebras")
        exit()    

  def isReal(self):
    return self.b is None

  # override equality
  def __eq__(self,other):
    if self.isReal():
      return self.a == other.a
    else:
      return self.a == other.a and self.b == other.b

  # override length
  def __len__(self):
    if self.isReal():
      return 1
    else:
      return len(self.a) + len(self.b)

  # Negation
  def neg(self):
    if self.isReal():
      return Algebra(-self.a)
    else:
      return Algebra(self.a.neg(),self.b.neg())
    
  # override addition
  # (a,b)+(c,d) = (a+c,b+d)
  def __add__(self,other):
    if self.isReal():
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
    if self.isReal():
      return Algebra(self.a * other.a)
    else:
      return Algebra(self.a * other.a - other.b.conj() * self.b,
                     other.b * self.a + self.b * other.a.conj())

  # override division
  # a / b = a b* (1/(bb*))
  def __floordiv__(self,other):
    if self.isReal():
      return Algebra(self.a / other.a)
    else:
      return self * other.conj() * Algebra([1.0/pow(other.norm(),2.0)] + [0.0 for i in range(len(other)-1)])   
  def __truediv__(self,other):
    if self.isReal():
      return Algebra(float(self.a) / float(other.a))
    else:
      return self * other.conj() * Algebra([1.0/pow(other.norm(),2.0)] + [0.0 for i in range(len(other)-1)])     
  def __div__(self,other):
    if self.isReal():
      return Algebra(float(self.a) / float(other.a))
    else:
      return self * other.conj() * Algebra([1.0/pow(other.norm(),2.0)] + [0.0 for i in range(len(other)-1)])   
  # commutator
  # [a,b] = a * b - b * a
  def commutator(self,other):
    return self * other - other * self

  # associator
  # [x, y, z] = (x * y) * z - x * (y * z)
  def associator(self,other1,other2):
    return (self * other1) * other2 - self * (other1 * other2)

  # norm / modulus
  def norm(self):
    if self.isReal():
      return abs(self.a)
    else:
      return pow((self * self.conj()).asList()[0],0.5)

  # Conjugation
  # (a,b)* = (a*,-b)
  def conj(self):
    if self.isReal():
      return self
    else:
      return Algebra(self.a.conj(),self.b.neg())

  def asList(self):
    if self.isReal():
      return [self.a]
    else:
      return self.a.asList() + self.b.asList()

  # overriding string
  def __str__(self):
    return str(self.asList())

  # overriding repr
  def __repr__(self):
    return 'Algebra' + str(tuple(self.asList()))
