#-*-coding: utf-8 -*-

import unittest



class RomanTest(unittest.TestCase):


	def test0ShouldReturnNothing(self):
		self.assertEqual('', number2roman(0))
		
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
		
	def testXX(self):
		self.assertEqual("XX", number2roman(20))
	def testXV(self):
		self.assertEqual('XV', number2roman(15))
		
	def testXVI(self):
		self.assertEqual('XVI', number2roman(16))
		
	def testLXIV(self):
		self.assertEqual('LXIV', number2roman(64))
		
	def testMCMXC(self):
		self.assertEqual('MCMXC', number2roman(1990))

	def testMXL(self):
		self.assertEqual('MXL', number2roman(1040))

	def testMCMXCIX(self):
		self.assertEqual('MCMXCIX', number2roman(1999))	
			
	def testMMXII(self):
		self.assertEqual('MMXII', number2roman(2012))

	def testMCDXLIV(self):
		self.assertEqual('MCDXLIV', number2roman(1444))	
		
	def testMMMCMXCIX(self):
		self.assertEqual('MMMCMXCIX', number2roman(3999))
		
	def testC(self):
		self.assertEqual('C', number2roman(100))
	
	def testL(self):
		self.assertEqual('L', number2roman(50))				
		
#def test(self):
#	self.assertEqual('', number2roman())

	

		
#==================================


def number2roman(number):
	
	romanos = {
		100: 'C',
		200: 'CC',
		300: 'CCC',
		400: 'CD',
		500: 'D',
		600: 'DC',
		700: 'DCC',
		800: 'DCCC',
		900: 'CM',
		10: 'X',
		20: 'XX',
		30: 'XXX', 
		40: 'XL', 
		50: 'L',
		60: 'LX',
		70: 'LXX',
		80: 'LXXX',
		90: 'XC',
		1: 'I',
		2: 'II',
		3: 'III',
		4: 'IV',
		5: 'V',
		6: 'VI',
		7: 'VII',
		8: 'VIII',
		9: 'IX',
		0: ''
	}
	
	milhar = number / 1000
	number = number - milhar * 1000
	final = "M" * milhar
	
	for temp in [100, 10, 1]:
		centena = number / temp
		number = number - centena * (temp)
		centena = romanos[centena * temp]
		
		final += centena
			
	return final	
				
if __name__ == '__main__':
	unittest.main()
