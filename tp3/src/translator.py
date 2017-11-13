#!/usr/bin/env python3

'''
translator.py: 3 address code -> TAM translator.
@author: Hugo Araujo de Sousa [2013007463]
@email: hugosousa@dcc.ufmg.br
@DCC053 - Compiladores I - UFMG
'''


import argparse as ap


# Global variables.

TYPES = ['int', 'float', 'char', 'bool'] # Types in grammar.
id_sizes = {} # Size in (2B words) of all ids


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
		@type 	input_file:	_io.TextIOWrapper'
		'''

	for line in input_file:
		if line == '':
			break

		else:


def main():
	args = parse_arguments()
	file = open(args.INPUT_FILE, 'r')
	print(type(file))

	file.close()


main()
