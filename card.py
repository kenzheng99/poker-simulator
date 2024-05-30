import random

from rank import Rank
from suit import Suit


class Card:
    def __init__(self, index):
        self.index = index
        self.rank = Rank(index % 13)
        self.suit = Suit(index // 13)

    def __str__(self):
        return str(self.rank) + str(self.suit)

    def __eq__(self, other):
        return self.rank == other.rank and self.suit == other.suit

    def __lt__(self, other):
        if self.rank == other.rank:
            return self.suit < other.suit
        return self.rank < other.rank

    @staticmethod
    def fromString(cardStr: str):
        cardStrUpdated = cardStr.replace("10", "T")  # special case for handling tens
        if len(cardStrUpdated) != 2:
            raise ValueError(f"can't parse card: {cardStr}")
        try:
            rank = Rank.fromString(cardStrUpdated[0])
            suit = Suit.fromString(cardStrUpdated[1])
        except ValueError:
            raise ValueError(f"can't parse card: {cardStr}")

        index = suit.index * 13 + rank.index
        return Card(index)

    @staticmethod
    def random():
        return Card(random.randint(0, 52))


if __name__ == "__main__":
    print("card.py")
    print(Card(12))
    print(Card.fromString("As"))
    print(Card.fromString("Ad") == Card.fromString("Ad"))
    print(Card.fromString("5h") < Card.fromString("6s"))
    print(Card.random())
