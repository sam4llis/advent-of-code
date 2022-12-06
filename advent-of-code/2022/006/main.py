#!/usr/bin/env python3


import os


def get_marker(data: str, number_distinct: int) -> int:
    for i in range(len(data)):
        if len(set(data[i : i + number_distinct])) == number_distinct:
            return i + number_distinct
    return 0


def main() -> int:
    DIRECTORY: str = os.path.dirname(__file__)
    with open(os.path.join(DIRECTORY, 'data', 'test.txt')) as f:
        data: str = f.read()

    part1, part2 = get_marker(data, 4), get_marker(data, 14)
    print(part1, part2)
    return 0


if __name__ == '__main__':
    exit(main())
