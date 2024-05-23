from card import Card
from deck import Deck
from rank import Rank
from handValue import HandValue

class Hand:
    def __init__(self, cards: list[Card]):
        self.cards = sorted(cards);
        self.deck = Deck();

    def __str__(self):
        return " ".join([str(card) for card in self.cards])

    def calculateValue(self, enable_jacks=True):
        if Hand.isRoyalFlush(self):
            return HandValue.ROYAL_FLUSH;
        if Hand.isStraightFlush(self):
            return HandValue.STRAIGHT_FLUSH;
        if Hand.isQuads(self):
            return HandValue.QUADS;
        if Hand.isFullHouse(self):
            return HandValue.FULL_HOUSE;
        if Hand.isFlush(self):
            return HandValue.FLUSH;
        if Hand.isStraight(self):
            return HandValue.STRAIGHT;
        if Hand.isTriplets(self):
            return HandValue.TRIPLETS;
        if Hand.isTwoPair(self):
            return HandValue.TWO_PAIR;
        if enable_jacks and Hand.isJacksOrBetter(self):
            return HandValue.JACKS_OR_BETTER;
        if Hand.isPair(self):
            return HandValue.PAIR;
        return HandValue.NONE;


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
        return len(pairs) == 1 and pairs[0] >= Rank.fromString('J');

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
    print(f'{straightHand} is straight: {Hand.isStraight(straightHand)}');

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

    jackPairHand = Hand.fromString('Jd Js Ad Kh 5d');
    print(f'{jackPairHand} is jack pair: {Hand.isJacksOrBetter(jackPairHand)}');

    pairHand = Hand.fromString('8d 8s 3d Kh 5d');
    print(f'{pairHand} is pair: {Hand.isPair(pairHand)}');

    print(Hand.fromString('5d 6h 7c 8s 9d').calculateValue())

    randomHand = Hand.random();
    print(f'{randomHand} is {randomHand.calculateValue()}')

        
