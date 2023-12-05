def load(input_file):

    data = {}
    with open(input_file, 'r', encoding='utf-8') as f:
        for line in f.readlines():
            line = line.replace('\n', '')

            game_id, outcomes = line.split(': ')
            game_id = int(game_id[5:])
            data[game_id] = []

            outcomes = outcomes.split('; ')
            for outcome in outcomes:
                outcome = outcome.split(', ')
                outcome = {dice.split(' ')[1]: int(dice.split(' ')[0])for dice in outcome}
                data[game_id].append(outcome)

    return data



def part1(input_file):

    valid = {'red': 12, 'green': 13, 'blue': 14}

    data = load(input_file)

    impossible = []
    result = 0

    for game_id, outcomes in data.items():
        for outcome in outcomes:
            for color, count in outcome.items():
                if count > valid[color]:
                    impossible.append(game_id)
                    break

        if game_id not in impossible:
            result += game_id

    return result


def part2(input_file):

    data = load(input_file)

    result = 0
    for outcomes in data.values():
        min_values = {'blue': 0, 'red': 0, 'green': 0}
        for outcome in outcomes:
            for color, count in outcome.items():
                if count > min_values[color]:
                    min_values[color] = count

        power = 1
        for count in min_values.values():
            power *= count

        result += power

    return result



def main():

    assert part1(input_file='inputs/day02/test.txt') == 8
    solution = part1(input_file='inputs/day02/input.txt')
    print('Part 1 solution:', solution)
    assert solution == 2439

    assert part2(input_file='inputs/day02/test.txt') == 2286
    solution = part2(input_file='inputs/day02/input.txt')
    print('Part 2 solution:', solution)
    assert solution == 63711


if __name__ == '__main__':
    main()
