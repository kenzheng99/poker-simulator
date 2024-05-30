from card import Card
from deck import Deck
from rank import Rank
from handValue import HandValue

class Hand:
    def __init__(self, cards):
        self.cards = sorted(cards);
        self.deck = Deck();           
        for card in cards:
            self.deck.remove(card);
        self.value = None;

    def __str__(self):
        return " ".join([str(card) for card in self.cards])

    def replace(self, indices):
        for i in indices:
            self.cards[i] = self.deck.draw();
        self.cards.sort();
        self.value = None;

    def calculateValue(self, enable_jacks=True):
        if self.value: 
            return self.value;

        if Hand.isRoyalFlush(self):
            self.value = HandValue.ROYAL_FLUSH;
        elif Hand.isStraightFlush(self):
            self.value = HandValue.STRAIGHT_FLUSH;
        elif Hand.isQuads(self):
            self.value = HandValue.QUADS;
        elif Hand.isFullHouse(self):
            self.value = HandValue.FULL_HOUSE;
        elif Hand.isFlush(self):
            self.value = HandValue.FLUSH;
        elif Hand.isStraight(self):
            self.value = HandValue.STRAIGHT;
        elif Hand.isTriplets(self):
            self.value = HandValue.TRIPLETS;
        elif Hand.isTwoPair(self):
            self.value = HandValue.TWO_PAIR;
        elif enable_jacks and Hand.isJacksOrBetter(self):
            self.value = HandValue.JACKS_OR_BETTER;
        elif Hand.isPair(self):
            self.value = HandValue.PAIR;
        else:
            self.value = HandValue.NONE;

        return self.value;

    def calculateScore(self):
        if not self.value:
            self.calculateValue();

        score_map = {
            HandValue.ROYAL_FLUSH: 5000,
            HandValue.STRAIGHT_FLUSH: 1500,
            HandValue.QUADS: 600,
            HandValue.FULL_HOUSE: 300,
            HandValue.FLUSH: 200,
            HandValue.STRAIGHT: 125,
            HandValue.TRIPLETS: 75,
            HandValue.TWO_PAIR: 40,
            HandValue.JACKS_OR_BETTER: 10,
            HandValue.PAIR: 0,
            HandValue.NONE: 0
        }

        return score_map[self.value];


    @staticmethod
    def fromString(handStr: str):
        cards = [Card.fromString(cardStr) for cardStr in handStr.split(' ')]
        return Hand(cards);

    @staticmethod
    def random():
        deck = Deck();
        return Hand(deck.draw(5));

    @staticmethod
    def isStraight(hand):
        # special case for ace high
        if (hand.cards[0].rank == Rank.fromString('A')
            and hand.cards[1].rank == Rank.fromString('T')
            and hand.cards[2].rank == Rank.fromString('J')
            and hand.cards[3].rank == Rank.fromString('Q')
            and hand.cards[4].rank == Rank.fromString('K')):
            return True;

        for i in range(1, 5):
            if hand.cards[i].rank.index - hand.cards[i-1].rank.index != 1:
                return False;
        return True;

    @staticmethod
    def isFlush(hand):
        suit = hand.cards[0].suit;
        for i in range(1, 5):
            if hand.cards[i].suit != suit:
                return False;
        return True;

    @staticmethod
    def isStraightFlush(hand):
        return Hand.isStraight(hand) and Hand.isFlush(hand);

    @staticmethod
    def isRoyalFlush(hand):
        return (hand.isStraightFlush(hand) 
                and hand.cards[0].rank == Rank.fromString('A') 
                and hand.cards[4].rank == Rank.fromString('K'));

    @staticmethod
    def isQuads(hand):
        return Hand.areAllRanksEqual(hand, [0, 1, 2, 3]) or Hand.areAllRanksEqual(hand, [1, 2, 3, 4]);

    @staticmethod
    def isFullHouse(hand):
        return (Hand.areAllRanksEqual(hand, [0, 1, 2]) and Hand.areAllRanksEqual(hand, [3, 4])
                or Hand.areAllRanksEqual(hand, [0, 1]) and Hand.areAllRanksEqual(hand, [2, 3, 4]));

    @staticmethod
    def isTriplets(hand):
        # careful, quads returns true
        return (Hand.areAllRanksEqual(hand, [0, 1, 2])
                or Hand.areAllRanksEqual(hand, [1, 2, 3])
                or Hand.areAllRanksEqual(hand, [2, 3, 4]));

    @staticmethod
    def isTwoPair(hand):
        pairs = Hand.getPairs(hand);
        if len(pairs) >= 2:
            return True;
        return False;

    @staticmethod
    def isJacksOrBetter(hand):
        pairs = Hand.getPairs(hand);
        return len(pairs) == 1 and (
                pairs[0] >= Rank.fromString('J') or pairs[0] == Rank.fromString('A'));

    @staticmethod
    def isPair(hand):
        pairs = Hand.getPairs(hand);
        return len(pairs) == 1;

    @staticmethod
    def areAllRanksEqual(hand, handIndices):
        for i in range(1, len(handIndices)):
            if (hand.cards[handIndices[i]].rank != hand.cards[handIndices[i-1]].rank):
                return False;
        return True;

    @staticmethod
    def getPairs(hand):
        pairs = set()
        for i in range(1, 5):
            if (hand.cards[i].rank == hand.cards[i-1].rank):
                pairs.add(hand.cards[i].rank);

        return list(pairs);


if __name__ == '__main__':
    print('hand.py');
    print(Hand([
        Card.fromString('Jh'),
        Card.fromString('Qh'),
        Card.fromString('Th'),
        Card.fromString('Ah'),
        Card.fromString('Kh'),
    ]))

    straightHand = Hand.fromString('5d 6h 7c 8s 9d');
    print(f'{straightHand} is straight: {Hand.isStraight(straightHand)}, score: {straightHand.calculateScore()}');

    flushHand = Hand.fromString('6h 9h Th Jh Kh');
    print(f'{flushHand} is flush: {Hand.isFlush(flushHand)}');

    straightFlushHand = Hand.fromString('Ts Js Qs Ks As');
    print(f'{straightFlushHand} is straight flush: {Hand.isStraightFlush(straightFlushHand)}');

    royalFlushHand = Hand.fromString('Ts Js Qs Ks As');
    print(f'{royalFlushHand} is royal flush: {Hand.isStraightFlush(royalFlushHand)}');

    quadsHand = Hand.fromString('3d 3c 3h 3s Ah');
    print(f'{quadsHand} is quads: {Hand.isQuads(quadsHand)}');

    fullHouseHand = Hand.fromString('Kh Kd Ks 4d 4s');
    print(f'{fullHouseHand} is full house: {Hand.isFullHouse(fullHouseHand)}');

    tripsHand = Hand.fromString('Ad 6d 6c 6h Ks');
    print(f'{tripsHand} is trips: {Hand.isTriplets(tripsHand)}');

    twoPairHand = Hand.fromString('3s 3d 8s 8h 9d');
    print(f'{twoPairHand} is two pair: {Hand.isTwoPair(twoPairHand)}');

    jackPairHand = Hand.fromString('Ad As Jd Kh 5d');
    print(f'{jackPairHand} is jack pair: {Hand.isJacksOrBetter(jackPairHand)}');

    pairHand = Hand.fromString('8d 8s 3d Kh 5d');
    print(f'{pairHand} is pair: {Hand.isPair(pairHand)}');

    print(Hand.fromString('5d 6h 7c 8s 9d').calculateValue())

    randomHand = Hand.random();
    print(f'{randomHand} is {randomHand.calculateValue()}')

    straightHand.replace([0, 2, 4]);
    print(f'after replace: {straightHand}')
