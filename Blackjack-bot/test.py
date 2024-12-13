## Class for converting cards in
## the format of a tuple of ints
## to multiline string or strings
## Author Matheus Aires - Kaazeeb

class Card:
    @staticmethod
    def to_string(cards: tuple, is_face_down: bool = True) -> list[str]:
        '''
            Convert card values to its string representation
        '''
        cards_str_list = [(Card._get_value(card), Card._get_suit(card))
                           for card in cards]
        
        # Generate first card, possibily face down
        lines = Card._generate_card(cards_str_list[0], is_face_down)

        answer = ""

        # Append new cards to the str, at most 3 cards side by side
        for i in range(1, len(cards)):
            string_card = Card._generate_card(cards_str_list[i])

            for j in range(len(lines)):
                lines[j] += string_card[j]
            
            if not (i+1) % 3 or i == len(cards) - 1:
                answer += Card._lines_to_str(lines) + '\n'
                lines = [""] * 7
        
        return answer
    
    @staticmethod
    def _get_suit(card: int) -> str:
        card = card // 13
        
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
    def _get_value(card: int) -> str:
        card = card % 13

        if card == 0:
            return "A"
        elif card < 10:
            return str(card + 1)
        elif card == 10:
            return "J"
        elif card == 11:
            return "Q"
        elif card == 12:
            return "K"
        
    @staticmethod
    def _generate_card(card: tuple[str, str], 
                      is_face_down: bool = False) -> list[str]:
        '''
        Generate a card in one of the following formats:
        ┌─────────┐    ┌─────────┐
        │░░░░░░░░░│    │A        │
        │░░░░░░░░░│    │         │
        │░░░░░░░░░│    │    ♣    │
        │░░░░░░░░░│    │         │
        │░░░░░░░░░│    │        A│
        └─────────┘    └─────────┘
        card tuple(value, suite)
        '''
        lines = ["" for _ in range(7)]

        top =   "┌─────────┐"
        bot =   "└─────────┘"
        mid =   "│         │"
        block = "│░░░░░░░░░│"

        lines[0] = top
        lines[6] = bot

        if is_face_down:
            for i in range(1, 6):
                lines[i] = block

            return lines

        if len(card[0]) == 2:
            lines[1] += f"│{card[0]}       │"
            lines[5] += f"│       {card[0]}│"
        else:
            lines[1] += f"│{card[0]}        │"
            lines[5] += f"│        {card[0]}│"

        lines[2] += mid
        lines[3] += f"│    {card[1]}    │"
        lines[4] += mid

        return lines
    
    @staticmethod
    def _lines_to_str(lines: list[str]) -> str:
        return "\n".join(lines)


class Player:
    def __init__(self):
        self.hand = []

    def receive(self, card: int):
        self.hand.append(card)

    def show(self):
        return Card.to_string(tuple(self.hand))
    
    def evaluate(self):
        has_ace = False
        total = 0

        for card in self.hand:
            val = (card % 13) + 1

            if val == 1 and not has_ace:
                has_ace = True
                continue

            if val >= 10:
                total += 10
            else:
                total += val
        
        if has_ace:
            if total + 11 > 21:
                total += 1
            else:
                total += 11
        
        if total > 21:
            return -1
        return total


if __name__ == '__main__':
    play1 = Player()
    play1.receive(0)
    play1.receive(0)
    play1.receive(0)
    play1.receive(10)
    print(play1.evaluate())