#-*-coding: utf-8 -*-

import unittest



class RomanTest(unittest.TestCase):
	
	def testI(self):
		self.assertEqual('I',number2roman(1))
		
	def testII(self):
		self.assertEqual('II',number2roman(2))

	
#==================================


def number2roman(number):
	return 'I'
	
	
if __name__ == '__main__':
	unittest.main()


