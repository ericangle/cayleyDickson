#!/bin/bash

py.test --genscript=mypytestscript

python3 mypytestscript test/testAlgebra.py test/testRotation.py
