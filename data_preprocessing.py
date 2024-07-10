import pandas as pd

class DataProc:
    def __init__(self, filename, delimiter, encoding='utf-8'):
        self.filename = filename
        self.delimiter = delimiter
        self.encoding = encoding

    def change_format_to_ddmmyy(self, columns):
        try:
            df = pd.read_csv(self.filename, delimiter=self.delimiter, encoding=self.encoding)

            for column in columns:
                df[column] = df[column].apply(
                    lambda x: f"{x.split('-')[2][:2]}.{x.split('-')[1]}.{x.split('-')[0]} 00:00:00" if isinstance(x, str) else x
                )
        
        except FileNotFoundError:
            return "The specified file was not found."
        except pd.errors.EmptyDataError:
            return "The file is empty."
        except pd.errors.ParserError:
            return f"Error parsing the file {self.filename}. Please check if it is a valid CSV file."

        return df
