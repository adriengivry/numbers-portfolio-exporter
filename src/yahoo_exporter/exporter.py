from numbers_parser import Document
import csv

def export(input: Document, outputFolder: str):
    sheets = input.sheets()
    tables = sheets[0].tables()
    rows = tables[0].rows()

    transactionsPerAccount = dict()

    for i in range(2, len(rows)):
        account = rows[i][4].value
        if account not in transactionsPerAccount:
            transactionsPerAccount[account] = list()

    for i in range (2, len(rows)):
            symbol = rows[i][0].value
            price = rows[i][1].value
            shares = rows[i][2].value
            date = rows[i][3].value.strftime("%Y%m%d")
            account = rows[i][4].value
            transactionsPerAccount[account].append(dict({"symbol": symbol, "quantity": shares, "unit_cost": price, "date": date}))
    
    for account, transactionList in transactionsPerAccount.items():
        with open(outputFolder + account + '.csv', 'w', newline='') as csvfile:
            filewriter = csv.writer(csvfile, delimiter=',')
            filewriter.writerow(["Symbol", "Trade Date", "Purchase Price", "Quantity"])

            for transaction in transactionList:
                symbol = transaction["symbol"]
                price = transaction["unit_cost"]
                shares = transaction["quantity"]
                date = transaction["date"]
                csvEntry = [symbol, date, price, shares]
                print(csvEntry)
                filewriter.writerow(csvEntry)
