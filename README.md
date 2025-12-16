# Bookbot

BookBot is a simple Python command-line tool designed to analyze text files (books) and generate statistical reports. It calculates the total number of words and the frequency of each character in a given text file.

This project was built as part of the [Boot.dev](https://www.boot.dev) curriculum.

## Features

- **Word Count**: Calculates the total number of words in the provided text file.
- **Character Analysis**: Counts the occurrence of each character (case-insensitive) and displays them.
- **Sorted Report**: Presents the character counts in descending order of frequency.

## Prerequisites

- [Python 3](https://www.python.org/downloads/) must be installed on your machine.

## Installation

1. Clone this repository or download the source code.
   ```bash
   git clone https://github.com/bootdotdev/curriculum.git
   ```
   *(Note: Adjust the path if you only downloaded the bookbot directory)*

2. Navigate to the `bookbot` directory:
   ```bash
   cd bookbot
   ```

## Usage

To run the program, use the following command structure:

```bash
python3 main.py <path_to_book>
```

### Example

To analyze the provided *Pride and Prejudice* text:

```bash
python3 main.py books/prideandprejudice.txt
```

### Sample Output

```text
============ BOOKBOT ============
Analyzing book found at books/prideandprejudice.txt
----------- Word Count ----------
Found 121551 total words
--------- Character Count -------
e: 70000
t: 60000
a: 50000
...
============= END ===============
```

## Project Structure

- `main.py`: The entry point of the application. Handles command-line arguments and orchestrates the report generation.
- `stats.py`: Contains helper functions for analyzing the text (counting words, counting characters, sorting data).
- `books/`: A directory to store text files for analysis.

## Development

To add new features or modify the analysis logic, you can edit `stats.py` to add new functions and update `main.py` to use them.

## License

This project is for educational purposes.