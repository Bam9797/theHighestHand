class Deck():
    def _init__(self, cards=[1,2,3,4,5]):
        self.cards = cards
        
    def play(self, card):
        return self.cards.remove(card)
    
    def inHand(self):
        return self.cards
    
    