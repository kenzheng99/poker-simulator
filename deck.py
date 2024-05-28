import random

from card import Card

class Deck:
    def __init__(self):
        self.deck = list(range(0, 52));

    def draw(self, num=1):
        choices = []
        for i in range(num):
            choice = random.choice(self.deck)
            self.deck.remove(choice)
            choices.append(Card(choice))
        return choices[0] if num == 1 else choices;

    def remove(self, card):
        self.deck.remove(card.index)

if __name__ == '__main__':
    deck = Deck();
    print(deck.deck);
    print([str(x) for x in deck.draw(5)]);
    print(deck.deck);

