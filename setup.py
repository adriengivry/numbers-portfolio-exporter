from setuptools import setup, find_packages

setup(
    name="numbers-portfolio-exporter",
    version="1.0",
    author="Adrien GIVRY",
    author_email="contact@adrien-givry.com",
    description="Package to export a stock portfolio from Apple Numbers to Yahoo Finance (CSV) and Ticker (YAML)",
    license="MIT",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/adriengivry/numbers-portfolio-exporter",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "numbers-to-yahoo-csv = numbers_portfolio_exporter.commands:numbers_to_yahoo_csv_command",
            "numbers-to-ticker-yaml = numbers_portfolio_exporter.commands:numbers_to_ticker_yaml_command",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)
