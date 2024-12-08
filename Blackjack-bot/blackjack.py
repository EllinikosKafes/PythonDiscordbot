# Blackjack logig
# Author Matheus Aires - Kaazeeb

import random

class Card:
    @staticmethod
    def get_suit(card: int) -> str:
        card = (card - 1) // 13
        
        match card:
            case 0:
                return "♦"
            case 1:
                return "♠"
            case 2:
                return "♥"
            case 3:
                return "♣"
            case _:
                return "♥"
    
    @staticmethod
    def get_value(card: int) -> str:
        card = (card - 1) % 13

        if card == 0:
            return "A"
        elif card < 10:
            return str(card)
        elif card == 10:
            return "J"
        elif card == 11:
            return "Q"
        elif card == 12:
            return "K"
    
    @staticmethod
    def print_face_down() -> None:
        card = (
            "┌─────────┐\n"
            "│░░░░░░░░░│\n"
            "│░░░░░░░░░│\n"
            "│░░░░░░░░░│\n"
            "│░░░░░░░░░│\n"
            "│░░░░░░░░░│\n"
            "└─────────┘"
        )
    
    @staticmethod
    def print(cards: tuple, is_dealer: bool) -> str:
        suits = list()
        values = list()

        for card in cards:
            suits.append(Card.get_suit(card))
            values.append(Card.get_value(card))
        
        lines = ["" for _ in range(7)]

        top = "┌─────────┐"
        bot = "└─────────┘"
        mid = "│         │"
        block = "│░░░░░░░░░│"

        for x in range(len(cards)):
            if not x and is_dealer:
                lines[0] += top
                lines[1] += block
                lines[2] += block
                lines[3] += block
                lines[4] += block
                lines[5] += block
                lines[6] += bot
                continue

            lines[0] += top
            lines[1] += f"│{values[x]}        │"
            lines[2] += mid
            lines[3] += f"│    {suits[x]}    │"
            lines[4] += mid
            lines[5] += f"│        {values[x]}│"
            lines[6] += bot
        
        return "\n".join(lines)
            

        



class Deck:
    def __init__(self):
        self.cards = list(range(1, 53))

    def shuffle(self):
        random.shuffle(self.cards)
    
    def draw(self):
        return self.cards.pop()

    @staticmethod
    def display_card(cards: tuple) -> None:
        pass

class Session:
    def __init__(self):
        return

if __name__ == '__main__':
    Card.print((10, 28), True)