from unittest import TestCase
from george import second_largest3 as second_largest



class Solution(TestCase):
    def test_input_example(self):
        mylist = [3,2,1,5,6,4]
        self.assertEqual(second_largest(mylist), 5)

    def test_duplicates(self):
        mylist = [1, 1, 2, 3, 4, -3, 8]
        self.assertEqual(second_largest(mylist), 4)

    def test_emptylist(self):
        self.assertEqual(second_largest([]), None)

    def test_withOneElement(self):
        self.assertEqual(second_largest([1]), None)


    def test_george_example(self):
        self.assertEqual(second_largest([5, 5, 2]), 2)

    def test_withNoneValue(self):
        with self.assertRaises(TypeError):
            second_largest(None)
        
    
