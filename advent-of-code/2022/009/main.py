#!/usr/bin/env python3

from dataclasses import dataclass
import itertools
import os


@dataclass
class Knot:
    x: int
    y: int


def signum(n: int):
    return -1 if n < 0 else 0 if n == 0 else 1


def simulate(lines: list[str], n_knots: int) -> int:
    knots: list[Knot] = [Knot(0, 0) for _ in range(n_knots)]
    head, tail = knots[0], knots[-1]
    tail_visited: set[tuple[int, int]] = set()

    for line in lines:
        direction, count = line.split()
        count = int(count)

        while count:
            count -= 1

            if direction == 'R':
                head.x += 1
            elif direction == 'L':
                head.x -= 1
            elif direction == 'U':
                head.y += 1
            elif direction == 'D':
                head.y -= 1

            # Update each knot in the rope (k2) based on the position of the
            # knot that came before it.
            for k1, k2 in itertools.pairwise(knots):
                dx, dy = k1.x - k2.x, k1.y - k2.y

                # If k1 and k2 aren't touching, k2 should move.
                if abs(dx) > 1 or abs(dy) > 1:
                    k2.x += signum(dx)
                    k2.y += signum(dy)

            tail_visited.add((tail.x, tail.y))

    return len(tail_visited)


def main() -> int:
    DIRECTORY: str = os.path.dirname(__file__)
    with open(os.path.join(DIRECTORY, 'data', 'test.txt')) as f:
        lines: list[str] = [line.strip('\n') for line in f.readlines()]

    # Part 1.
    print(simulate(lines=lines, n_knots=2))

    # Part 2.
    print(simulate(lines=lines, n_knots=10))
    return 0


if __name__ == '__main__':
    exit(main())
