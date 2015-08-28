cayleyDickson
=============

Implementation of the Cayley–Dickson algebras, including the real and complex numbers, quaternions, and octonions.

Real Example
------------------

.. code-block:: python

    >>> from algebra.py import Algebra as alg
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
