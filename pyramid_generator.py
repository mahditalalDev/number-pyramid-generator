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