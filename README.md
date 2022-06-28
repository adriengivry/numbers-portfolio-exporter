# Stock Portfolio Exporter
## Quick Start
```properties
# Installation
pip install -r requirements.txt
pip install -e .

# Ticker Exporter Example
ticker-exporter portfolio.numbers ~/.ticker.base.yaml

# Yahoo Exporter Example
yahoo-exporter portfolio.numbers output.csv
```

## Stock Portfolio Sheet Format (.numbers)
|Symbol|Price|Shares|Date|
|-|-|-|-|
|AAPL|140.37|5|2022-06-28|
|AAPL|140.96|-2|2022-06-28|