#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
	"""Class for testing 6-max_integer"""

	def setUp(self):
		self.max_at_middle = [3,6,88,2,45]
		self.empty_list = []
		self.negative_list = [-3,-5,-9,-2]
		self.list_of_strings = ["Mike", "Bran", "Jadon"]
		self.string_as_list = "jamiez"
		self.max_at_end = [3,4,6,7,9]
		self.max_at_beginning = [8,4,2]
		self.floats = [3.5,5.43,7.5]
		self.floats_and_int = [4,5.6,3.26,8,50]
		self.one_element = [6]

	def test_maxAtEnd(self):
		"""Tests when max is at end of list"""
		self.assertEqual(max_integer(self.max_at_end), 9)

	def test_maxAtBeginning(self):
		"""Tests when max is at beginning of list"""
		self.assertEqual(max_integer(self.max_at_beginning), 8)
				   
	def test_floats(self):
		"""Tests with lists of only floats"""
		self.assertEqual(max_integer(self.floats), 7.5)
	
	def test_floatsAndInt(self):
		"""Tests with list of floats and int"""
		self.assertEqual(max_integer(self.floats_and_int), 50)

	def test_oneElement(self):
		"""Tests with list of only one element"""
		self.assertEqual(max_integer(self.one_element), 6)

	def test_emptyList(self):
		"""Tests with empty list"""
		self.assertEqual(max_integer(self.empty_list), None)
	
	def test_maxAtMiddle(self):
		"""Tests when max is at middle of list"""
		self.assertEqual(max_integer(self.max_at_middle), 88)

	def test_negativeList(self):
		"""Tests with list of negative integers"""
		self.assertEqual(max_integer(self.negative_list), -2)
	
	def test_listOfStrings(self):
		"""Tests with string"""
		self.assertEqual(max_integer(self.list_of_strings), "Mike")

	def test_stringAsList(self):
		"""Tests with list of strings"""
		self.assertEqual(max_integer(self.string_as_list), 'z')

if __name__ == "__main__":
	unittest.main()
