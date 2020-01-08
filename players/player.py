from typing import Tuple
from .player_state import PlayerState


class Player:
    def get_state(self) -> PlayerState:
        pass

    def send_state(self, state: PlayerState, reveal=False):
        pass

    def get_guess(self) -> Tuple[int, int]:
        pass

    def send_guess(self, guess: Tuple[int, int]):
        pass

    def close(self):
        pass
