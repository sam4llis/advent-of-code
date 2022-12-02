#!/usr/bin/env python3

import os


class EOutcome:
    WIN: int = 6
    DRAW: int = 3
    LOSS: int = 0


class EShape:
    ROCK: int = 1
    PAPER: int = 2
    SCISSORS: int = 3


# (OPPONENT) A = ROCK, B = PAPER, C = SCISSORS
# X = ROCK, Y = PAPER, Z = SCISSORS
OUTCOME_A = {
    'AX': EShape.ROCK + EOutcome.DRAW,
    'AY': EShape.PAPER + EOutcome.WIN,
    'AZ': EShape.SCISSORS + EOutcome.LOSS,
    'BX': EShape.ROCK + EOutcome.LOSS,
    'BY': EShape.PAPER + EOutcome.DRAW,
    'BZ': EShape.SCISSORS + EOutcome.WIN,
    'CX': EShape.ROCK + EOutcome.WIN,
    'CY': EShape.PAPER + EOutcome.LOSS,
    'CZ': EShape.SCISSORS + EOutcome.DRAW,
}

# (OPPONENT) A = ROCK, B = PAPER, C = SCISSORS
# X = LOSS, Y = DRAW, Z = WIN.
OUTCOME_B = {
    'AX': EOutcome.LOSS + EShape.SCISSORS,
    'AY': EOutcome.DRAW + EShape.ROCK,
    'AZ': EOutcome.WIN + EShape.PAPER,
    'BX': EOutcome.LOSS + EShape.ROCK,
    'BY': EOutcome.DRAW + EShape.PAPER,
    'BZ': EOutcome.WIN + EShape.SCISSORS,
    'CX': EOutcome.LOSS + EShape.PAPER,
    'CY': EOutcome.DRAW + EShape.SCISSORS,
    'CZ': EOutcome.WIN + EShape.ROCK,
}


def main() -> int:
    DIRECTORY: str = os.path.dirname(__file__)
    with open(os.path.join(DIRECTORY, 'data', 'test.txt')) as f:
        data: list[str] = [line.strip('\n').replace(' ', '') for line in f.readlines()]

    score1: int = 0
    score2: int = 0
    for event in data:
        score1 += OUTCOME_A[event]
        score2 += OUTCOME_B[event]

    print(score1)
    print(score2)
    return 0


if __name__ == '__main__':
    exit(main())
