import argparse
from collections import Counter
from tqdm import tqdm

from hand import Hand


def print_counter(counter, total_iters):
    for k, v in counter.most_common():
        print(f"{str(k)}: {v} ({v * 100 / total_iters:.04f}%)")


def simulate_no_draw(num_iters):
    counter = Counter()
    score_total = 0
    for i in tqdm(range(0, num_iters)):
        hand = Hand.random()
        handValue = hand.calculateValue(enable_jacks=True)
        # print(f'{hand}: {handValue}')

        counter[handValue] += 1
        score_total += hand.calculateScore()

    print_counter(counter, num_iters)
    print(f"EV: {score_total / num_iters}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--num-iters", type=int, default=10000)
    args = parser.parse_args()
    simulate_no_draw(args.num_iters)
