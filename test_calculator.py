import pytest
from calculator import calculate_average

def test_average_simple():
  assert calculate_average([10, 20, 30]) == 20.0
