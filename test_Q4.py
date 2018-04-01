import unittest
from Q4 import convert_flat_to_nested_list

class LinkedListTest(unittest.TestCase):

    def test_flat_to_nested(self):
        my_list = [None, 5, 10, 11, None, None, 2, 6]
        self.assertEqual(convert_flat_to_nested_list(my_list),[5, [10, None, None], [11, [2, None, None],[6, None, None]]])

    def test_flat_to_nested_short(self):
        my_list = [None, 1, 2, 3]
        self.assertEqual(convert_flat_to_nested_list(my_list),[1,[2,None,None],[3,None,None]])

    def test_flat_to_nested_long_branch(self):
        my_list = [None, 1, 2,None,3,None,None,None,4,None,None,None,None,None,None,None,None,5]
        self.assertEqual(convert_flat_to_nested_list(my_list),[1, [2, [3, [4, None, [5, None, None]], None], None], None])

    def test_flat_to_nested_switching(self):
        my_list = [None, 1, 2,3,4,None,None,5,None,6,None,None,None,None,7]
        self.assertEqual(convert_flat_to_nested_list(my_list),[1,[2,[4,None,[6,None,None]],None],[3,None,[5,[7,None,None],None]]])


if __name__ == '__main__':
    unittest.main()
