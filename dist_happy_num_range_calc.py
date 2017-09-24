from time import clock
from mypackage.mymodule import num_input


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


def get_dist_happy(r):
    count = 0
    range_gen = (i for i in range(1, r) if is_first_it(i)
        )  # save memory with generator
    for i in range_gen:
        if ishappy(i):
            count += 1
    return count


def main():
    print('Distinct Happy Number Range Counter\n')
    r = num_input('Number Range: ')  # define range
    time_start = clock()  # start timer
    count = get_dist_happy(r)

    time_end = clock()  # end timer
    time_delta = time_end - time_start
    print('Count Total: {count}'.format(count=count))
    print('Calc Time: {}s'.format(round(time_delta, 5)))
    input()


if __name__ == "__main__":
    main()
