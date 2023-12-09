import re
from dataclasses import dataclass
from pathlib import Path

input = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""

input = Path("input02").read_text()
#  only 12 red cubes, 13 green cubes, and 14 blue cubes

MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14


@dataclass
class Draw:
    blue: int = 0
    red: int = 0
    green: int = 0

    def is_possible(self) -> bool:
        return self.red <= MAX_RED and self.green <= MAX_GREEN and self.blue <= MAX_BLUE


@dataclass
class Game:
    id: int
    draws: list[Draw]

    def is_possible(self) -> bool:
        for draw in self.draws:
            if not draw.is_possible():
                return False
        return True

    def get_power(self) -> int:
        reds = max(draw.red for draw in self.draws)
        greens = max(draw.green for draw in self.draws)
        blues = max(draw.blue for draw in self.draws)
        return reds * blues * greens


def get_game_from_string(s: str) -> Game:
    id_part, draws = s.split(":")
    id = int(re.findall(r"\d+", id_part)[0])
    _draws = []
    for draw in draws.split(";"):
        blue, red, green = 0, 0, 0
        for ball in draw.split(", "):
            match ball.split():
                case [count, "blue"]:
                    blue = int(count)
                case [count, "red"]:
                    red = int(count)
                case [count, "green"]:
                    green = int(count)
        _draw = Draw(blue, red, green)
        _draws.append(_draw)

    return Game(id, _draws)

totals = 0

for row in input.splitlines():
    #print(row)
    game = get_game_from_string(row)
    #print(game)
    #for draw in game.draws:
        #print(draw)
        #print(draw.is_possible())
    #if game.is_possible():
    totals += game.get_power()
    #print(game.is_possible(), game.id)

print(totals)
