#!/bin/bash

py.test --genscript=mypytestscript

python3 mypytestscript testAlgebra.py testRotation.py
