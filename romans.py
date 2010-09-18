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
	
	final =""
	
	
	caracter = number[-1]
	
	if caracter == '1':
		 final = "I"
	elif caracter == "2":
		final = "II"
	elif caracter == "3":
		final ="III"
	elif caracter == "4":
		final ="IV"
	elif caracter == "5":
		final ="V"
	elif caracter == "6":
		final ="VI"
	elif caracter == "7":
		final ="VII"
	elif caracter == "8":
		final ="VIII"
	elif caracter == "9":
		final ="IX"	
	
	if len(number) > 1:
		caracter2 = number[-2]
	
		if caracter == '1':
			final = "X" + final
		elif caracter == "2":
			final = "XX" + final
		elif caracter == "3":
			final = "XX" + final
		elif caracter == "4":
			final = "XL" + final
		elif caracter == "5":
			final = "L" + final
		elif caracter == "6":
			final = "LX" + final
		elif caracter == "7":
			final = "LXX" + final
		elif caracter == "8":
			final = "LXXX" + final
		elif caracter == "9":
			final = "XC" + final
			
	return final	
	
	
						
if __name__ == '__main__':
	unittest.main()


