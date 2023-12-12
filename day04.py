def load(input_file):
    
    cards = []
    with open(input_file, 'r') as f:
        for line in f.readlines():

            line = line[:-1]
            while '  ' in line:
                line = line.replace('  ', ' ')

            numbers = line.split(': ')[1]
            own_numbers, winning_numbers = numbers.split(' | ')

            own_numbers = own_numbers.split(' ')
            own_numbers = [int(n) for n in own_numbers]

            winning_numbers = winning_numbers.split(' ')
            winning_numbers = [int(n) for n in winning_numbers] 
            
            cards.append((own_numbers, winning_numbers))
    
    return cards


def compute_points(own_numbers, winning_numbers):
    return len(set(own_numbers) & set(winning_numbers))


def part1(cards):
    
    result = 0

    for own_numbers, winning_numbers in cards:
        points = compute_points(own_numbers, winning_numbers)
        if points:
            result += 2 ** (points - 1)

    return result


def part2(cards):

    n_cards = [1 for i in range(len(cards))]

    for i, (own_numbers, winning_numbers) in enumerate(cards):
        points = compute_points(own_numbers, winning_numbers)
        for p in range(points):
            n_cards[i+p+1] += n_cards[i]
        
    return sum(n_cards)


def main():
    cards = load(input_file='inputs/day04/test.txt')
    assert part1(cards) == 13
    assert part2(cards) == 30

    cards = load(input_file='inputs/day04/input.txt')
    solution = part1(cards)
    print('Part 1 solution:', solution)
    assert solution == 17803

    solution = part2(cards)
    print('Part 2 solution:', solution)
    assert solution == 5554894


if __name__ == '__main__':
    main()
