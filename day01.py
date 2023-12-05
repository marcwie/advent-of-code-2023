def parse(line, allow_letters=False):

    pointer = 0
    digits = ''
    lookup = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6',
              'seven': '7', 'eight': '8', 'nine': '9'}

    while pointer < len(line):
        if line[pointer].isdigit():
            digits += line[pointer]
        elif line[pointer:pointer+3] in ['one', 'two', 'six'] and allow_letters:
            digits += lookup[line[pointer:pointer+3]]
        elif line[pointer:pointer+4] in ['four', 'five', 'nine'] and allow_letters:
            digits += lookup[line[pointer:pointer+4]]
        elif line[pointer:pointer+5] in ['three', 'seven', 'eight'] and allow_letters:
            digits += lookup[line[pointer:pointer+5]]
        pointer += 1

    return int(digits[0] + digits[-1])


def run(input_file, allow_letters):

    result = 0
    with open(input_file, 'r', encoding='utf-8') as f:
        for line in f.readlines():
            result += parse(line, allow_letters=allow_letters)

    return result


def main():
    assert run(input_file='inputs/day01/test_part1.txt', allow_letters=False) == 142
    solution = run(input_file='inputs/day01/input.txt', allow_letters=False)
    print('Part 1 solution:', solution)
    assert solution == 54927

    assert run(input_file='inputs/day01/test_part2.txt', allow_letters=True) == 281
    solution = run(input_file='inputs/day01/input.txt', allow_letters=True)
    print('Part 2 solution:', solution)
    assert solution == 54581


if __name__ == '__main__':
    main()
