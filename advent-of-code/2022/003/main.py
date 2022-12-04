#!/usr/bin/env python3


import os
from string import ascii_lowercase, ascii_uppercase


def priority(character: str) -> int:
    return (ascii_lowercase + ascii_uppercase).index(character) + 1


def part1(data: list[str]) -> int:
    count: int = 0
    for rucksack in data:
        midpoint: int = len(rucksack) // 2
        compartment1, compartment2 = rucksack[:midpoint], rucksack[midpoint:]
        common: str = (set(compartment1) & set(compartment2)).pop()
        count += priority(common)
    return count


def part2(data: list[str]) -> int:
    count: int = 0
    while data:
        r1, r2, r3 = [data.pop(0) for _ in range(3)]
        common: str = (set(r1) & set(r2) & set(r3)).pop()
        count += priority(common)
    return count


def main() -> int:
    DIRECTORY: str = os.path.dirname(__file__)
    with open(os.path.join(DIRECTORY, 'data', 'test.txt')) as f:
        data: list[str] = [line.strip('\n') for line in f.readlines()]

    print(part1(data=data))
    print(part2(data=data))
    return 0


if __name__ == '__main__':
    exit(main())
