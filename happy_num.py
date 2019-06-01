from math import pow


def is_first_iteration(n: int):
    prev: str = "0"

    for (i, curr) in enumerate(str(n)):
        if i > 0:
            if prev > curr:
                return False
        prev = curr
    return True


def square_sum(n: int):
    ss = 0
    val = 0 + n

    while val > 0:
        ss += pow((val % 10), 2)
        val: int = int(val/10)
    return ss


def ishappy(n: int):
    unhappy_markers = [89, 145, 42, 37, 58, 20, 4, 16]
    ss = n
    while True:
        ss = square_sum(ss)
        if ss in unhappy_markers:  # definitely not happy
            return False
        elif ss == 1:  # therefore happy
            return True


def get_dist_happy(r: int, verbose: bool = False):
    count = 0
    range_gen = (i for i in range(1, r + 1)
                 if is_first_iteration(i))  # save memory with generator
    for i in range_gen:
        if ishappy(i):
            print(i) if verbose else 0
            count += 1
    return count
