class Deck():
    def __init__(self, cards):
        self.cards = cards
        
    def play(self, card):
        return self.cards.remove(card)
    
    def inHand(self):
        return self.cards
    
    