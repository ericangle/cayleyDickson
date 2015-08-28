cayleyDickson
=============

Implementation of the Cayley–Dickson algebras, including the real and complex numbers, quaternions, and octonions.

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
    >>> (C1 + C2).asList()
    [4, 6]
    >>> (C1 - C2).asList()
    [-2, -2]
    >>> (C1 * C2).asList()
    [-5, 10]
    >>> (C1 / C2).asList()
    [0.44, 0.08]
    >>> C1.norm()
    2.23606797749979
    >>> C1.conj().asList()
    [1, -2]
