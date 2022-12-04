#!/usr/bin/env python3

from dataclasses import dataclass
import os


@dataclass
class Elf:
    start: int
    end: int


@dataclass
class ElfPair:
    elf1: Elf
    elf2: Elf


def part1(data: list[ElfPair]) -> int:
    count: int = 0
    for pair in data:
        elf1, elf2 = pair.elf1, pair.elf2
        if elf1.start <= elf2.start and elf1.end >= elf2.end:
            count += 1
        elif elf2.start <= elf1.start and elf2.end >= elf1.end:
            count += 1
    return count


def part2(data: list[ElfPair]) -> int:
    count: int = 0
    for pair in data:
        elf1, elf2 = pair.elf1, pair.elf2
        if elf1.start <= elf2.start <= elf1.end or elf2.start <= elf1.start <= elf2.end:
            count += 1
    return count


def main() -> int:
    DIRECTORY: str = os.path.dirname(__file__)
    with open(os.path.join(DIRECTORY, 'data', 'test.txt')) as f:
        data: list[list[str]] = [line.strip('\n').split(',') for line in f.readlines()]

    lst: list[ElfPair] = []
    for line in data:
        i, j = [group.split('-') for group in line]
        lst.append(ElfPair(Elf(*[int(n) for n in i]), Elf(*[int(n) for n in j])))

    print(part1(data=lst))
    print(part2(data=lst))
    return 0


if __name__ == '__main__':
    exit(main())
