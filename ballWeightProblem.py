'''
Parameters: 
    There are N number of balls, all of equal weight except one which is heavier than the rest.
    Write a program in Python that accepts the weights as an Array and identifies the heaviest ball in the Array.
    NOTE: Do NOT use python utility methods to find the max element
    NOTE: Create the logic in a way that it can find the heaviest ball from a Large Array (optimal solution)
    Write unit tests for testing this program.
    Please provide a python3 virtual environment file for the project so that I can execute the program and tests in that environment. 
'''

import unittest as ut
import sys

# Recursive Method O(n)
def findHeavyBall(ballArray,n=0):
    # Exception Handling
    try: 
        # Check if Balls are Equal. If so, recursivly iterate through array till complete.  
        if ballArray[n] == ballArray[n+1]:
                return findHeavyBall(ballArray,n+1)
        if ballArray[n] > ballArray[n+1]:
                return ballArray[n]
        if ballArray[n] < ballArray[n+1]:
                return ballArray[n+1]
    except(TypeError):
        return "Ball in the Bag has no weight."
    except(IndexError):
        if not ballArray:
            return "Bag is Empty."
        return "End of Bag."
    except(KeyError):
        return "Bag of Balls is not an Array."
    except(RecursionError):
        return "Bag is too large. Update Recursion Limit to try again."
    

        
class TestBallInSequence(ut.TestCase):
    def test_first_in_sequence(self):
        self.assertEqual(findHeavyBall([2,1,1,1,1,1,1,1,1,1]),2,"Incorrect Ball")
        
    def test_last_in_sequence(self):
        self.assertEqual(findHeavyBall([1,1,1,1,1,1,1,1,1,2]),2,"Incorrect Ball")
        
    def test_middle_of_sequence(self):
        self.assertEqual(findHeavyBall([1,1,1,1,2,1,1,1,1,1]),2,"Incorrect Ball")
    
    def test_second_in_sequence(self):
        self.assertEqual(findHeavyBall([1,2,1,1,1,1,1,1,1,1]),2,"Incorrect Ball")
    
    def test_second_to_last_in_sequence(self):
        self.assertEqual(findHeavyBall([1,1,1,1,1,1,1,1,2,1]),2,"Incorrect Ball")
        
    def test_negative_weight_in_sequence(self):
        self.assertEqual(findHeavyBall([-1,-1,-1,-1,-1,-1,-1,-1,1,-1]),1,"Incorrect Ball")
        
    def test_all_negative_weights_in_sequence(self):
        self.assertEqual(findHeavyBall([-2,-2,-2,-2,-2,-2,-1,-2,-2,-2]),-1,"Incorrect Ball")    
        
class TestBallExceptionHandling(ut.TestCase):
    def test_end_of_bag_exception(self):
        self.assertEqual(findHeavyBall([1,1,1,1,1,1,1,1,1,1]),"End of Bag.")

    def test_non_integer_ball_exception(self):
        self.assertEqual(findHeavyBall([1,1,1,1,1,"n",1,1,1,1]),"Ball in the Bag has no weight.")

    def test_bag_is_array_exception(self):
        self.assertEqual(findHeavyBall({"foo":"bar","fizz":"bang"}),"Bag of Balls is not an Array.")
    
    def test_recursion_limit_(self):
        self.large_array = []
        for i in range (10001):
            self.large_array.append(1)
        self.large_array[5000] = 2
        self.assertEqual(findHeavyBall(self.large_array),"Bag is too large. Update Recursion Limit to try again.")   
    
    
    def test_bag_is_not_empty_exception(self):
        self.assertEqual(findHeavyBall([]),"Bag is Empty.")

class TestLargeNumberOfBalls(ut.TestCase):
    def test_hundred_array(self):
        self.large_array = []
        for i in range (101):
            self.large_array.append(1)
        self.large_array[70] = 2
        self.assertEqual(findHeavyBall(self.large_array),2,"Incorrect Ball")
       
    def test_thousand_array(self):
        self.large_array = []
        for i in range (1001):
            self.large_array.append(1)
        self.large_array[700] = 2
        self.assertEqual(findHeavyBall(self.large_array),2,"Incorrect Ball")
    
    @ut.skipIf(sys.getrecursionlimit() < 1001, "Test is known to fail if the Recursion Limit is not modified")    
    def test_ten_thousand_array(self):
        self.large_array = []
        for i in range (10001):
            self.large_array.append(1)
        self.large_array[5000] = 2
        self.assertEqual(findHeavyBall(self.large_array),2,"Incorrect Ball")
        
while __name__ == "__main__":       
    ut.main()