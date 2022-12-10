#!/usr/bin/env python3

import os
import re


def pprint(data: list):
    for y in range(len(data)):
        for x in range(len(data[0])):
            print('#' if data[y][x] else '.', end=' ')
        print()
    print()


def parse(lines: list[str]) -> list[int]:
    ADDX_RE: re.Pattern = re.compile(r'addx (-?\d+)')
    data: list[int] = []
    for line in lines:
        data.append(0)
        match = re.match(ADDX_RE, line)
        if match:
            data.append(int(match.group(1)))
    return data


def part1(data: list[int]) -> int:
    register: int = 1
    result: int = 0
    for cycle, entry in enumerate(data, start=1):
        if cycle in [20, 60, 100, 140, 180, 220]:
            result += cycle * register
        register += entry
    return result


def part2(data: list[int]) -> list[list[int]]:
    # Create output dimensions and map.
    rows, cols = 6, 40
    MAP: list[list[int]] = [[0 for _ in range(cols)] for _ in range(rows)]

    # Initialise counting variables.
    line_number: int = 0
    register: int = 1
    sprite_position: tuple[int, int] = (0, 2)

    while line_number < rows:
        for cycle in range(cols * line_number, cols * line_number + cols):
            start, end = sprite_position
            MAP[line_number][cycle % cols] = 1 if start <= cycle % cols <= end else 0
            register += data[cycle]
            sprite_position = register - 1, register + 1
        line_number += 1
    return MAP


def main() -> int:
    DIRECTORY: str = os.path.dirname(__file__)
    with open(os.path.join(DIRECTORY, 'data', 'test.txt')) as f:
        data: list[str] = [line.strip('\n') for line in f.readlines()]

    print(part1(data=parse(data)))
    pprint(part2(data=parse(data)))
    return 0


if __name__ == '__main__':
    exit(main())
