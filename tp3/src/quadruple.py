#!/usr/bin/env python3

'''
quadruple.py: Represents a Quadruple.
@author: Hugo Araujo de Sousa [2013007463]
@email: hugosousa@dcc.ufmg.br
@DCC053 - Compiladores I - UFMG
'''


class Quadruple():

	def __init__(self, dst, op1, op2, operator, branch=None):
		''' Initialize the Quadruple.

			@param 	dst:	Destination variable (in case of assignments).
			@type	dst:	String.

			@param 	op1:	First operand.
			@param 	op1:	String.

			@param 	op2':	Second operand.
			@param 	op2':	String.
			
			@param	operator:	Operator.
			@type 	operator:	String.

			@param 	branch:		In case of branches, the label to branch to.
			@type 	branch:		Integer.
			'''

		self.dst = dst
		self.op1 = op1
		self.op2 = op2
		self.operator = operator
		self.branch = branch

	def __str__(self):
		''' Return a string representation of the Quadruple. '''

		return 	self.operator + ', ' + self.dst + ', ' + self.op1 + ', ' + \
				self.op2 + ', ' + str(self.branch)