import os

class DelimiterChecker:
    def __init__(self, filename, delimiter, encoding='utf-8'):
        self.filename = filename
        self.delimiter = delimiter
        self.encoding = encoding

    def check_and_correct_delimiters(self):
        try:
            with open(self.filename, 'r', encoding=self.encoding) as file:
                lines = file.readlines()

                if not lines:
                    return "The file is empty."

                # Count delimiters in the first row
                first_row = lines[0].strip()
                first_row_delimiter_count = first_row.count(self.delimiter)
                print(f'First row has {first_row_delimiter_count} delimiters')

                corrected_lines = [first_row]  # Add the first row to corrected lines

                # Check and correct rows with incorrect delimiter count
                count = 0
                for line_num, line in enumerate(lines[1:], start=2):
                    stripped_line = line.strip()
                    delimiter_count = stripped_line.count(self.delimiter)
                    if delimiter_count != first_row_delimiter_count:
                        corrected_line = self.correct_line(stripped_line)
                        corrected_lines.append(corrected_line)
                        count += 1
                        print(f"Line {line_num} corrected")
                    else:
                        corrected_lines.append(stripped_line)
                if count != 0:
                    new_filename = self.create_new_filename('corrected')
                    with open(new_filename, 'w', encoding=self.encoding) as new_file:
                        new_file.write("\n".join(corrected_lines))

                    return f"All rows processed. Corrected file saved as {new_filename}."

                return 'There are no wrong rows.'

        except FileNotFoundError:
            return "The specified file was not found."
        except UnicodeDecodeError:
            return f"Could not decode the file using the encoding {self.encoding}."

    def correct_line(self, line):
        corrected_line = []
        inside_quotes = False
        for char in line:
            if char == '"':
                inside_quotes = not inside_quotes
            if char == self.delimiter and inside_quotes:
                corrected_line.append(' ')  # Replace delimiter with space if inside quotes
            else:
                corrected_line.append(char)
        return ''.join(corrected_line)

    def create_new_filename(self, suffix):
        base, ext = os.path.splitext(self.filename)
        return f"{base}_{suffix}{ext}"

# # Example usage:
# filename = r'C:\Users\RM342AY\Downloads\VOITH_VTIP_Batch1\TPL_OTC_06_Customer_invoices.csv'
# delimiter = ';'
# encoding = 'utf-8'  # You can change this to the appropriate encoding

# checker = DelimiterChecker(filename, delimiter, encoding)
# print(checker.check_and_correct_delimiters())
