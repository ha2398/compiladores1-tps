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

# Code stack top
CT = 0

# Address, on the stack, of the variables.
addresses = {}

# Types of the variables.
types = {}

# Dictionary which returns the Quadruple by label.
labels = {}

# Instruction format
INSTR = '{}\t{}\t{}\t{}\t; {}\n'

# Instruction buffer
INSTR_BUFFER = []

# Backpatching dependency dictionary. Key -> Index of instruction on
# INSTR_BUFFER. Value -> label on which the instruction indexed
# depends.
BACKPATCH_DEP = {}


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


def add_instr(instr):
	''' Print instruction to output file.

		@param 	instr: 	Instruction to print.
		@type 	instr:	String.
		'''

	global CT

	INSTR_BUFFER.append(instr)
	CT += 1

def read_decls():
	''' Read the program's declarations.
		'''

	global ST, CT

	while True:
		line = input_file.readline()

		if len(line) <= 2:
			break
		else:
			line = line.replace('[', '')
			line = line.replace(']', '')
			args = line.split()

			if len(args) < 3: # Simple variable
				if args[1] not in addresses:
					size = TSIZES[args[0]]
					addresses[args[1]] = ST
					ST += size
					types[args[1]] = args[0]
			else: # Array
				if args[2] not in addresses:
					size = TSIZES[args[1]] * int(args[0])
					addresses[args[2]] = ST
					ST += size
					types[args[2]] = args[1]

		add_instr(INSTR.format(10, 0, 0, size, 'PUSH ' + str(size)))



def build_quadruples():
	''' Build quadruples from the isntruction in the source code.

		@return 	quads: 	Quadruples built.
		@rtype 		quads:	List of Quadruple.
		'''

	global CT, ST

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

				if dst not in addresses: # Allocate memory for temporaries
					addresses[dst] = ST
					ST += MAX_SIZE
					types[dst] = 'float'

					add_instr(INSTR.format(10, 0, 0, MAX_SIZE,
						'PUSH ' + str(MAX_SIZE)))

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

	for quad in quads:
		quad.addresses = CT
		quad_type = quad.type

		if quad_type == 1: # Conditional jump.
			pass
		elif quad_type == 2: # Unconditional jump.
			add_instr(INSTR.format(12, 0, 0, '{}', 'JUMP {}[CB]'))
		elif quad_type == 3: # Array indexing l-value assignment.
			pass
		elif quad_type == 4: # Array indexing r-value assignment.
			pass
		elif quad_type == 5: # Simple variable copy assignments.
			if quad.op1 in addresses: # Operand is variable
				addr_op1 = addresses[quad.op1]
				addr_dst = addresses[quad.dst]
				op1_size = TSIZES[types[quad.op1]]
				dst_size = TSIZES[types[quad.dst]]

				add_instr(INSTR.format(1, 4, 0, addr_op1,
					'LOADA ' + str(addr_op1) + '[SB]'))
				add_instr(INSTR.format(2, 0, op1_size, 0,
					'LOADI(' + str(op1_size) + ')'))

				add_instr(INSTR.format(1, 4, 0, addr_dst,
					'LOADA ' + str(addr_dst) + '[SB]'))
				add_instr(INSTR.format(5, 0, dst_size, 0,
					'STOREI(' + str(dst_size) + ')'))
			else: # Operand is not variable
				# Need to handle floating point literals.
				literal = int(quad.op1)

				add_instr(INSTR.format(3, 0, 0, literal,
					'LOADL ' + str(literal)))
		elif quad_type == 6: # Arithmetic assignment.
			pass
		elif quad_type == 7: # Unary assignment.
			pass

	add_instr(INSTR.format(15, 0, 0, 0, 'HALT'))


def finish():
	''' Finishes translation. '''

	input_file.close()

	for instruction in INSTR_BUFFER:
		output_file.write(instruction)

	output_file.close()


def main():

	global input_file, output_file

	args = parse_arguments()

	input_file = open(args.INPUT_FILE, 'r')
	output_file = open(args.OUTPUT_FILE, 'w')

	read_decls()
	quads = build_quadruples()

	for quad in quads:
		print(quad)

	translate(quads)

	finish()


################################################################################


main()
