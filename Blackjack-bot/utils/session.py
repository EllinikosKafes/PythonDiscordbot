'''
    Main game logic and session stats
    Author: Matheus Aires - Kaazeeb
    2024
'''

from utils.game_util import *

class Game:
    def __init__(self):
        # 0 waiting for deal comm and 1 waiting for hit or stand
        self.state = 0
        self._deck = Deck()
        self._dealer = Dealer()
        self._player = Player()
    
    def deal(self):
        self._deck.is_time_to_shuffle()

        for i in range(2):
            self._dealer.receive(self._deck.draw())
            self._player.receive(self._deck.draw())
        
        self.state = 1

        msg_1 = self.quote(self._dealer.show())
        msg_2 = self.quote(self._player.show())

        return msg_1 + msg_2

    def player_hit(self):
        p_score = self._player.evaluate()
        if p_score == 21:
            return
        
        self._player.receive(self._deck.draw())
        p_score = self._player.evaluate()

        if p_score > 21:
            pass
    
    def quote(self, string):
        return "```" + string + "```"


class Session:
    def __init__(self):
        self.games = 0
        self.score = 0
        self.game = Game()

if __name__ == '__main__':
    g = Game()
    print(g.deal())