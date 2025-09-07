from dataclasses import dataclass
from enum import Enum
from typing import Optional

MAX_POLICIES_ON_BOARD = 5

class Role(Enum):
    LIBERAL=0
    FASCIST=1
    HITLER=2
    PRESIDENT=3
    CHANCELLOR=4

class RoundState(Enum):
    CHANCELLOR_CHOOSING=0
    LEGITIMANCY_VOTE=1
    POLICY_PICKING=2
    POLICY_IMPLEMENTATION=3
    DISCUSSION=4

@dataclass
class Deck:
    """
    Represents the policy card deck. Contains a number of fascist and liberal policies
    This is just two counters, pretty meaningless tbh
    """
    fascist_cards_count: int
    liberal_cards_count: int

class PolicyBoard:
    """
    Represents how many policies have been passed
    """
    fascist_policies_passed: int
    liberal_policies_passed: int

    def resolve_effects(self):
        # depending on how many policies have been passed
        # effects may need resolution
        # put those here
        pass

class Player:
    """
    Represents a single player
    TODO: hook up to a layer which can drive this logic
    """
    roles: list[Role]

class Game:
    """
    Represents the complete game setup
    """
    # General game info
    players: list[Player]
    draw_deck: Deck
    board: PolicyBoard
    rounds: int
    current_round_state: RoundState

    # Per round information
    current_president: Player
    current_chancellor: Optional[Player]

players = []

def game_loop(game: Game):
    [president] = [player for player in game.players if Role.PRESIDENT in player.roles]
    game.current_round_state = RoundState.CHANCELLOR_CHOOSING
    # TODO: ask the player who is president for chancellor (need a clean way to ask for this)
    game.current_round_state = RoundState.LEGITIMANCY_VOTE
    # TODO: ask all players to vote on legitimacy of the government
    [chancellor] = [player for player in game.players if Role.CHANCELLOR in player.roles]
    if Role.HITLER in chancellor.roles:
        print("Fascists win!");
        return
    game.current_round_state = RoundState.POLICY_PICKING
    # TODO: ask the chancellor to pick up three policies and discard one and pass to the president
    game.current_round_state = RoundState.POLICY_IMPLEMENTATION
    # TODO: ask the president to choose one policy of the given two (need a clean way to resolve this hand)
    # TODO: alter the policy board to reflect the president's choice
    if game.board.liberal_policies_passed >= MAX_POLICIES_ON_BOARD:
        print("Liberals win!")
        return
    game.current_round_state = RoundState.DISCUSSION
    # TODO: simulate discussion somehow
    game.board.resolve_effects()
    