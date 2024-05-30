import sys
from collections import Counter
from tqdm import tqdm
import argparse
from hand import Hand
from handValue import HandValue


def print_counter(counter, total_iters):
    for k, v in counter.most_common():
        print(f"{str(k)}: {v} ({v * 100 / total_iters:.04f}%)")


def replace2hold(replace_indices):
    return {0, 1, 2, 3, 4} - set(replace_indices)


def simulate_replacements(cards, num_iters, verbose=False):
    ev_counter = Counter()
    replacement_combinations = [
        (),
        (0,),
        (1,),
        (2,),
        (3,),
        (4,),
        (0, 1),
        (0, 2),
        (0, 3),
        (0, 4),
        (1, 2),
        (1, 3),
        (1, 4),
        (2, 3),
        (2, 4),
        (3, 4),
        (0, 1, 2),
        (0, 1, 3),
        (0, 1, 4),
        (0, 2, 3),
        (0, 2, 4),
        (0, 3, 4),
        (1, 2, 3),
        (1, 2, 4),
        (1, 3, 4),
        (2, 3, 4),
        (0, 1, 2, 3),
        (0, 1, 2, 4),
        (0, 1, 3, 4),
        (0, 2, 3, 4),
        (1, 2, 3, 4),
        (0, 1, 2, 3, 4),
    ][::-1]
    for combination in tqdm(replacement_combinations, disable=verbose):
        ev = simulate_replacement(cards, combination, num_iters, verbose)
        ev_counter[combination] = ev

    hand = Hand.fromString(cards)
    print("*****************************")
    print("*--------- RESULTS ---------*")
    print("*****************************")
    print(f"hand: {hand}")
    for replace_indices, ev in ev_counter.most_common():
        hold_indices = replace2hold(replace_indices)
        hold_str = " ".join([str(hand.cards[i]) for i in hold_indices])
        print(f"ev: {ev} \t hold: {hold_str}")


def simulate_replacement(cards, replace_indices, num_iters, verbose=False):
    counter = Counter()
    score_total = 0
    for i in tqdm(range(0, num_iters), disable=not verbose):
        hand = Hand.fromString(cards)
        hand.replace(replace_indices)
        handValue = hand.calculateValue(enable_jacks=True)
        counter[handValue] += 1
        score_total += hand.calculateScore()

    ev = score_total / num_iters
    if verbose:
        hand = Hand.fromString(cards)
        hold_indices = replace2hold(replace_indices)
        hold_str = " ".join([str(hand.cards[i]) for i in hold_indices])
        print(f"hand: {hand}, hold: {hold_str}")
        print_counter(counter, num_iters)
        print(f"ev: {ev}")

    return ev


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--num_iters", type=int, default=10000)
    parser.add_argument("-v", "--verbose", action="store_true")
    parser.add_argument("card1")
    parser.add_argument("card2")
    parser.add_argument("card3")
    parser.add_argument("card4")
    parser.add_argument("card5")
    args = parser.parse_args()
    cards = f"{args.card1} {args.card2} {args.card3} {args.card4} {args.card5}"
    simulate_replacements(cards, args.num_iters, args.verbose)
