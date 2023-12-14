import math


def load(input_file, part2=False):

    with open(input_file, 'r') as f:
        time = f.readline()[:-1]
        distance = f.readline()[:-1]

    time = time.split(':')[1].split(' ')
    time = [entry for entry in time if entry != '']

    distance = distance.split(':')[1].split(' ')
    distance = [entry for entry in distance if entry != '']

    if part2:
        time = [int(''.join(time))]
        distance = [int(''.join(distance))]
    else:
        time = map(int, time)
        distance = map(int, distance)

    return time, distance


def ways_to_win(time, distance):
    t0 = time / 2 - (time ** 2 / 4 - distance) ** 0.5
    t1 = time / 2 + (time ** 2 / 4 - distance) ** 0.5

    if (t0 % 1) == 0:
        t0 += 1
    if (t1 % 1) == 0:
        t1 -= 1

    return math.floor(t1) - math.ceil(t0) + 1


def solve(time, distance):

    result = 1
    for time, distance in zip(time, distance):
        result *= ways_to_win(time, distance)
    return result


def main():

    data = load(input_file='inputs/day06/test.txt')
    assert solve(*data) == 288

    data = load(input_file='inputs/day06/input.txt')
    solution = solve(*data)
    print('Part 1 solution:', solution)
    assert solution == 4403592

    data = load(input_file='inputs/day06/input.txt', part2=True)
    solution = solve(*data)
    print('Part 2 solution:', solution)
    assert solution == 38017587


if __name__ == '__main__':
    main()
