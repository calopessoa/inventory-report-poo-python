# Inventory Report

This project was developed to generate a series of inventory reports, using as entry points data files and, as output, a report about those files.
For this effort, it was used the Object-oriented programming (OOP) paradigm, following the principles of SOLID with Python language. 

Mainly, there are two types of reports, a simple one and a complete one (simples == simple / complete == completo).
The inventory data were obtained from three distinct sources:

- JSON file;

- CSV file;

- XML file.

## Tools used

  - Python
  - Pytest

## How to run it

Please clone this project from source and move into its folder.

```bash
$ git clone git@github.com:calopessoa/inventory-report-poo-python.git

$ cd inventory-report-poo-python
```

To boot it, run the following steps:

  ```bash
  # create a virtual environment
  $ python3 -m venv .venv

  # activate the virtual environment
  $ source .venv/bin/activate

  # using the virtual environment, install the dependencies
  $ python3 -m pip install -r dev-requirements.txt

  # then, install itself
  $ pip install .
  ```

  Finally, to run the application, run either 
  Para executar a aplicação, insira o comando no seguinte formato:
  
  ```bash
  $ inventory_report <entry_file_path> <report_type>
  ```

  Exemplo: 
  
  ```bash
  inventory_report inventory_report/data/inventory.csv simples
  ```

  To run the tests, run the following command:

  ```bash
  $ python3 -m pytest
  ```

