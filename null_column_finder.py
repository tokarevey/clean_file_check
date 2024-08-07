import pandas as pd
import os

class ColumnNaNChecker:
    def __init__(self, filename, delimiter=';', encoding='utf-8'):
        self.filename = filename
        self.delimiter = delimiter
        self.encoding = encoding

    def check_columns_with_nan(self):
        try:
            # Read the CSV file into a pandas DataFrame
            df = pd.read_csv(self.filename, delimiter=self.delimiter, encoding=self.encoding, keep_default_na=False, na_values=['NULL', 'NaN', ''])

            # Check for NaN values in each column
            columns_with_nan = df.columns[df.isna().any()].tolist()

            if columns_with_nan:
                return f"Columns with NaN values: {columns_with_nan}"
            else:
                return "No columns with NaN values found."

        except FileNotFoundError:
            return "The specified file was not found."
        except pd.errors.EmptyDataError:
            return "The file is empty."
        except pd.errors.ParserError:
            return f"Error parsing the file {self.filename}. Please check if it is a valid CSV file."

