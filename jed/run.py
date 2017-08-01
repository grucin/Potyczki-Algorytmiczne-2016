#!/usr/bin/env python

import argparse

from jed import jed


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('n', type=int)

    return parser.parse_args()


def main():
    args = get_args()
    print jed(args.n)


if __name__ == '__main__':
    main()