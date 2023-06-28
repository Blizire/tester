import sys
sys.path.append('..')  # hack to import module in parent dir...
from lmath import lmath
import pytest

def test_add():
    assert lmath.add(5,5) == 10

def test_sub():
    assert lmath.sub(10,5) == 5

def test_mult():
    assert lmath.mult(5,5) == 25

def test_div():
    assert lmath.div(5,5) == 1
