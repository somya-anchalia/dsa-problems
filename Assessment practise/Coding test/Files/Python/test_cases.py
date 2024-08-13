import unittest
from main import compare

class TestOfficerComparison(unittest.TestCase):
    
    def test_similar_officers(self):
        officer_1 = {
            "name": "KADAMA, Roger Martin",
            "role": "director",
            "date_of_birth": "3/1982"
        }
        
        officer_2 = {
            "name": "KADAMA, Roger Martin",
            "role": "director",
            "date_of_birth": "3/1982"
        }
        
        self.assertTrue(compare(officer_1, officer_2))
        
    def test_different_officers(self):
        officer_1 = {
            "name": "KADAMA, Roger Martin",
            "role": "director",
            "date_of_birth": "3/1982"
        }
        
        officer_2 = {
            "name": "WALL, Arnold",
            "role": "director",
            "date_of_birth": "4/1955"
        }
        
        self.assertFalse(compare(officer_1, officer_2))

if __name__ == '__main__':
    unittest.main()
