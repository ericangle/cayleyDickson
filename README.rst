.. role:: raw-math(raw)
    :format: latex html

cayleyDickson
=============

Implementation of the Cayley–Dickson algebras using the `Cayley-Dickson construction <https://en.wikipedia.org/wiki/Cayley–Dickson_construction>`__, including (but not limited to) the real and complex numbers, quaternions, octonions, and sedenions.

In this construction, starting with the real numbers, the next algebra in the sequence is an ordered pair of the previous algebra in the sequence, with multiplication defined by

(a,b)(c,d) = (ac-d*b,da+bc*)

where * denotes conjugation, defined by

(a,b)* = (a*,-b)

For complex numbers, composed of two real numbers, multiplication and conjugation reduce to the familiar

(a,b)(c,d) = (ac-db,da+bc)

and

(a,b)* = (a,-b)

respectively.

Real Example
------------------

.. code-block:: python

    >>> from algebra import Algebra as alg
    >>> R1 = alg(2)
    >>> R2 = alg(3)
    >>> print(R1 + R2)
    [5]
    >>> print(R1 - R2)
    [-1]
    >>> print(R1 * R2)
    [6]
    >>> print(R1 / R2)
    [0.6666666666666666]

Complex Example
------------------

.. code-block:: python

    >>> from algebra import Algebra as alg
    >>> C1 = alg(1,2)
    >>> C2 = alg(3,4)
    >>> C1.norm()
    2.23606797749979
    >>> print(C1.conj())
    [1, -2]
    >>> C1 == alg(alg(1),alg(2))
    True
    >>> print(C1 + C2)
    [4, 6]
    >>> print(C1 - C2)
    [-2, -2]
    >>> print(C1 * C2)
    [-5, 10]
    >>> print(C1 / C2)
    [0.44, 0.08]

Quaternion Example
------------------

.. code-block:: python

    >>> from algebra import Algebra as alg
    >>> Q1 = alg(1,2,3,4)
    >>> Q2 = alg(5,6,7,8)
    >>> print(Q1.conj())
    [1, -2, -3, -4]
    >>> Q1 == alg(alg(1,2),alg(3,4))
    True
    >>> Q1.norm()
    5.477225575051661
    >>> print(Q1 + Q2)
    [6, 8, 10, 12]
    >>> print(Q1 - Q2)
    [-4, -4, -4, -4]
    >>> print(Q1 * Q2)
    [-60, 12, 30, 24]
    >>> print(Q1 / Q2)
    [0.40229885057471265, 0.04597701149425287, 0.0, 0.09195402298850575]
    >>> print(Q1.commutator(Q2))
    [0, -8, 16, -8]


Octonion Example
------------------

.. code-block:: python

    >>> from algebra import Algebra as alg
    >>> O1 = alg(1,2,3,4,5,6,7,8)
    >>> O2 = alg(9,10,11,12,13,14,15,16)
    >>> print(O1.conj())
    [1, -2, -3, -4, -5, -6, -7, -8]
    >>> O1 == alg(alg(1,2,3,4),alg(5,6,7,8))
    True
    >>> O1.norm()
    14.2828568570857
    >>> print(O1+O2)
    [10, 12, 14, 16, 18, 20, 22, 24]
    >>> print(O1-O2)
    [-8, -8, -8, -8, -8, -8, -8, -8]
    >>> print(O1*O2)
    [-474, 20, 22, 24, 154, 60, 30, 96]
    >>> print(O1/O2)
    [0.38080495356037153, 0.01238390092879257, 0.02476780185758514, 0.03715170278637771, -0.04953560371517028, 0.03715170278637771, 0.07430340557275542, 0.03715170278637771]
    >>> print(O1.commutator(O2))
    [0, -16, -32, -48, 192, -16, -96, 16]
    >>> O3=alg(0,1,0,1,0,1,0,1)
    >>> print(O1.associator(O2,O3))
    [0, 64, -192, 64, 64, 0, 128, -128]

Run Tests
------------------

To run the tests, run the script testAll.sh from the parent directory.
