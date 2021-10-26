import os
import argparse
import re
from typing import Optional

import pexpect


class Game:
    def __init__(
        self,
        path: str,
        interpreter_path: str = "python3",
    ):
        self.path = path
        self.interpreter_path = interpreter_path
        self._delim = re.compile(r"^>>> $", re.M)
        path = path.replace(" ", "\\ ")
        self._game = pexpect.spawn(
            f"{interpreter_path} {path}",
            encoding="utf-8",
        )
        self.text = ""
        self.get_input()

    def create_game(self):
        pass

    def restart(self):
        """Restarts the game"""
        self.close()
        path = self.path.replace(" ", "\\ ")
        self._game = pexpect.spawn(
            f"{self.interpreter_path} {path}",
            encoding="utf-8",
        )
        self.text = ""
        self.get_input()

    def get_input(self) -> bool:
        if (
            index := self._game.expect(
                [self._delim, pexpect.EOF, pexpect.TIMEOUT], timeout=5
            )
        ) == 0:
            # if (index := self._game.expect([self._delim, pexpect.EOF])) == 0:
            self.text: str = self._game.before + self._game.after
        elif index == 1:
            self.text: str = self._game.before
        else:
            self.text = "Timeout error!"
            self.close()
            # raise RuntimeError("Game took too long")
        return index == 0

    def step(self, inp: Optional[str]) -> bool:
        if self.text is not None:
            self._game.sendline(inp)
        ret = self.get_input()
        if self.text.startswith(inp):
            self.text = self.text[len(inp) :]  # type: ignore
        return ret

    def close(self):
        try:
            self._game.kill(9)
        except Exception:  # pylint: disable=broad-except
            pass

    def is_alive(self):
        try:
            return self._game.isalive()
        except Exception:  # pylint: disable=broad-except
            return False

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-g", "--game", required=True, help="Path to the game")
    return parser.parse_args()

def main():
    args = parse_args()
    game = Game(
        # "games/Кочеркевич Вікторія_318670_assignsubmission_file_/gameghost.py",
        args.game,
        interpreter_path="python3",
    )
    print(game.text)
    # while game.step("Potato"):
    while game.step(input()):
        print(game.text)
    print("is alive:", game.is_alive())


if __name__ == "__main__":
    main()
