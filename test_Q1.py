import unittest
import time
from Q1 import LinkedList


class LinkedListTest(unittest.TestCase):

    def test_append_empty(self):
        my_list= LinkedList()
        my_list.append(4)
        my_list.append(5)
        my_list.append(6)
        self.assertEqual(my_list.to_list(),[4,5,6])

    def test_append_after_add(self):
        my_list= LinkedList()
        my_list.add(5)
        my_list.add(4)
        my_list.append(6)
        my_list.append(7)
        self.assertEqual(my_list.to_list(),[4,5,6,7])

    def test_remove_from_end_then_append(self):
        my_list= LinkedList()
        my_list.add(6)
        my_list.add(5)
        my_list.add(4)
        my_list.add(3)
        my_list.add(2)
        my_list.remove(6)
        my_list.append(7)
        self.assertEqual(my_list.to_list(),[2,3,4,5,7])

    def test_remove_from_start_then_append(self):
        my_list= LinkedList()
        my_list.add(6)
        my_list.add(5)
        my_list.add(4)
        my_list.add(3)
        my_list.add(2)
        my_list.remove(2)
        my_list.append(7)
        self.assertEqual(my_list.to_list(),[3,4,5,6,7])

    def test_remove_to_empty_then_append(self):
        my_list= LinkedList()
        my_list.add(6)
        my_list.add(5)
        my_list.remove(6)
        my_list.remove(5)
        my_list.append(8)
        my_list.append(9)
        self.assertEqual(my_list.to_list(),[8,9])

    def test_append_empty_size(self):
        my_list= LinkedList()
        my_list.append(4)
        my_list.append(5)
        my_list.append(6)
        self.assertEqual(my_list.size(),3)

    def test_append_after_add(self):
        my_list= LinkedList()
        my_list.add(5)
        my_list.add(4)
        my_list.append(6)
        my_list.append(7)
        self.assertEqual(my_list.size(),4)

    def test_remove_from_end_then_append(self):
        my_list= LinkedList()
        my_list.add(6)
        my_list.add(5)
        my_list.add(4)
        my_list.add(3)
        my_list.add(2)
        my_list.remove(6)
        my_list.append(7)
        self.assertEqual(my_list.size(),5)

    def test_remove_from_start_then_append(self):
        my_list= LinkedList()
        my_list.add(6)
        my_list.add(5)
        my_list.add(4)
        my_list.add(3)
        my_list.add(2)
        my_list.remove(2)
        my_list.append(7)
        self.assertEqual(my_list.size(),5)

    def test_remove_to_empty_then_append(self):
        my_list= LinkedList()
        my_list.add(6)
        my_list.add(5)
        my_list.remove(6)
        my_list.remove(5)
        my_list.append(8)
        my_list.append(9)
        self.assertEqual(my_list.size(),2)

    def test_O1_append(self):
        my_list = LinkedList()
        time_start = time.time()
        for i in range(0,1000):
            my_list.append(i)
        time_end = time.time()
        try:
            self.assertTrue(time_end - time_start <0.05)
        except AssertionError as e:
            print("Failed Test: Implemented as O(1) append")

    def test_O1_size(self):
        my_list = LinkedList()
        for i in range(0,1000):
            my_list.append(i)
        time_start = time.time()
        for i in range(0,1000):
            my_list.size()
        time_end = time.time()
        try:
            self.assertTrue(time_end - time_start <0.05)
        except AssertionError as e:
            print("Failed Test: Implemented as O(1) size")

if __name__ == '__main__':
    unittest.main()
