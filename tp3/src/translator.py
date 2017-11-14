#!/usr/bin/env python3

'''
translator.py: 3 address code -> TAM translator.
@author: Hugo Araujo de Sousa [2013007463]
@email: hugosousa@dcc.ufmg.br
@DCC053 - Compiladores I - UFMG
'''


import argparse as ap
from quadruple import Quadruple


# Global variables.

input_file = None
output_file = None

# Sizes (in 2B words) of the grammar types.
TSIZES = {'int': 2, 'float': 4, 'char': 1, 'bool': 1}
MAX_SIZE = TSIZES['float']

# Stack top
ST = 0

# Address, on the stack, of the variables.
address = {}

# Dictionary which returns the Quadruple by label.
labels = {}


################################################################################


def parse_arguments():
	''' Add command line arguments to the program.

		@return:	Command line arguments.
		@rtype:		argparse.Namespace.
		'''

	parser = ap.ArgumentParser()
	parser.add_argument('INPUT_FILE', type=str, help='Name of input file')
	parser.add_argument('OUTPUT_FILE', type=str, help='Name of output file')
	return parser.parse_args()


def read_decls():
	''' Read the program's declarations.
		'''

	global ST

	while True:
		line = input_file.readline()

		if len(line) <= 2:
			break
		else:
			line = line.replace('[', '')
			line = line.replace(']', '')
			args = line.split()

			if len(args) < 3: # Simple variable
				if args[1] not in address:
					size = TSIZES[args[0]]
					address[args[1]] = ST
					ST += size
			else: # Array
				if args[2] not in address:
					size = TSIZES[args[1]] * int(args[0])
					address[args[2]] = ST
					ST += size


def build_quadruples():
	''' Build quadruples from the isntruction in the source code.

		@return 	quads: 	Quadruples built.
		@rtype 		quads:	List of Quadruple.
		'''

	global ST

	quads = []
	for line in input_file: # Get all quadruples in source code
		newQuad = None
		line_args = line.split()

		L = []
		if ':' in line_args[0]: # Collect Quadruple labels
			L = [int(x[1:]) for x in line_args[0].split(':') if x != '']
			del line_args[0]

		if len(line_args) != 0: # Non empty quadruples
			if 'if' in line_args[0]: # Conditional
				op = line_args[0]
				cond = line_args[1:4]
				branch = int(line_args[-1][1:])
				newQuad = Quadruple(None, cond, None, op, branch)
			elif 'goto' == line_args[0]: # Unconditional jump
				branch = int(line_args[1][1:])
				newQuad = Quadruple(None, None, None, line_args[0], branch)
			else: # Operation
				dst = line_args[0]

				if dst not in address: # Allocate memory for temporaries
					address[dst] = ST
					ST += MAX_SIZE

				# Get operator and operands
				if line_args[1] == '[': # Array indexing l-value
					op = '[]='
					op1 = line_args[2]
					op2 = line_args[5]

					newQuad = Quadruple(dst, op1, op2, op)
				else:
					if len(line_args) == 3: # Simple copy assignments
						op1 = line_args[2]
						newQuad = Quadruple(dst, op1, None, None)
					elif len(line_args) == 5: # Arithmetic
						op = line_args[3]
						op1 = line_args[2]
						op2 = line_args[4]

						newQuad = Quadruple(dst, op1, op2, op)
					elif len(line_args) == 6: # Array indexing r-value
						op = '=[]'
						op1 = line_args[2]
						newQuad = Quadruple(dst, op1, None, op)
					else: # Unary
						op = line_args[2]
						op2 = line_args[3]

						newQuad = Quadruple(dst, None, op2, op)

		if newQuad:
			quads.append(newQuad)

		for label in L: # Each label points to their proper quadruple
			labels[label] = newQuad

	return quads


def translate(quads):
	''' Translate quadruples to TAM code.

		Types of quadruples:
			1. Conditional jump.
			2. Unconditional jump.
			3. Array indexing l-value assignment.
			4. Array indexing r-value assignment.
			5. Simple variable copy assignments.
			6. Arithmetic assignment.
			7. Unary assignment.
		
		@param 	quads:	Quadruples to translate.
		@type 	quads:	List of Quadruple.
		'''

	CT = 0 # Code stack top
	quads[0].address = 0

	for quad in quads:
		quad_type = quad.type

		if quad_type == 1:
			pass
		elif quad_type == 2:
			pass
		elif quad_type == 3:
			pass
		elif quad_type == 4:
			pass
		elif quad_type == 5:
			pass
		elif quad_type == 6:
			pass
		elif quad_type == 7:
			pass


def main():

	global input_file, output_file

	args = parse_arguments()

	input_file = open(args.INPUT_FILE, 'r')
	output_file = open(args.OUTPUT_FILE, 'w')

	read_decls()
	quads = build_quadruples()

	input_file.close()
	output_file.close()


################################################################################


main()
