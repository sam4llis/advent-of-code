#!/usr/bin/env python3

import os


class House:
    """A class to create house objects with unique (x, y) coordinates."""

    def __init__(self, x: int, y: int):
        self.x: int = x
        self.y: int = y
        self.visits: int = 1  # A house is created, so is technically visited.

    def __repr__(self) -> str:
        return f'House(x={self.x}, y={self.y}, count={self.visits})'

    def __eq__(self, other) -> bool:
        if not isinstance(other, House):
            return NotImplemented
        return self.x == other.x and self.y == other.y

    def visit(self):
        """When a house is visited, increment the `count` class variable."""
        self.visits += 1


def main() -> int:
    DIRECTORY: str = os.path.dirname(__file__)

    with open(os.path.join(DIRECTORY, 'data', 'test.txt')) as f:
        data: str = f.read()

    x: int = 0
    y: int = 0

    houses: list[House] = []

    # He begins by delivering a present to the house at his starting location.
    houses.append(House(x, y))

    for action in data:

        if action == '^':
            y += 1
        elif action == 'v':
            y -= 1
        elif action == '>':
            x += 1
        else:
            x -= 1

        # Create a new house with the updated coordinates.
        house: House = House(x, y)

        if house in houses:
            idx: int = houses.index(house)
            houses[idx].visit()  # Visit the house in the list.
        else:
            houses.append(House(x, y))

    # How many houses receive at least one present?
    print(len(houses))

    return 0


if __name__ == '__main__':
    exit(main())
