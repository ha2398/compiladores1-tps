#!/usr/bin/env python3

'''
compiler.py: SmallL to TAM compiler. 
@author: Hugo Araujo de Sousa [2013007463]
@email: hugosousa@dcc.ufmg.br
@DCC053 - Compiladores I - UFMG
'''


import argparse as ap
import subprocess as sp
import os


# Global variables
BACKEND_FOLDER = 'back-end'
FRONTEND_FOLDER = 'front-end'


def parse_arguments():
	''' Add command line arguments to the program.

		@return:	Command line arguments.
		@rtype:		argparse.Namespace.
		'''

	parser = ap.ArgumentParser()
	parser.add_argument('INPUT_FILE', type=str, help='Name of input file')
	return parser.parse_args()


def frontend(input_file):
	''' The front-end of the compiler.

		@param 	input_file:	Input source code file.
		@type 	input_file: File.
		'''

	os.chdir('src/' + FRONTEND_FOLDER)
	sp.call(['make'])
	sp.call(['java', 'main.Main'], stdin=input_file)
	os.chdir('../../')


def backend():
	''' The back-end of the compiler. '''

	os.chdir('src/' + BACKEND_FOLDER)
	sp.call(['./translator.py', '../' + FRONTEND_FOLDER + '/code.out',
		'../../out.tam'])
	sp.call(['rm', '-rf', '../' + FRONTEND_FOLDER + '/code.out'])


def main():

	args = parse_arguments()
	input_file = open(args.INPUT_FILE, 'r')
	frontend(input_file)
	input_file.close()
	backend()


main()