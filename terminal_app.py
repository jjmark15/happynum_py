#! /usr/bin/env python

import argparse
from argparse import Namespace, ArgumentParser
from time import perf_counter

import chalk
from colorama import init as init_colorama

from happy_num import get_dist_happy

init_colorama()


def get_args() -> Namespace:
    # set up argument parser
    parser: ArgumentParser = argparse.ArgumentParser()
    parser.add_argument('-r',
                        type=float,
                        default=1E06,
                        help='Range to be calculated?')
    args: Namespace = parser.parse_args()
    args.r = int(args.r)
    return args


def format_dec(n: float) -> str:
    a, b = ('%E' % n).split('E')
    out: str = str(round(float(a.rstrip('0').rstrip('.')), 3))
    if b != '+00':
        out += 'e' + b
    return out


def main() -> None:
    args: Namespace = get_args()

    # start main script
    print(chalk.green('Distinct Happy Number Range Counter\n'))
    print('Range:', chalk.red(args.r))
    time_start: float = perf_counter()  # start timer

    count: int = get_dist_happy(args.r)

    time_end: float = perf_counter()  # end timer
    time_delta: float = time_end - time_start
    print('Count Total: {count}'.format(count=chalk.cyan(count)))
    print('Calc Time (s): {}'.format(chalk.magenta(format_dec(time_delta))))


if __name__ == "__main__":
    main()
