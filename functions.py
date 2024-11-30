def next_ten_numbers(number):
    """
    Takes in a number and returns the next 10 numbers as a comma-delimited string.

    Parameters:
    number (int): The starting number.

    Returns:
    str: The next 10 numbers as a comma-delimited string.
    """
    return ",".join(str(number + i) for i in range(1, 11))


def list_to_comma_string(string_list):
    """
    Converts a list of strings to a comma-delimited string.

    Parameters:
    string_list (list): A list of strings.

    Returns:
    str: A comma-delimited string.
    """
    return ",".join(string_list)


def write_to_csv(filename, headers, data):
    """
    Writes headers and data to a CSV file.

    Parameters:
    filename (str): Name of the file to write.
    headers (str): The headers of the CSV file.
    data (str): The data to write to the CSV file.
    """
    with open(filename, "w") as file:
        file.write(headers + "\n")
        file.write(data + "\n")
