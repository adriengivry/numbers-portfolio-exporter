import argparse

from numbers_parser import Document

from yahoo_exporter.exporter import *

def main():
	parser = argparse.ArgumentParser()

	parser.add_argument(dest='input',
						help='input sheet (.numbers)')

	parser.add_argument(dest='output',
						help='destination of the output file')

	args = parser.parse_args()
	document = Document(args.input)
	export(document, args.output)
	print("Success! %s created")

if __name__ == '__main__':
	main()
