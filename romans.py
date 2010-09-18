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

		
#==================================


def number2roman(number):
	
	milhar = number / 1000
	
	if milhar:
		number = number - milhar * 1000
		milhar = milhar * 'M'
	else:
		milhar = ''
	
	centena = number / 100
	number = number - centena * 100
	if centena == 5:
		centena = 'D'
	elif centena == 4:
		centena = 'CD'
	elif centena == 9:
		centena = 'CM'
	elif centena > 5 and centena < 9:
		centena = 'D' + (centena - 5) * 'C'
	elif centena >= 1 and centena < 4:
		centena = 'C' * centena
	else:
		centena = ''
		
	dezena = number / 10	
	number = number - dezena * 10
	if dezena == 5:
		dezena = 'L'
	elif dezena == 4:
		dezena = 'XL'
	elif dezena == 9:
		dezena = 'XC'
	elif dezena > 5 and dezena < 9:
		dezena = 'L' + (dezena - 5) * 'X'
	elif dezena >= 1 and dezena < 4:
		dezena = 'X' * dezena
	else:
		dezena = ''
		
	unidade = number
	if unidade == 5:
		unidade = 'V'
	elif unidade == 4:
		unidade = 'IV'
	elif unidade == 9:
		unidade = 'IX'
	elif unidade > 5 and unidade < 9:
		unidade = 'V' + (unidade - 5) * 'I'
	elif unidade >= 1 and unidade < 4:
		unidade = 'I' * unidade
	else:
		unidade = ''

	

		
		
	
	final = milhar + centena + dezena + unidade		
	return final	
	
	
						
if __name__ == '__main__':
	unittest.main()


