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
	return parser.parse_args()


def read_decls(input_file):
	''' Read the program's declarations.

		@param 	input_file: File to read code from.
		@type 	input_file:	_io.TextIOWrapper
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


def main():
	global ST

	args = parse_arguments()
	file = open(args.INPUT_FILE, 'r')
	read_decls(file)

	quads = []
	for line in file: # Get all quadruples in source code
		line_args = line.split()

		L = []
		if ':' in line_args[0]: # Collect Quadruple labels
			L = [int(x[1:]) for x in line_args[0].split(':') if x != '']
			del line_args[0]

		if len(line_args) != 0: # Non empty quadruples
			if 'if' in line_args[0] or 'goto' in line_args[0]: # Branch or Cond
				continue
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
				else:
					op = line_args[3]

					if op == '[':
						op = '=[]'

					op1 = line_args[2]
					op2 = line_args[4]


				newQuad = Quadruple(dst, op1, op2, op)
				quads.append(newQuad)

		for label in L: # Each label points to their proper quadruple
			labels[label] = newQuad

	file.close()


################################################################################


main()
