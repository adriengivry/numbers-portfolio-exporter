import argparse

from numbers_parser import Document

from ticker_exporter.exporter import *

def main():
	parser = argparse.ArgumentParser()

	parser.add_argument(dest='input',
						help='input sheet (.numbers)')

	parser.add_argument(dest='config',
						help='base config file to build the final config file from')

	args = parser.parse_args()
	document = Document(args.input)
	export(document, args.config)
	print("Success! ~/.ticker.yaml updated!")

if __name__ == '__main__':
	main()
