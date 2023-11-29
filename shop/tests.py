from django.test import TestCase
import unittest
class Test(TestCase):
    def test_1(self):
        self.assertEqual(1, 1)




class DoszhanTestCase(unittest.TestCase):
    def test_numbers(self):
        self.assertEqual(3 + 4, 7)
        self.assertEqual(3 + 4, 7)

if __name__ == '__main__':
    unittest.main()




class MyDoszhan2TestCase(unittest.TestCase):
    def test_strings(self):
        self.assertEqual("hello" + " " + "world", "hello world")
        self.assertEqual("hello" + " " + "world", "hello world")

if __name__ == '__main__':
    unittest.main()



