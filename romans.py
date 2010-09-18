#-*-coding: utf-8 -*-

import unittest



class RomanTest(unittest.TestCase):
	
	def testI(self):
		self.assertEqual('I',number2roman(1))

	
#==================================




if __name__ == '__main__':
	unittest.main()


