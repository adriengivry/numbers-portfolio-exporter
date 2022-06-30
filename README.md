# Numbers Portfolio Exporter
Package to export a stock portfolio from [Apple Numbers](https://www.apple.com/numbers/) to [Yahoo Finance](https://finance.yahoo.com) (CSV) and [Ticker](https://github.com/achannarasappa/ticker) (YAML)

## Installation
```properties
pip install -r requirements.txt
pip install -e .
```

## Python Example
```python
from numbers_portfolio_exporter import Exporter

exporter = Exporter('my_portfolio.numbers')
exporter.to_yahoo_csv('output/')
exporter.to_ticker_yaml()
```

## Console Scripts
```bash
# Show Help Message
numbers-to-ticker-yaml --help
numbers-to-yahoo-csv --help

# Numbers to Ticker YAML
numbers-to-ticker-yaml portfolio.numbers

# Numbers to Yahoo CSV
numbers-to-yahoo-csv portfolio.numbers output/
```

## Numbers Portfolio Expected Format
Tables made with Apple Numbers should be formatted this way:
|Symbol|Price|Shares|Date|
|-|-|-|-|
|AAPL|140.37|5|2022-06-28|
|AAPL|140.96|-2|2022-06-28|
