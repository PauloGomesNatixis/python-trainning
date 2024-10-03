
def read_file1(filename: str) -> str:
    """
    Read a file and return its content.

    Args:
        filename (str): The name of the file to read.

    Returns:
        str: The content of the file.
    """
    # with open(filename, 'r') as file:
    #     content = file.read()
        
    # return content

    try:
        with open(filename, 'r') as file:
            content = file.read()

    except FileNotFoundError:
        print(f'File {filename} not found.')
        content = ''
        
    return content

print(read_file1('sample.txt'))



from typing import TextIO

def read_file(file: TextIO) -> str:
    """
    Read a file and return its content.

    Args:
        filename (TextIO): The file object to read.
    
    Returns:
        str: The content of the file.
    """
    content = file.read()
        
    return content

#with open('sample.txt', 'r') as file:
#    print(read_file(file))

    
# 7. Create a function called `write_file` that writes a string to a file.
# def write_file(filename: str, content: str) -> None:
#     """
#     Write content to a file.

#     Args:
#         filename (str): The name of the file to write.
#         content (str): The content to write to the file.
#     """
#     with open(filename, 'w') as file:
#         file.write(content)

# write_file('output.txt', 'Hello, Output!')

# with open('output.txt', 'r') as file:
#     print(file.read())


#9. Change the `write_file` function to append content to a file instead of overwriting it.
def write_file(filename: str, content: str) -> None:
    """
    Append content to a file.

    Args:
        filename (str): The name of the file to write.
        content (str): The content to append to the file.
    """
    with open(filename, 'a') as file:
        file.write(content)


with open('sample.txt', 'r') as file:
    print(read_file(file))

write_file('output.txt', '\nHello, Again!')

with open('output.txt', 'r') as file:
    print(file.read())
    
    
import csv

def create_csv_file(filename, data):
    """
    Creates a CSV file with the given data.

    Args:
        filename (str): The name of the CSV file to create.
        data (list): A list of lists, where each inner list represents a row in the CSV file.
    """
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(data)

# Example usage:
data = [
    ['Name', 'Age', 'City'],
    ['John Doe', 25, 'New York'],
    ['Jane Doe', 30, 'Los Angeles'],
    ['Bob Smith', 35, 'Chicago'],
    ['Alice Johnson', 20, 'Houston']
]

create_csv_file('example.csv', data)


#**Note**: In the future, we will learn about exception and logging handling in 
# Python - and you will be able to handle things more gracefully, as below:
import logging

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__)

def read_file(filename: str) -> str:
    """
    Read a file and return its content.

    Args:
        filename (str): The name of the file to read.

    Returns:
        str: The content of the file.
    """
    try:
        with open(filename, 'r') as file:
            logger.info(f'Reading file {filename}')
            content = file.read()

    except FileNotFoundError:
        logger.error(f'File {filename} not found.')
        content = ''
        
    return content


# ### Optional Challenge

# - Create a function to create a CSV file with at least 5 rows of data.
import csv

def create_csv_file(filename, data):
    """
    Creates a CSV file with the given data.

    Args:
        filename (str): The name of the CSV file to create.
        data (list): A list of lists, where each inner list represents a row in the CSV file.
    """
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(data)

# Example usage:
data = [
    ['Name', 'Age', 'City'],
    ['John Doe', 25, 'New York'],
    ['Jane Doe', 30, 'Los Angeles'],
    ['Bob Smith', 35, 'Chicago'],
    ['Alice Johnson', 20, 'Houston']
]

create_csv_file('example.csv', data)


# - Create a function to read the CSV file and print its content.

import csv

def read_csv_file(filename):
    """
    Reads a CSV file and prints its content.

    Args:
        filename (str): The name of the CSV file to read.
    """
    with open(filename, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            print(row)

# Example usage:

create_csv_file('example.csv', data)
read_csv_file('example.csv')


# - Create a function to append a new row of data to the CSV file.
import csv

def append_to_csv_file(filename, new_row):
    """
    Appends a new row to the CSV file.

    Args:
        filename (str): The name of the CSV file to append to.
        new_row (list): The new row to append to the CSV file.
    """
    with open(filename, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(new_row)

# Example usage:
new_row = ['Mike Brown', 40, 'San Francisco']
append_to_csv_file('example.csv', new_row)
read_csv_file('example.csv')