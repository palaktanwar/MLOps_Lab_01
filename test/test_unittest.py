import sys
import os
import unittest

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(project_root)

from src.maths import findOddEven, findfibbonaci

class Test_findOddEvenfibbonaci(unittest.TestCase):
    def test_oddeven(self):
         self.assertEqual(findOddEven(3), "Odd")
         self.assertEqual(findOddEven(13), "Odd")
         self.assertEqual(findOddEven(132), "Even")
         self.assertEqual(findOddEven(130), "Even")
    

    def test_fibbonaci(self):
            self.assertEqual(findfibbonaci(8), 21)
            self.assertEqual(findfibbonaci(3), 2)
            self.assertEqual(findfibbonaci(0), 0)
            self.assertEqual(findfibbonaci(5), 5)

if __name__ == '__main__':
    unittest.main()
         