#! /usr/bin/env python

from time import perf_counter
import argparse
from happy_num import get_dist_happy
import chalk

from colorama import init
init()


def get_args():
    # set up argument parser
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-r', type=float, default=1E06, help='Range to be calculated?')
    parser.add_argument(
        '-v', default=False, action='store_true', help="Verbose?"
    )
    args = parser.parse_args()
    args.r = int(args.r)
    return args


def format_dec(n):
    a, b = ('%E' % n).split('E')
    out = str(round(float(a.rstrip('0').rstrip('.')), 3))
    if b != '+00':
        out += 'e' + b
    return out


def main():
    args = get_args()

    # start main script
    print(chalk.green('Distinct Happy Number Range Counter\n'))
    print('Range:', chalk.red(args.r))
    time_start = perf_counter()  # start timer

    count = get_dist_happy(args.r, args.v)

    time_end = perf_counter()  # end timer
    time_delta = time_end - time_start
    print('Count Total: {count}'.format(count=chalk.cyan(count)))
    print('Calc Time (s): {}'.format(chalk.magenta(format_dec(time_delta))))


if __name__ == "__main__":
    main()
