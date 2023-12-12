from itertools import product

def load(input_file):
     
    with open(input_file, 'r') as f:
        lines = [[*l[:-1]] for l in f.readlines()]

    return lines


def neighbor_indices(i, j, n_lines, n_rows):

    indices = []
    
    for n_i, n_j in product(range(i-1, i+2), range(j-1, j+2)):
        if (n_i >= 0) & (n_i < n_lines) & (n_j >= 0) & (n_j < n_rows):
            indices.append((n_i, n_j))

    return indices


def sum_of_part_numbers(data):

    n_lines = len(data)
    n_rows = len(data[0])
    
    digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    numbers = []
    in_number = False
    current_number = ''
    is_part_number = False

    for i, j in product(range(n_lines), range(n_rows)):
        if data[i][j] in digits:
            in_number = True
            current_number += data[i][j]
            for (neighbor_i, neighbor_j) in neighbor_indices(i, j, n_lines, n_rows):
                if data[neighbor_i][neighbor_j] not in digits and data[neighbor_i][neighbor_j] != '.':
                    is_part_number = True
        else:
            in_number = False
            if current_number != '' and is_part_number:
                numbers.append(int(current_number))
            current_number = '' 
            is_part_number = False

    return(sum(numbers))

        
def gear_ratio(data):

    digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    n_lines = len(data)
    n_rows = len(data[0])
    
    gear_positions = []
    for i in range(n_lines):
        for j in range(n_rows):
            if data[i][j] == '*':
                gear_positions.append((i, j))

    numbers = []
    for i in range(n_lines):
        indices = []
        current_number = ''
        for j in range(n_rows):
            if data[i][j] in digits:
                current_number += data[i][j]
                indices.append((i, j))
            elif current_number != '':
                numbers.append((int(current_number), indices))
                indices = []
                current_number = ''
        else:
            if current_number != '':
                numbers.append((int(current_number), indices))
    
    results = []
    for gear_i, gear_j in gear_positions:
        neighbors = neighbor_indices(gear_i, gear_j, n_lines, n_rows)
        gear_ratio = [] 
        for number, indices in numbers:
            valid_number = False
            for index_pair in indices:
                if index_pair in neighbors:
                    valid_number = True
            if valid_number:
                gear_ratio.append(number)
        if len(gear_ratio) == 2:
            results.append(gear_ratio[0] * gear_ratio[1])
    
    return sum(results)


def main():
    data = load(input_file='inputs/day03/test.txt')
    assert sum_of_part_numbers(data) == 4361
    assert gear_ratio(data) == 467835

    data = load(input_file='inputs/day03/input.txt')
    solution = sum_of_part_numbers(data)
    print('Part 1 solution:', solution)
    assert solution == 553825

    solution = gear_ratio(data)
    print('Part 2 solution:', solution)
    assert solution == 93994191


if __name__ == '__main__':
    main()

