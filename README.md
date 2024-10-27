# Number Pyramid Generator

This repository contains a Python program that generates a number pyramid based on a user-defined height. With a simple input, the program creates a pyramid where each row consists of an increasing sequence of numbers, adding an extra number in each subsequent row until it reaches the specified height.

## Example Output

For an input of `5`, the output will be:

```
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
```

For an input of `3`, the output will be:

```
1
1 2
1 2 3
```

## Features

- **Dynamic Pyramid Creation**: The program generates rows dynamically based on user input.
- **Simple and Clear Output**: Rows of increasing numbers form a visually satisfying pyramid pattern.
- **User-Friendly**: Easy-to-follow prompt and immediate output.

## Getting Started

### Prerequisites

- **Python 3.x** is required to run this program. You can download it from [python.org](https://www.python.org/).

### Installation

1. **Clone the Repository**:
   Clone the repository to your local machine using:
   ```bash
   git clone https://github.com/yourusername/number-pyramid-generator.git
   cd number-pyramid-generator
   ```

2. **Run the Program**:
   Run the script directly from the command line:
   ```bash
   python pyramid_generator.py
   ```

3. **Enter the Desired Height**:
   When prompted, enter an integer to define the height of the pyramid:
   ```
   Please enter a number: 5
   ```

## Code Explanation

The script builds the pyramid row by row:
- It initializes an empty string `row_output` to accumulate numbers for each row.
- In each iteration, the program appends the current row number, separated by a space, to `row_output` and prints it immediately.
- This process continues until the pyramid reaches the specified height.

```python
# User input for pyramid height
num = int(input("Please enter a number: "))

# Initialize empty string for row contents
row_output = ""

# Loop through each row up to the specified number
for i in range(1, num + 1):
    # Append the current row number to row_output
    row_output += f"{i} "
    # Print the current row
    print(row_output)
```

## File Structure

```
number-pyramid-generator/
├── README.md               # Project overview, examples, and usage details
├── pyramid_generator.py     # Main Python script to generate the pyramid
```

## Example Usage

For example, if the user inputs `4` when prompted, the output would be:

```
1
1 2
1 2 3
1 2 3 4
```

## Contributing

We welcome contributions! If you have ideas to improve this program, please:
1. Fork this repository.
2. Make your changes.
3. Submit a pull request.

Please make sure your code adheres to best practices and includes clear comments.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

---
