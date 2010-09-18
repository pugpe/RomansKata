#-*-coding: utf-8 -*-

import unittest



class RomanTest(unittest.TestCase):
	
	def testI(self):
		self.assertEqual('I',number2roman(1))
		
	def testII(self):
		self.assertEqual('II',number2roman(2))
	def testIII(self):
		self.assertEqual('III',number2roman(3))
	def testIV(self):
		self.assertEqual('IV', number2roman(4))
	def testV(self):
		self.assertEqual('V', number2roman(5))
		
		
#==================================


def number2roman(number):
	if number % 5 == 0:
		return 'V'
	if number % 5 == 1:
		return 'I'
	if number % 5 == 2:
		return 'II'	
	if number % 5 == 3:
		return 'III'
	if number % 5 == 4:
		return 'IV'					
if __name__ == '__main__':
	unittest.main()


