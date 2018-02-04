from time import clock
import argparse


def is_first_it(n):
    ascending = int("".join(sorted(str(n))))
    if n == ascending:
        return True
    else:
        return False


def square_sum(n):
    ss = 0
    for digit in str(n):
        ss += int(digit)**2
    return ss


def ishappy(n):
    ss = n
    while True:
        ss = square_sum(ss)
        if ss in [89, 145, 42, 37, 58, 20, 4, 16]:
            return False
        elif ss == 1:  # therefore happy
            return True


def get_dist_happy(r, verbose=False):
    count = 0
    range_gen = (i for i in range(1, r + 1)
                 if is_first_it(i))  # save memory with generator
    for i in range_gen:
        if ishappy(i):
            if verbose is True:
                print(i)
            count += 1
    return count


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
    print('Distinct Happy Number Range Counter\n')
    print('Range:', args.r)
    time_start = clock()  # start timer

    count = get_dist_happy(args.r, args.v)

    time_end = clock()  # end timer
    time_delta = time_end - time_start
    print('Count Total: {count}'.format(count=count))
    print('Calc Time: {}s'.format(format_dec(time_delta)))


if __name__ == "__main__":
    main()
    input('\nEnter to close...')
