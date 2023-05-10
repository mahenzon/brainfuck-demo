"""
https://github.com/sstelian/Text-to-Brainfuck/blob/master/brainfuck_generator.py
"""

import argparse
from pathlib import Path


# Clears the current and the next cell.
# Uses current cell as a counter for a loop that increments the next cell 10 times.
# Loop runs for the number given by
# the integer division of the ASCII code by 10.
# The final ASCII code is obtained by further incrementing the cell
# based on the remainder of the division by 10.


def char_to_bf(char):
    buffer = "[-]>[-]<"
    for i in range(ord(char) // 10):
        buffer = buffer + "+"
    buffer = buffer + "[>++++++++++<-]>"
    for i in range(ord(char) % 10):
        buffer = buffer + "+"
    buffer = buffer + ".<"
    return buffer


# Uses a similar algorithm to char_to_bf(), but can also decrement, based on the sign of the given argument.
# Optimizes the final Brainfuck source code by altering the current value in the cell, instead of clearing and
# starting from 0.


def delta_to_bf(delta):
    # return char_code_to_bf(delta)
    buffer = ""
    for _i in range(abs(delta) // 10):
        buffer = buffer + "+"

    buffer = buffer + "[>++++++++++<-]>" if delta > 0 else buffer + "[>----------<-]>"

    for _i in range(abs(delta) % 10):
        buffer = buffer + "+" if delta > 0 else buffer + "-"
    buffer = buffer + ".<"
    return buffer


# Uses the previous helper functions to generate Brainfuck source that prints the string argument of this function.
# The commented argument puts code that generates one character on a new line and appends the printed character, which
# is considered a comment in Brainfuck. Valid Brainfuck source characters are stripped.


def string_to_bf(string):
    buffer = ""
    if string is None:
        return buffer
    for i, char in enumerate(string):
        if i == 0:
            buffer = buffer + char_to_bf(char)
        else:
            delta = ord(string[i]) - ord(string[i - 1])
            buffer = buffer + delta_to_bf(delta)
    return buffer


def main():
    parser = argparse.ArgumentParser(
        description="Text to Brainfuck generator. (C) Stelian Saracut 2018.",
    )
    parser.add_argument(
        "--string",
        metavar="S",
        help="String to be printed by Brainfuck source code.",
        required=True,
    )
    parser.add_argument(
        "--file",
        metavar="O",
        help="Brainfuck output file. Leave blank to output to console.",
    )

    args = parser.parse_args()

    source_code = string_to_bf(args.string)

    if args.file is None:
        print(source_code)
    else:
        Path(args.file).write_text(source_code)


if __name__ == "__main__":
    main()
