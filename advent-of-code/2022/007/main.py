#!/usr/bin/env python3

from __future__ import annotations
from abc import ABC, abstractmethod
import os
import re


class FSNode(ABC):
    @abstractmethod
    def size(self):
        pass

    @abstractmethod
    def visit(self, visitor: FSNodeVisitor):
        pass


class Directory(FSNode):
    def __init__(self, name: str, parent=None) -> None:
        self.name: str = name
        self.children: list[Directory | File] = []
        self.parent: Directory | None = parent

    def add_file(self, child: Directory | File) -> None:
        self.children.append(child)

    def size(self) -> int:
        return sum(child.size() for child in self.children)

    def visit(self, visitor: FSNodeVisitor) -> None:
        visitor.visit_directory(self)
        for child in self.children:
            child.visit(visitor)


class File(FSNode):
    def __init__(self, name: str, size: int, parent=None) -> None:
        self.name: str = name
        self._size: int = size
        self.parent: Directory | None = parent

    def size(self) -> int:
        return self._size

    def visit(self, visitor: FSNodeVisitor) -> None:
        visitor.visit_file(self)


class FSNodeVisitor(ABC):
    @abstractmethod
    def visit_directory(self, directory: Directory):
        pass

    @abstractmethod
    def visit_file(self, file: File):
        pass


def parse(lines: list[str]) -> Directory:
    CD_RE: re.Pattern = re.compile(r'\$ cd (\S+)')
    LS_RE: re.Pattern = re.compile(r'\$ ls')
    FILE_LISTING_RE: re.Pattern = re.compile(r'(\d+) (\S+)')

    root: Directory = Directory('/')
    current_directory = root

    while lines:
        command: str = lines.pop(0)
        if match := CD_RE.match(command):
            directory: str = match.group(1)

            if directory == '/':
                current_directory = root
            elif directory == '..':
                if current_directory.parent:
                    current_directory = current_directory.parent
            else:
                new_node = Directory(directory, parent=current_directory)
                current_directory.add_file(new_node)
                current_directory = new_node

        elif match := LS_RE.match(command):
            while lines and not lines[0].startswith('$'):
                listing: str = lines.pop(0)
                if match := FILE_LISTING_RE.match(listing):
                    size, name = match.groups()
                    file: File = File(name, int(size), parent=current_directory)
                    current_directory.add_file(file)

    return root


def part1(lines) -> int:
    root: Directory = parse(lines)
    ans: int = 0

    class SolutionVisitor(FSNodeVisitor):
        def visit_directory(self, directory: Directory) -> None:
            nonlocal ans
            directory_size: int = directory.size()
            if directory_size > 100000:
                return
            ans += directory_size

        def visit_file(self, file: File) -> None:
            pass

    root.visit(SolutionVisitor())
    return ans


def part2(lines) -> int:
    root: Directory = parse(lines)

    CAPACITY: int = 70_000_000
    NEEDED_FOR_UPDATE: int = 30_000_000
    used_space: int = root.size()
    unused_space: int = CAPACITY - used_space
    need_to_free: int = NEEDED_FOR_UPDATE - unused_space

    directory_sizes: list[int] = []

    class SolutionVisitor(FSNodeVisitor):
        def visit_directory(self, directory: Directory) -> None:
            nonlocal directory_sizes
            directory_sizes.append(directory.size())

        def visit_file(self, file: File) -> None:
            pass

    root.visit(SolutionVisitor())
    deletion_candidates: list[int] = [d for d in directory_sizes if d > need_to_free]
    return min(deletion_candidates)


def main() -> int:
    DIRECTORY: str = os.path.dirname(__file__)
    with open(os.path.join(DIRECTORY, 'data', 'test.txt')) as f:
        lines: list[str] = [line.strip('\n') for line in f.readlines()]

    print(part1(lines=lines))
    print(part2(lines=lines))
    return 0


if __name__ == '__main__':
    exit(main())
