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

			Types of quadruples:
				0: Unknown type.
				1. Conditional jump.
				2. Unconditional jump.
				3. Array indexing l-value assignment.
				4. Array indexing r-value assignment.
				5. Simple variable copy assignments.
				6. Arithmetic assignment.
				7. Unary assignment.

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

		self.address = None # Address in TAM code stack.

		''' List with strings that represent the quadruple's tam instructions.
			'''
		self.tam_code = []
		self.type = self.get_type()

	def get_type(self):
		''' Get quadruple's type.

			@return: 	Quadruple's type.
			@rtype:		Integer.
			'''

		if self.operator != None and 'if' in self.operator:
			return 1
		elif self.operator == 'goto':
			return 2
		elif self.operator == '[]=':
			return 3
		elif self.operator == '=[]':
			return 4
		elif self.operator == None:
			return 5
		elif self.operator in ['+', '-', '*', '/']:
			return 6
		else:
			return 7
 
	def __str__(self):
		''' Return a string representation of the Quadruple. '''

		string = ''

		if self.type:
			string += 'Type: ' + str(self.type) + ' '

		if self.dst:
			string += str(self.dst) + ' '

		if self.op1:
			string += str(self.op1) + ' '

		if self.operator:
			string += str(self.operator) + ' '

		if self.op2:
			string += str(self.op2) + ' '

		if self.branch:
			string += str(self.branch)

		return string