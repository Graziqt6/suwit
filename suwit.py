# v0.1.0
# { "Depends": "py-genlayer:1jb45aa8ynh2a9c9xn3b7qqh8sm5q93hwfp7jqmwsfhh8jpz09h6" }
from genlayer import *

import json


class Suwit(gl.Contract):
    player1: str
    player2: str
    move1: str
    move2: str
    winner: str

    def __init__(self):
        self.player1 = ""
        self.player2 = ""
        self.move1 = ""
        self.move2 = ""
        self.winner = ""

    @gl.public.write
    def join_game(self, player_name: str) -> None:
        if self.player1 == "":
            self.player1 = player_name
        elif self.player2 == "":
            self.player2 = player_name

    @gl.public.write
    def submit_move(self, player_name: str, move_description: str) -> None:
        if player_name == self.player1:
            self.move1 = move_description
        elif player_name == self.player2:
            self.move2 = move_description

    @gl.public.write
    def judge(self) -> None:
        prompt = f"""
You are the judge of Suwit, an ancient Indonesian hand game.
The three possible moves are:
- Gajah (Elephant): beats Manusia, loses to Semut
- Manusia (Human): beats Semut, loses to Gajah
- Semut (Ant): beats Gajah, loses to Manusia

Player 1 ({self.player1}) described their move as: {self.move1}
Player 2 ({self.player2}) described their move as: {self.move2}

Interpret each description and map it to Gajah, Manusia, or Semut.
Determine the winner. If both chose the same move, winner is draw.

Respond using ONLY the following format:
{{
"player1_move": str,
"player2_move": str,
"winner": str,
"reason": str
}}
It is mandatory that you respond only using the JSON format above,
nothing else. Don't include any other words or characters,
your output must be only JSON without any formatting prefix or suffix.
This result should be perfectly parseable by a JSON parser without errors.
"""

        def get_result():
            result = gl.nondet.exec_prompt(prompt)
            result = result.replace("```json", "").replace("```", "")
            return result

        result = gl.eq_principle.prompt_comparative(
            get_result, "The winner value must match"
        )
        parsed = json.loads(result)
        self.winner = parsed["winner"]

    @gl.public.view
    def get_game_state(self) -> str:
        return self.player1 + " vs " + self.player2 + " | Winner: " + self.winner

    @gl.public.write
    def reset_game(self) -> None:
        self.player1 = ""
        self.player2 = ""
        self.move1 = ""
        self.move2 = ""
        self.winner = ""
