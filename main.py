def check_delimiters(filename, delimiter, encoding='utf-8'):
    try:
        with open(filename, 'r', encoding=encoding) as file:
            lines = file.readlines()

            if not lines:
                return "The file is empty."

            # Count delimiters in the first row
            first_row = lines[0].strip()
            first_row_delimiter_count = first_row.count(delimiter)

            # Check if all other rows have the same delimiter count
            for line_num, line in enumerate(lines[1:], start=2):
                if line.strip().count(delimiter) != first_row_delimiter_count:
                    return f"Line {line_num} does not match the delimiter count of the first row."

            return "All rows have the same number of delimiters."

    except FileNotFoundError:
        return "The specified file was not found."
    except UnicodeDecodeError:
        return f"Could not decode the file using the encoding {encoding}."


# Example usage:
filename = r'...'
delimiter = ','
encoding = 'utf-8'  # You can change this to the appropriate encoding

result = check_delimiters(filename, delimiter, encoding)
print(result)
