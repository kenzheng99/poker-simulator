import random 

"""
Class representing a card's rank (1-10, JQKA)
"""
class Rank:
    index2rank = {
        0: 'A',
        1: '2',
        2: '3',
        3: '4',
        4: '5',
        5: '6',
        6: '7',
        7: '8',
        8: '9',
        9: 'T',
        10: 'J',
        11: 'Q',
        12: 'K',

    };
    rank2index = {v: k for k, v in index2rank.items()};

    def __init__(self, index):
        self.index = index;


    def __str__(self):
        return Rank.index2rank[self.index];

    def __eq__(self, other):
        return self.index == other.index;
    
    def __lt__(self, other):
        return self.index < other.index;

    def __le__(self, other):
        return self.index <= other.index;

    def __gt__(self, other):
        return self.index > other.index;

    def __ge__(self, other):
        return self.index >= other.index;

    def __hash__(self):
        return hash(self.index);

    @staticmethod
    def fromString(rankStr):
        rankStrUpdated = rankStr.upper();
        if rankStrUpdated not in Rank.rank2index.keys():
            raise ValueError(f"cannot parse rank: {rankStr}");
        return Rank(Rank.rank2index[rankStrUpdated]);

    @staticmethod
    def random():
        return Rank(random.randint(0, 12));


if __name__ == '__main__':
    print(Rank(3));
    print(Rank.fromString('K'));
    print(Rank(11) == Rank(11))
    print(Rank(10) < Rank(9))
    print(Rank.random())


