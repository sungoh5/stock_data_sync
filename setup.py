from setuptools import find_packages, setup

with open('.version') as version_file:
    version = version_file.read()

setup(
    name='stock-data-sync',
    version=version,
    description='This project syncs the stock data using yahoo finance',
    author='Sungoh Kim',
    author_email='sungoh5.kim@g.skku.edu',
    packages=find_packages(exclude=["tests", "*.tests", "*.tests.*", "tests.*"]),
    install_requires=[
        'pymongo==3.11.4',
        'yfinance==0.1.59'
        ],
    include_package_data=True
)
