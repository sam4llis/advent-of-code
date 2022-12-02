#!/usr/bin/env python3

import os


def main() -> int:
    DIRECTORY: str = os.path.dirname(__file__)
    with open(os.path.join(DIRECTORY, 'data', 'test.txt')) as f:
        data: list[str] = [line.rstrip('\n') for line in f.readlines()]

    lst: list[int] = []
    count: int = 0

    for number in data:
        if number:
            count += int(number)
        else:
            lst.append(count)
            count = 0

    # Sort `lst` in descending order.
    lst.sort(reverse=True)

    max: int = lst[0]
    sum_max_three: int = sum(lst[:3])

    print(max, sum_max_three)
    return 0


if __name__ == '__main__':
    exit(main())
