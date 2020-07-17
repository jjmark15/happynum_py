from math import pow
from typing import List, Iterator


def is_first_iteration(n: int) -> bool:
    prev: str = "0"

    for (i, curr) in enumerate(str(n)):
        if i > 0:
            if prev > curr:
                return False
        prev = curr
    return True


def square_sum(n: int) -> int:
    ss: float = 0
    val: int = 0 + n

    while val > 0:
        ss += pow((val % 10), 2)
        val = int(val / 10)
    return int(ss)


def is_happy(n: int) -> bool:
    unhappy_markers: List[int] = [89, 145, 42, 37, 58, 20, 4, 16]
    ss: int = n

    while True:
        ss = int(square_sum(ss))
        if ss in unhappy_markers:  # definitely not happy
            return False
        elif ss == 1:  # therefore happy
            return True


def get_dist_happy(r: int) -> int:
    count: int = 0
    happy_nums: Iterator[int] = (1 for i in range(1, r + 1)
                                 if is_first_iteration(i) & is_happy(i))

    return sum(happy_nums)
