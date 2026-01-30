import unittest

def count_four_legged_animals(animals):
    
    animals_legs = {'lion': 4, 'cat': 4, 'ant': 6, 'spider': 8, 'dog': 4, 'snake': 0, 'monkey': 2, 'parrot': 2,
                  'worm': 0, 'elephant': 4, 'frog': 2, 'horse': 4,
                  }
    
    if not animals:
        return 0
    
    count = 0
    
    for animal in animals:
     if not isinstance(animals , str):
            continue
     if animals_legs.get(animal.lower()) == 4:
         
         count += 1
         
         return 0