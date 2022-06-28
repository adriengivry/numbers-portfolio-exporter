from numbers_parser import Document
import csv

def export(input: Document, output: str):
    sheets = input.sheets()
    tables = sheets[0].tables()
    rows = tables[0].rows()
    
    with open(output, 'w', newline='') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=',')
        filewriter.writerow(["Symbol", "Trade Date", "Purchase Price", "Quantity"])

        for i in range (2, len(rows)):
            symbol = rows[i][0].value
            price = rows[i][1].value
            shares = rows[i][2].value
            date = rows[i][3].value.strftime("%Y%m%d")
            csvEntry = [symbol, date, price, shares]
            print(csvEntry)
            filewriter.writerow(csvEntry)
