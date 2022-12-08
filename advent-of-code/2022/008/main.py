#!/usr/bin/env python3


from dataclasses import dataclass
import os


@dataclass
class Tree:
    x: int
    y: int
    size: int
    visible: bool = False
    scenic_score: int = 1


class TreeMap:
    def __init__(self, treemap: list[Tree], max_x: int, max_y: int) -> None:
        self.treemap: list[Tree] = treemap
        self.max_x = max_x
        self.max_y = max_y

    def get_index(self, x: int, y: int) -> int:
        return x + self.max_y * y

    def parse_tree_visible(self) -> None:
        for tree in self.treemap:
            # Boundary conditions.
            if tree.x <= 0 or tree.x >= self.max_x - 1 or tree.y <= 0 or tree.y >= self.max_y - 1:
                tree.visible = True
            else:
                north, south, east, west = 0, 0, 0, 0

                # Case North.
                y = tree.y - 1
                x = tree.x
                while y >= 0:
                    north = max(north, self.treemap[self.get_index(x, y)].size)
                    y -= 1

                # Case South.
                y = tree.y + 1
                x = tree.x
                while y < self.max_y:
                    south = max(south, self.treemap[self.get_index(x, y)].size)
                    y += 1

                # Case East.
                y = tree.y
                x = tree.x + 1
                while x < self.max_x:
                    east = max(east, self.treemap[self.get_index(x, y)].size)
                    x += 1

                # Case West.
                y = tree.y
                x = tree.x - 1
                while x >= 0:
                    west = max(west, self.treemap[self.get_index(x, y)].size)
                    x -= 1

                if any([direction < tree.size for direction in (north, south, east, west)]):
                    tree.visible = True

    def parse_tree_scenic_score(self) -> None:
        for tree in self.treemap:
            north, south, east, west = 0, 0, 0, 0

            # Case North.
            y = tree.y - 1
            x = tree.x
            while y >= 0:
                if self.treemap[self.get_index(x, y)].size >= tree.size:
                    north += 1
                    break
                else:
                    north += 1
                    y -= 1

            # Case South.
            y = tree.y + 1
            x = tree.x
            while y < self.max_y:
                south += 1
                if self.treemap[self.get_index(x, y)].size >= tree.size:
                    break
                y += 1

            # Case East.
            y = tree.y
            x = tree.x + 1
            while x < self.max_x:
                east += 1
                if self.treemap[self.get_index(x, y)].size >= tree.size:
                    break
                x += 1

            # Case West.
            y = tree.y
            x = tree.x - 1
            while x >= 0:
                west += 1
                if self.treemap[self.get_index(x, y)].size >= tree.size:
                    break
                x -= 1

            tree.scenic_score = north * south * east * west

    def part1(self) -> int:
        count: int = 0
        for tree in self.treemap:
            count += tree.visible
        return count

    def part2(self) -> int:
        return max(tree.scenic_score for tree in self.treemap)


def parse(lines: list[str]) -> tuple[list[Tree], int, int]:
    max_x: int = len(lines)
    max_y: int = len(lines[0])

    lst: list[Tree] = []
    for y, row in enumerate(lines):
        for x, col in enumerate(row):
            lst.append(Tree(x=x, y=y, size=int(col)))
    return lst, max_x, max_y


def main() -> int:
    DIRECTORY: str = os.path.dirname(__file__)
    with open(os.path.join(DIRECTORY, 'data', 'test.txt')) as f:
        lines: list[str] = [line.strip('\n') for line in f.readlines()]

    data, max_x, max_y = parse(lines=lines)
    treemap: TreeMap = TreeMap(treemap=data, max_x=max_x, max_y=max_y)

    treemap.parse_tree_visible()
    print(treemap.part1())

    treemap.parse_tree_scenic_score()
    print(treemap.part2())

    return 0


if __name__ == '__main__':
    exit(main())
