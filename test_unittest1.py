import unittest
from app import printJoke
  
class SimpleTest(unittest.TestCase): 
    
    def test_testcase1(self):
        '''
        This test will always pass!
        '''         
        self.assertTrue(True) 
   
    def test_testcase2(self):
        '''
        Test to check if the response has an id or not.
        '''
        response_from_api = printJoke()
        if "id" in response_from_api:
            test_passed = True
        else:
            test_passed = False
        self.assertTrue(test_passed)

if __name__ == '__main__': 
    unittest.main() 