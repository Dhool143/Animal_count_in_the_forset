import unittest

from main import count_four_legged_animals



class TestCountFourLeggedAnimals(unittest.TestCase):
    
    # Normal test cases
    
    def test_example_(self):
        animals =['lion', 'dog', 'elephant']
        self.assertEqual(count_four_legged_animals(), 3)
        
    def test_example_2(self):
        animals = ['cat', 'snake', 'frog']
        self.assertEqual(count_four_legged_animals(), 1)
        
        
    def test_match_animals(self):
        animals = ['elephant', 'horse',]
        self.assertEqual(count_four_legged_animals(), 2)
        
        
        
        # Edge test cases
        
        
        
    def test_unkown_animals(self):
        animals = ['cow', 'drogan']
        self.assertEqual(count_four_legged_animals(), 0)
        
        
    def test_duplicate_animals(self):
        animals = ['lion', 'dog' 'cat', 'snake']
        self.assertEqual(count_four_legged_animals(), 3)
        
        
    def test_empty_list(self):
    
      self.assertEqual(count_four_legged_animals([]) )
      
      
      
      
      if __name__ == '__main__':
          unittest.main()
        
        
    