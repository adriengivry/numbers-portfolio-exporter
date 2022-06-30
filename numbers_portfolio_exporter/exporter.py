import copy
import csv
import yaml
import pathlib

from genericpath import exists
from os import makedirs
from numbers_parser import Document

class Exporter:
    # General
    DEFAULT_SHEET_INDEX = 0
    DEFAULT_TABLE_INDEX = 0
    DEFAULT_HEADER_ROWS = 1
    DEFAULT_VERBOSITY = False

    # Ticker
    DEFAULT_TICKER_INPUT_CONFIG_PATH = pathlib.Path.joinpath(pathlib.Path.home(), '.ticker.base.yaml')
    DEFAULT_TICKER_OUTPUT_CONFIG_PATH = pathlib.Path.joinpath(pathlib.Path.home(), '.ticker.yaml')
    DEFAULT_TICKER_ADD_ALL_ACCOUNT = True

    def __init__(self,
            filepath: str,
            sheetIndex: int = DEFAULT_SHEET_INDEX,
            tableIndex: int = DEFAULT_TABLE_INDEX,
            headerRows: int = DEFAULT_HEADER_ROWS,
            verbose: bool = DEFAULT_VERBOSITY):
        """Creates the exporter"""
        self.document = Document(filepath)
        self.sheet = self.document.sheets()[sheetIndex]
        self.table = self.sheet.tables()[tableIndex]
        self.rows = self.table.rows()
        self.headerRows = headerRows
        self.transactionsPerAccount = dict()
        self.verbose = verbose
        self.parse_transactions()

    def parse_transactions(self):
        self.transactionsPerAccount.clear()
        
        for i in range(self.headerRows, len(self.rows)):
            symbol  = self.rows[i][0].value
            price = self.rows[i][1].value
            quantity = self.rows[i][2].value
            date = self.rows[i][3].value.strftime("%Y%m%d")
            account = self.rows[i][4].value

            if not account in self.transactionsPerAccount:
                self.transactionsPerAccount[account] = list()

            self.transactionsPerAccount[account].append(dict({"symbol": symbol, "quantity": quantity, "price": price, "date": date}))

    def to_ticker_yaml(self,
            inputConfigPath: str = DEFAULT_TICKER_INPUT_CONFIG_PATH,
            outputConfigPath = DEFAULT_TICKER_OUTPUT_CONFIG_PATH,
            addAllAccount: bool = DEFAULT_TICKER_ADD_ALL_ACCOUNT):
        with open(inputConfigPath, 'r') as yamlfile:
            data = yaml.safe_load(yamlfile)

            # Creates the 'groups' entry
            if data['groups'] is None:
                data['groups'] = list()

            allEntries = list()

            for account, transactionList in self.transactionsPerAccount.items():
                accountEntries = list()

                for transaction in transactionList:
                    yamlEntry = {"symbol": transaction["symbol"], "quantity": transaction["quantity"], "unit_cost": transaction["price"]}

                    accountEntries.append(copy.deepcopy(yamlEntry))
                    allEntries.append(copy.deepcopy(yamlEntry))

                    if self.verbose:
                        print(yamlEntry)

                data['groups'].append({'name': account, 'holdings': accountEntries})
            
            if addAllAccount:
                data['groups'].append({'name': 'All', 'holdings': allEntries})

        if data:
            with open(outputConfigPath, 'w') as yamlfile:
                yaml.safe_dump(data, yamlfile, sort_keys=False)

    def to_yahoo_csv(self, outputFolder: str):
        if not exists(outputFolder):
            makedirs(outputFolder)

        for account, transactionList in self.transactionsPerAccount.items():
            with open(outputFolder + account + '.csv', 'w', newline='') as csvfile:
                filewriter = csv.writer(csvfile, delimiter=',')

                # Header Row
                filewriter.writerow(["Symbol", "Trade Date", "Purchase Price", "Quantity"])

                # Data Rows
                for transaction in transactionList:
                    csvEntry = [transaction["symbol"], transaction["date"], transaction["price"], transaction["quantity"]]
                    filewriter.writerow(csvEntry)

                    if self.verbose:
                        print(csvEntry)