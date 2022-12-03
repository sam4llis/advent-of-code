#!/usr/bin/env python3


import os


def character_to_int(character: str) -> int:
    unicode_number: int = ord(character) - 96
    # The character is uppercase.
    if unicode_number < 0:
        return ord(character.lower()) - 96 + ord('z') - 96
    # The character is lowercase.
    return unicode_number


def part1(data: list[str]) -> int:
    count: int = 0
    for rucksack in data:
        compartment1: str = rucksack[: len(rucksack) // 2]
        compartment2: str = rucksack[len(rucksack) // 2 :]

        dictionary = dict.fromkeys(compartment1, 0)
        for character in compartment2:

            if character in dictionary:
                dictionary[character] += 1

                # If the dictionary value is not zero.
                if dictionary[character]:
                    count += character_to_int(character=character)
                    dictionary.clear()  # Clear the dictionary before restarting the loop.
    return count


def part2(data: list[str]) -> int:
    nested_data: list[list[str]] = [data[i : i + 3] for i in range(0, len(data), 3)]

    count: int = 0
    for group in nested_data:
        dictionary = dict.fromkeys([item for rucksack in group for item in rucksack], 0)

        for rucksack in group:
            for item in ''.join(set(rucksack)):
                dictionary[item] += 1
                if dictionary[item] == 3:
                    count += character_to_int(item)
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
