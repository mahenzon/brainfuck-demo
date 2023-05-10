"""
+-----------+------------+
| Character | ASCII Code |
+-----------+------------+
|     H     |     72     |
|     i     |    105     |
|     ,     |     44     |
|           |     32     |
|     P     |     80     |
|     y     |    121     |
|     t     |    116     |
|     h     |    104     |
|     o     |    111     |
|     n     |    110     |
|     !     |     33     |
+-----------+------------+
"""
from prettytable import PrettyTable

# Define the string
string = "Hi, Python!"

# Create a table with two columns
table = PrettyTable(["Character", "ASCII Code"])

# Add the data to the table
for c in string:
    table.add_row([c, str(ord(c))])

# Print the table
print(table)
