import sys
from pathlib import Path

known_bf = set("><+-.,[]")


def parse_raw(raw_code_line):
    raw_bf = []
    braces_stack = []
    cycle_blocks = {}
    index = 0
    for char in raw_code_line:
        if char not in known_bf:
            continue
        raw_bf.append(char)

        if char == "[":
            braces_stack.append(index)
        elif char == "]":
            last_open_brace_idx = braces_stack.pop()
            cycle_blocks[index] = last_open_brace_idx
            cycle_blocks[last_open_brace_idx] = index

        index += 1

    return "".join(raw_bf), cycle_blocks


def run(raw_code):
    code, blocks = parse_raw(raw_code)
    pointer = 0
    code_i = 0
    bf = {0: 0}
    code_len = len(code)
    while code_i < code_len:
        sym = code[code_i]
        match sym:
            case ">":
                # move pointer to the right
                pointer += 1
                # init value for new pointer position
                bf.setdefault(pointer, 0)
            case "<":
                # move pointer to the left
                pointer -= 1
            case "+":
                # increase current value
                bf[pointer] += 1
            case "-":
                # decrease current value
                bf[pointer] -= 1
            case ".":
                # value out (as char)
                print(chr(bf[pointer]), end="")
            case ",":
                # value in (only integers)
                bf[pointer] = int(input("Input: "))
            case "[" if not bf[pointer]:
                # cycle start: move current step
                code_i = blocks[code_i]
            case "]" if bf[pointer]:
                # cycle end: move current step to start
                code_i = blocks[code_i]
        code_i += 1

    # print new line
    print()


if __name__ == "__main__":
    # user_input = input("Put your bf code here: ")
    # run(user_input)
    file_text = Path(sys.argv[1]).read_text()
    run(file_text)
