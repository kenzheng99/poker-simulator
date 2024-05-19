from card import Card

class Hand:
    def __init__(self, cards: list[Card]):
        self.cards = sorted(cards);

    def __str__(self):
        return " ".join([str(card) for card in self.cards])

    def calculateValue(self):
        if Hand.isStraight(self):
            return "straight";
        return "none";

    @staticmethod
    def isStraight(hand):
        for i in range(1, 5):
            if hand.cards[i].rank - hand.cards[i].rank != 1:
                return False;
        return True;


    @staticmethod
    def fromString(handStr: str):
        cards = [Card(cardStr[0], cardStr[1]) for cardStr in handStr.split(' ')]
        return Hand(cards);

if __name__ == '__main__':
    print('hand.py');
    print(Hand([
        Card('J','h'),
        Card('Q','h'),
        Card('T','h'),
        Card('A','h'),
        Card('K','h'),
    ]))

    print(Hand.fromString('5d 6h 7c 8s 9d'))
    print(Hand.fromString('5d 6h 7c 8s 9d').calculateValue())

        
