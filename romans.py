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
	def testX(self):
		self.assertEqual('X', number2roman(10))
		
		
		
#==================================


def number2roman(number):
	number = str(number)
	
	caracter = number[-1]
	
	if caracter == '1':
		return "I"
	elif caracter == "2":
		return "II"
	elif caracter == "3":
		return "III"
	elif caracter == "4":
		return "IV"
	elif caracter == "5":
		return "V"
	elif caracter == "6":
		return "VI"
	elif caracter == "7":
		return "VII"
	elif caracter == "8":
		return "VIII"
	elif caracter == "9":
		return "IX"
	elif caracter == "10":
		return "X"
	
	 	 
	
	
	
	
	
						
if __name__ == '__main__':
	unittest.main()


