from setuptools import setup, find_packages

main_ns = {}
with open("src/_version.py") as ver_file:
    exec(ver_file.read(), main_ns)


setup(
    name="stock-portfolio-exporter",
    version=main_ns["__version__"],
    author="Adrien GIVRY",
    author_email="contact@adrien-givry.com",
    description="Package to export a stock portfolio from Apple Numbers to Ticker and Yahoo",
    license="MIT",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/adriengivry/stock-portfolio-exporter",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    entry_points={
        "console_scripts": [
            "ticker-exporter = ticker_exporter.__main__:main",
            "yahoo-exporter = yahoo_exporter.__main__:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)
