from number_machine import reverse_number, add_nums, add_one
import unittest

class TestMy(unittest.TestCase):
      def test_main(self):
          self.assertEqual(reverse_number(12345), 54321)
          self.assertEqual(reverse_number(00000), 0)

      def test_add_nums(self):
          self.assertEqual(add_nums(12345), 15)
          self.assertEqual(add_nums(45674), 26)

      def test_add_one(self):
          self.assertEqual(add_one(12345), 23456)
          self.assertEqual(add_one(00000), 11111)
