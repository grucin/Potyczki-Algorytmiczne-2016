#!/usr/bin/env python

import argparse

LETTERS = ('a', 'b', 'c')
LETTERS_COUNT = len(LETTERS)


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('max_length', type=int)
    parser.add_argument('position', type=int)

    return parser.parse_args()


def slo(max_length, position):
    max_set = LETTERS_COUNT * ((LETTERS_COUNT - 1) ** max_length - 1)
    if max_set < position:
        return 'NIE'

    letters = []
    prev = 0
    for l in LETTERS:
        l_position = prev + 1
        if position == l_position:
            return l
        last = prev + (LETTERS_COUNT - 1) ** max_length - 1
        if position <= last:
            letters.append((l, l_position))
            break
        prev = last


    for depth in xrange(1, max_length):
        prev = letters[-1][1]
        for l in LETTERS:
            if l == letters[-1][0]:
                continue
            l_position = prev + 1
            if position == l_position:
                letters.append((l, l_position))
                break
            last = l_position + (LETTERS_COUNT - 1) * (
                (LETTERS_COUNT - 1) ** (max_length - depth - 1) - 1)
            if position <= last:
                letters.append((l, l_position))
                break
            prev = last

        if position == letters[-1][1]:
            break

    return ''.join(l for l, _ in letters)


def main():
    args = get_args()
    print slo(max_length=args.max_length, position=args.position)


if __name__ == '__main__':
    main()