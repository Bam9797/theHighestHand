class Deck():
    def _init__(self):
        self.cards = []
        self.build()
    def play(self, card):
        return self.cards.remove(card)
    def inHand(self):
        return self.cards
    