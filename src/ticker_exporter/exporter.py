from numbers_parser import Document
import yaml
from pathlib import Path

def export(input: Document, config: str):
    sheets = input.sheets()
    tables = sheets[0].tables()
    rows = tables[0].rows()

    accounts = list()

    accounts.append('All')

    for i in range (2, len(rows)):
        account = rows[i][4].value
        if account not in accounts:
            accounts.append(account)

    # Update Ticker YAML file
    tickerBaseConfigPath = config
    tickerConfigPath = Path.joinpath(Path.home(), '.ticker.yaml')

    with open(tickerBaseConfigPath, 'r') as yamlfile:
        data = yaml.safe_load(yamlfile)

        groupCount = 0

        if data['groups'] is None:
            data['groups'] = list()
        else:
            groupCount = len(data['groups'])

        for account in accounts:
            data['groups'].append({'name': account, 'holdings': list()})

        for i in range (2, len(rows)):
            symbol = rows[i][0].value
            price = rows[i][1].value
            shares = rows[i][2].value
            date = rows[i][3].value.strftime("%Y%m%d")
            account = rows[i][4].value
            data['groups'][accounts.index(account) + groupCount]['holdings'].append(dict({"symbol": symbol, "quantity": shares, "unit_cost": price}))
            data['groups'][accounts.index('All') + groupCount]['holdings'].append(dict({"symbol": symbol, "quantity": shares, "unit_cost": price}))

    if data:
        with open(tickerConfigPath, 'w') as yamlfile:
            yaml.safe_dump(data, yamlfile, sort_keys=False)