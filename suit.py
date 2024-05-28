import random 

"""
Class representing a card's suit (diamond/club/heart/spade)
"""
class Suit:
    index2suit = {
        0: 'd',
        1: 'c',
        2: 'h',
        3: 's'
    };
    suit2index = {v: k for k, v in index2suit.items()};
    index2print = {
        0: '♦',
        1: '♣',
        2: '♥',
        3: '♠',
    }

    def __init__(self, index):
        self.index = index;

    def __str__(self):
        return Suit.index2print[self.index];

    def __eq__(self, other):
        return self.index == other.index;
    
    def __lt__(self, other):
        return self.index < other.index;

    @staticmethod
    def fromString(suitStr):
        suitStrUpdated = suitStr.lower();
        if suitStrUpdated not in Suit.suit2index.keys():
            raise ValueError(f"cannot parse suit: {suitStr}");
        return Suit(Suit.suit2index[suitStrUpdated]);

    @staticmethod
    def random():
        return Suit(random.randint(0, 3))


if __name__ == '__main__':
    print(Suit(3));
    print(Suit.fromString('d'));
    print(Suit(3) == Suit(3))
    print(Suit(3) < Suit(2))
    print(Suit.random())


