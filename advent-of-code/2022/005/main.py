#!/usr/bin/env python3

import os
import re

STACKS = [
    ['Z', 'N'],
    ['M', 'C', 'D'],
    ['P'],
]


def main() -> int:
    DIRECTORY: str = os.path.dirname(__file__)
    with open(os.path.join(DIRECTORY, 'data', 'test.txt')) as f:
        data = [line.strip('\n').strip() for line in f.readlines()]

    # Increment integer `i` until we reach the empty line - after this line is
    # the `move x from y to z` query data.
    i: int = 0
    while data[i]:
        i += 1

    queries: list[str] = data[i + 1 :]
    LINE_RE: re.Pattern = re.compile(r'move (\d+) from (\d+) to (\d+)')

    for query in queries:
        match: re.Match | None = re.search(LINE_RE, query)

        if match:
            _move, _from, _to = (int(m) for m in match.groups())

            # WARNING: As I'm using `.pop()` and `.extend()` methods, they will
            # directly affect the `STACKS` variable - therefore if both solutions
            # are ran at the same time then the latter will not produce the correct
            # result.

            # Part 1
            STACKS[_to - 1].extend([STACKS[_from - 1].pop() for _ in range(_move)])

            # Part 2
            # STACKS[_to - 1].extend((STACKS[_from - 1][-_move:]))
            # for _ in range(_move):
            #     STACKS[_from - 1].pop()

    # Printing the top crate in the stack to a human-readable string.
    print(''.join([stack[-1] for stack in STACKS]))
    return 0


if __name__ == '__main__':
    exit(main())
