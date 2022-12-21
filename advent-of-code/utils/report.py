#!/usr/bin/env python3


from __future__ import annotations
from dataclasses import dataclass
import json
import datetime
import os
import time
from typing import Any


def uts_to_gmt(uts: int) -> str:
    return datetime.datetime.fromtimestamp(uts).strftime('%H:%M:%S on %d %b')


@dataclass
class AoCMember:
    """A dataclass to store information on AoC members in a Pythonic format."""

    id: int
    name: str
    stars: int
    local_score: int
    global_score: int
    days: list[AoCDay]

    def __post_init__(self) -> None:
        self.days.sort(key=lambda m: m.id)

    def report(self) -> None:
        title: str = f'Report for {self.name}'
        print(title)
        print(len(title) * '=')
        print()
        for day in self.days:
            day_title: str = f'Day {day.id}'
            print(day_title)
            print((len(day_title)) * '-')
            print('  Part 1:')
            print(f'    Time completed: {uts_to_gmt(day.part_one.time)}')

            print()

            print('  Part 2:')
            if not day.part_two:
                print('    Not completed.')
                continue

            print(f'    Time completed: {uts_to_gmt(day.part_two.time)}')
            print()
            duration = time.strftime(
                '%H hours, %M minutes, %S seconds.',
                time.gmtime(day.part_two.time - day.part_one.time),
            )
            print(f'  Difference: {duration}')
            print()

        print()


@dataclass
class AoCDay:
    """A dataclass to store information on an AoC member's daily metrics."""

    id: int
    part_one: AoCPart
    part_two: AoCPart | None = None

    def to_datetime(self):
        pass


@dataclass
class AoCPart:
    """A dataclass to store information on question parts"""

    id: int
    time: int


class AoCLeaderboard:
    """A class with helper methods for the AoC API."""

    def __init__(self, data: dict[str, Any]) -> None:
        self.year: int = int(data['event'])
        self.members: list[AoCMember] = self._parse_members(data=data['members'])

    def _parse_members(self, data: dict) -> list[AoCMember]:
        members: list[AoCMember] = []
        for _id, d in data.items():
            member = AoCMember(
                id=int(_id),
                name=d['name'],
                stars=d['stars'],
                local_score=d['local_score'],
                global_score=d['global_score'],
                days=self._parse_days(data=d['completion_day_level']),
            )
            members.append(member)

        return members

    def _parse_days(self, data: dict) -> list[AoCDay]:
        days: list[AoCDay] = []
        for _id, d in data.items():
            parts = self._parse_parts(data=d)
            parts.sort(key=lambda p: p.id)

            day = AoCDay(
                id=int(_id),
                part_one=parts[0],
                part_two=parts[1] if len(parts) == 2 else None,
            )
            days.append(day)
        return days

    def _parse_parts(self, data: dict) -> list[AoCPart]:
        parts: list[AoCPart] = []
        for _id, d in data.items():
            part = AoCPart(id=int(_id), time=d['get_star_ts'])
            parts.append(part)
        return parts


def main() -> int:
    DIRECTORY: str = os.path.dirname(__file__)
    with open(os.path.join(DIRECTORY, 'data', 'leaderboard.json')) as f:
        data: dict[str, Any] = json.load(f)

    leaderboard: AoCLeaderboard = AoCLeaderboard(data=data)

    for member in leaderboard.members:
        if member.name == 'sam4llis':
            member.report()

    return 0


if __name__ == '__main__':
    exit(main())
