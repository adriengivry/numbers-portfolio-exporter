import argparse
from numbers_portfolio_exporter import Exporter

def add_generic_arguments(parser: argparse.ArgumentParser):
	parser.add_argument(dest='filepath', help='path to the input spreadsheet (.numbers)')
	parser.add_argument('-v', '--verbose', dest='verbose', action='store_true', required=False, default=Exporter.DEFAULT_VERBOSITY, help='provides additional details during exports')
	parser.add_argument('-cs', '--currency-split', dest='currency_split', action='store_true', required=False, default=Exporter.DEFAULT_CURRENCY_SPLIT, help='determines if holdings in the same account with different currencies should be separated')
	parser.add_argument('-s', '--sheet-index', dest='sheet_index', type=int, required=False, default=Exporter.DEFAULT_SHEET_INDEX, help='determines the sheet to target in the .numbers file')
	parser.add_argument('-t', '--table-index', dest='table_index', type=int, required=False, default=Exporter.DEFAULT_TABLE_INDEX, help='determines the table to target in the current sheet')
	parser.add_argument('-hr', '--header-rows', dest='header_rows', type=int, required=False, default=Exporter.DEFAULT_HEADER_ROWS, help='determines the size of the header in the transaction table')

def create_parser() -> argparse.ArgumentParser:
	parser = argparse.ArgumentParser()
	add_generic_arguments(parser)
	return parser

def create_exporter(args):
	return Exporter(
		filepath = args.filepath,
		sheetIndex = args.sheet_index,
		tableIndex = args.table_index,
		headerRows = args.header_rows,
		currencySplit = args.currency_split,
		verbose = args.verbose)

def numbers_to_yahoo_csv_command():
	parser = create_parser()
	parser.add_argument(dest='output', help='destination folder for output files (one CSV will be generated per account)')
	args = parser.parse_args()
	exporter = create_exporter(args)
	exporter.to_yahoo_csv(args.output)

def numbers_to_ticker_yaml_command():
	parser = argparse.ArgumentParser()
	add_generic_arguments(parser)
	parser.add_argument('-i', '--input', dest='input', required=False, default=Exporter.DEFAULT_TICKER_INPUT_CONFIG_PATH, help='input YAML config file to build the output config file from')
	parser.add_argument('-o', '--output', dest='output', required=False, default=Exporter.DEFAULT_TICKER_OUTPUT_CONFIG_PATH, help='output YAML config file')
	parser.add_argument('-a', '--add-all-account', dest='add_all_account', action='store_true', required=False, default=Exporter.DEFAULT_TICKER_ADD_ALL_ACCOUNT, help='create an additional account summarizing all the other account transactions')
	args = parser.parse_args()
	exporter = create_exporter(args)
	exporter.to_ticker_yaml(
		inputConfigPath = args.input,
		outputConfigPath = args.output,
		addAllAccount = args.add_all_account)
