#!/usr/bin/env python3

from __future__ import annotations
import collections
import functools
import heapq
import math
import operator
import os
import re
from dataclasses import dataclass
from typing import Callable


@dataclass
class Monkey:
    uid: int
    items: collections.deque[int]
    operator: Callable
    value: int | None
    divisor: int
    true: int
    false: int
    inspections: int = 0

    def get_new_value(self) -> int:
        item: int = self.items.popleft()

        # If the new value is equal to old (operation) old...
        if self.value is None:
            return self.operator(item, item)

        # If the new value is equal to old (operation) int...
        return self.operator(item, self.value)


def parse(data: list[str]) -> list[Monkey]:
    VALUE_RE: re.Pattern = re.compile(r'.* (\d+)')

    monkeys: list[Monkey] = []
    for i in range(0, len(data), 7):
        monkey: list = []
        monkey.append(int(data[i][7:-1]))
        monkey.append(collections.deque((int(n) for n in data[i + 1][18:].split(','))))
        monkey.append(operator.add if '+' in data[i + 2] else operator.mul)

        for j in range(2, 6):
            match: re.Match | None = re.match(VALUE_RE, data[i + j])
            monkey.append(int(match.group(1)) if match else None)

        monkeys.append(Monkey(*monkey))
    return monkeys


def play(monkeys: list[Monkey], rounds: int = 20, part2: bool = False) -> int:
    modulus: int = 0
    if part2:
        modulus = math.lcm(*[monkey.divisor for monkey in monkeys])

    for _ in range(rounds):
        for monkey in monkeys:
            while monkey.items:
                if part2:
                    item: int = monkey.get_new_value() % modulus
                else:
                    item: int = monkey.get_new_value() // 3
                if item % monkey.divisor == 0:
                    monkeys[monkey.true].items.append(item)
                else:
                    monkeys[monkey.false].items.append(item)
                monkey.inspections += 1
    return functools.reduce(operator.mul, heapq.nlargest(2, [m.inspections for m in monkeys]))


def main() -> int:
    DIRECTORY: str = os.path.dirname(__file__)
    with open(os.path.join(DIRECTORY, 'data', 'test.txt')) as f:
        lines: list[str] = [line.strip('\n') for line in f.readlines()]

    monkeys = parse(data=lines)
    print(play(monkeys=monkeys))

    monkeys = parse(data=lines)
    print(play(monkeys=monkeys, rounds=10000, part2=True))
    return 0


if __name__ == '__main__':
    exit(main())
