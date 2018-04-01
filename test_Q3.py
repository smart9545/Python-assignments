import unittest
from Q3 import hashing

class LinkedListTest(unittest.TestCase):

    def test_no_collisions_linear(self):
        values = [0,1,2,3,4,5,6,7,8,9,10]
        self.assertEqual(hashing(values,11,'linear',None),[0,1,2,3,4,5,6,7,8,9,10])

    def test_no_collisions_quadratic(self):
        values = [0,1,2,3,4,5,6,7,8,9,10]
        self.assertEqual(hashing(values,11,'quadratic',None),[0,1,2,3,4,5,6,7,8,9,10])

    def test_no_collisions_double(self):
        values = [0,1,2,3,4,5,6,7,8,9,10]
        self.assertEqual(hashing(values,11,'double',5),[0,1,2,3,4,5,6,7,8,9,10])

    def test_collision_linear_wrap(self):
        values = [0,1,1,3,15,5,4,22]
        self.assertEqual(hashing(values,11,'linear',None),[0,1,1,3,15,5,4,22,None,None,None])

    def test_collision_linear_no_wrap(self):
        values = [0,3,7,10,14,25]
        self.assertEqual(hashing(values,11,'linear',None),[0,None,None,3,14,25,None,7,None,None,10])

    def test_collision_quadratic_wrap(self):
        values = [1,4,6,15,18,19,24,27]
        self.assertEqual(hashing(values,13,'quadratic',None),[None,1,15,None,4,18,6,19,None,None,27,24,None])

    def test_collision_quadratic_no_wrap(self):
        values = [0,1,2,4,5,6,19,14,24]
        self.assertEqual(hashing(values,13,'quadratic',None),[0,1,2,None,4,5,6,19,None,None,14,24,None])

    def test_collision_double_no_wrap(self):
        values = [0,4,12,28,15,26]
        self.assertEqual(hashing(values,13,'double',5),[0,None,28,None,4,None,None,15,26,None,None,None,12])
        
    def test_collision_double_wrap(self):
        values = [0,4,12,28,15,26,25,9]
        self.assertEqual(hashing(values,13,'double',5),[0,None,28,None,4,None,None,15,26,25,9,None,12])

if __name__ == '__main__':
    unittest.main()
