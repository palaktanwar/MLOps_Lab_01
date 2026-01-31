import pytest
import sys
import os

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(project_root)
from src.maths import findOddEven, findfibbonaci

def test_fibbonaci():
    assert findfibbonaci(8) == 21
    assert findfibbonaci(5) == 5
    assert findfibbonaci(3) == 2
    assert findfibbonaci(10) == 55

def test_oddeven():
    assert findOddEven(8) == "Even"
    assert findOddEven(82) == "Even"
    assert findOddEven(1) == "Odd"
    assert findOddEven(7) == "Odd"

