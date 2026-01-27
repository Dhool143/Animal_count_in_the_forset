
import unittest


def count_four_legged_animals(animals):
    
    if not animals:
        return 0
    
    
    animals_legs = {'lion': 4, "cat": 4, 'ant': 6, 'spider': 8, 'sanke': 0, 'monkey': 2, 'elephan': 4, 'worm': 0, 'parrot': 2, 'deer': 4, 'dog': 4,
        
        
    }
    
    count = 0
    for animal in animals:
        if animals_legs.get(animal.lower()) == 4:
            count +=1
            
            
            return count
        
    