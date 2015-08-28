.. role:: raw-math(raw)
    :format: latex html

cayleyDickson
=============

Implementation of the Cayley–Dickson algebras using the `Cayley-Dickson construction <https://en.wikipedia.org/wiki/Cayley–Dickson_construction>`__, including (but not limited to) the real and complex numbers, quaternions, octonions, and sedenions.

.. math:: (a + b)^2 = a^2 + 2ab + b^2

.. math::
    
    \sin{a + b}

    :raw-math:`$$ \frac{s}{\sqrt{N}} $$`

conjugation

multiplaication


Real Example
------------------

.. code-block:: python

    >>> from algebra import Algebra as alg
    >>> R1 = alg(2)
    >>> R2 = alg(3)
    >>> (R1 + R2).asList()
    [5]
    >>> (R1 - R2).asList()
    [-1]
    >>> (R1 * R2).asList()
    [6]
    >>> (R1 / R2).asList()
    [0.6666666666666666]

Complex Example
------------------

.. code-block:: python

    >>> from algebra import Algebra as alg
    >>> C1 = alg(1,2)
    >>> C2 = alg(3,4)
    >>> C1.norm()
    2.23606797749979
    >>> C1.conj().asList()
    [1, -2]
    >>> C1 == alg(alg(1),alg(2))
    True
    >>> (C1 + C2).asList()
    [4, 6]
    >>> (C1 - C2).asList()
    [-2, -2]
    >>> (C1 * C2).asList()
    [-5, 10]
    >>> (C1 / C2).asList()
    [0.44, 0.08]

Quaternion Example
------------------

.. code-block:: python

    >>> from algebra import Algebra as alg
    >>> Q1 = alg(1,2,3,4)
    >>> Q2 = alg(5,6,7,8)
    >>> Q1.conj().asList()
    [1, -2, -3, -4]
    >>> Q1 == alg(alg(1,2),alg(3,4))
    True
    >>> Q1.norm()
    5.477225575051661
    >>> (Q1 + Q2).asList()
    [6, 8, 10, 12]
    >>> (Q1 - Q2).asList()
    [-4, -4, -4, -4]
    >>> (Q1 * Q2).asList()
    [-60, 12, 30, 24]
    >>> (Q1 / Q2).asList()
    [0.40229885057471265, 0.04597701149425287, 0.0, 0.09195402298850575]
    >>> Q1.commutator(Q2).asList()
    [0, -8, 16, -8]
