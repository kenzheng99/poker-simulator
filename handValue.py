from enum import Enum


class HandValue(Enum):
    ROYAL_FLUSH = "royal_flush"
    STRAIGHT_FLUSH = "straight_flush"
    QUADS = "quads"
    FULL_HOUSE = "full_house"
    FLUSH = "flush"
    STRAIGHT = "straight"
    TRIPLETS = "triplets"
    TWO_PAIR = "two_pair"
    JACKS_OR_BETTER = "jacks_or_better"
    PAIR = "pair"
    NONE = "none"
