
import unittest

from main import count_four_legged_animals


# Normal test cases


def test_normal_cases():
  
  assert count_four_legged_animals({'lion', 'deer'}) == 2
  assert count_four_legged_animals({'elephan', 'monkey'}) == 1
  assert count_four_legged_animals({'dog' , 'cat'}) == 2


# Edge test Cases


def test_edge_cases():
  
  assert count_four_legged_animals({'worm', 'snake'}) == 0
  assert count_four_legged_animals({'spider', 'ant'}) == 0
  assert count_four_legged_animals({None}) == 0
  assert count_four_legged_animals({}) == 0
  
  
  print('All tests passed!')












