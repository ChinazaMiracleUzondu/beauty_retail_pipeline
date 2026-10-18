# Beauty Retail Sales Data Pipeline

## Project Overview

This project is a Python-based retail analytics pipeline designed
to process sales transactions from multiple beauty retail branches.

The program reads transaction records from a CSV file, validates
the data, removes invalid records, and generates a summary report
to support business decision-making.

## Problem Statement

Retail businesses collect large amounts of sales information.
However, some records may contain missing values, invalid dates,
incorrect data types, or negative amounts.

These problems can affect the accuracy of sales reports.

This project provides a simple automated solution for cleaning
transaction data and calculating useful business metrics.

## Project Objectives

- Read retail transaction records from a CSV file.
- Convert numeric text into appropriate Python data types.
- Validate branch IDs, transaction dates, customer tiers,
  item counts, and revenue.
- Identify and reject invalid transactions.
- Calculate sales totals and average revenue.
- Determine the percentage of valid records retained.
- Identify the top-performing retail branch.
- Calculate customer tier breakdowns.
- Filter transactions with positive revenue.
- Apply an example tax adjustment.
- Calculate estimated net margins.
- Generate a formatted terminal report.

## Dataset

The project uses simulated beauty retail transaction records.

Each transaction contains:

- branch_id
- transaction_date
- customer_tier
- item_count
- revenue

The dataset is stored in:

data/transactions.csv

The sample dataset contains seven transactions.
Five transactions are valid, while two contain invalid values.

The invalid records are included to demonstrate data validation
and error handling.

## Project Structure

beauty_retail_pipeline/
│
├── main.py
├── README.md
├── requirements.txt
│
├── data/
│   └── transactions.csv
│
├── pipeline/
│   ├── __init__.py
│   ├── schema.py
│   ├── ingestion.py
│   ├── validator.py
│   ├── transformer.py
│   └── reporter.py
│
└── tests/
    ├── test_validator.py
    ├── test_transformer.py
    └── test_reporter.py

## Module Responsibilities

### main.py

Coordinates the data ingestion, validation, and reporting process.

### schema.py

Defines the TransactionRecord class used to represent
individual retail transactions.

### ingestion.py

Reads the CSV dataset, converts numeric values, validates records,
and counts the original transactions.

### validator.py

Contains functions for validating transaction fields
and converting numeric values.

### transformer.py

Contains functions for calculating business metrics
and performing functional data transformations.

### reporter.py

Defines the SalesReporter class, which uses the transformation
functions to generate a formatted sales summary.

## Object-Oriented Programming

The project uses two classes:

1. TransactionRecord
2. SalesReporter

TransactionRecord represents an individual retail sale.

SalesReporter receives a collection of TransactionRecord objects
and produces summary metrics.

This demonstrates interaction between classes.

## Functional Programming

The project demonstrates functional programming through:

- map()
- filter()
- lambda functions
- List comprehensions
- Generator expressions

These operations calculate results without directly modifying
the original transaction objects.

## Data Validation and Error Handling

The pipeline checks for:

- Missing branch IDs
- Invalid transaction dates
- Missing customer tiers
- Negative item counts
- Negative revenue
- Invalid numeric values
- Missing required CSV columns

Invalid transactions are excluded from the final calculations.

The program uses try and except statements to handle
numeric conversion errors.

## Business Metrics

The final report includes:

- Total valid transactions
- Total items sold
- Total revenue
- Average revenue
- Gross sales
- Clean record retention percentage
- Top-performing branch
- Revenue by branch
- Customer tier breakdown
- Active transactions
- Tax-adjusted revenue
- Estimated net margins

## Calculation Assumptions

The sample tax calculation uses a default rate of 13%.

This rate is an illustrative assumption and does not represent
the correct tax rate for every geographical region.

The project currently applies the same default rate to all
transactions unless another rate is supplied.

Estimated net margins use an assumed cost rate of 60%.

Therefore, the estimated margin is 40% of revenue.

These figures are demonstrations and are not based on actual
business expense records.

## Installation Instructions

1. Install Python.
2. Open the beauty_retail_pipeline folder in VS Code.
3. Open the VS Code terminal.
4. Create a virtual environment:

   python -m venv .venv

5. Activate the virtual environment on Windows PowerShell:

   .\.venv\Scripts\Activate.ps1

6. Install the required package:

   python -m pip install -r requirements.txt

The project uses Python's built-in CSV module, which does
not require separate installation.

## How to Run the Project

Open the terminal inside the project folder.

Run:

```bash
python main.py
```

The program reads the CSV file and displays the sales report.

## How to Run Unit Tests

Run:

```bash
python -m pytest tests/ -v
```

The project currently contains ten automated unit tests
covering validation, transformation, and reporting functions.

All ten original tests passed during development.

## Sample Results

Using the included simulated dataset:

- Total raw transactions: 7
- Total valid transactions: 5
- Invalid transactions: 2
- Total items sold: 20
- Total revenue: $615.50
- Average revenue: $123.10
- Gross sales: $615.50
- Clean record retention: 71.43%
- Top-performing branch: BR002
- Active transactions: 5
- Revenue including example tax: $695.51
- Estimated total net margin: $246.20

## Sales by Branch

- BR001: $271.00
- BR002: $299.50
- BR003: $45.00

## Customer Tier Breakdown

- Gold: 2 transactions
- Silver: 1 transaction
- Regular: 2 transactions

## Project Usefulness

This project demonstrates how Python can automate repetitive
data preparation tasks.

It helps illustrate how retail businesses can identify
invalid transactions and produce reliable operational reports.

The modular structure also makes the code easier to maintain,
test, and extend.

## Project Contributions

This project was developed as an individual academic assignment.

The student is responsible for understanding, reviewing,
testing, and maintaining the submitted project code.

AI assistance was used as a learning and debugging resource
during development.

## Technologies Used

- Python
- Python CSV module
- Pytest
- Visual Studio Code

## Future Improvements

Possible future enhancements include:

- Branch-specific regional tax configurations
- Larger retail datasets
- Exporting reports to CSV or Excel
- Additional automated tests
- Data visualizations
- More detailed cost and profit analysis

