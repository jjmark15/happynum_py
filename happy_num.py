def is_first_iteration(n):
    prev = "0"

    for (i, curr) in enumerate(str(n)):
        if i > 0:
            if prev > curr:
                return False
        prev = curr
    return True


def square_sum(n):
    return sum([int(d)**2 for d in str(n)])


def ishappy(n):
    unhappy_markers = [89, 145, 42, 37, 58, 20, 4, 16]
    ss = n
    while True:
        ss = square_sum(ss)
        if ss in unhappy_markers:  # definitely not happy
            return False
        elif ss == 1:  # therefore happy
            return True


def get_dist_happy(r, verbose=False):
    count = 0
    range_gen = (i for i in range(1, r + 1)
                 if is_first_iteration(i))  # save memory with generator
    for i in range_gen:
        if ishappy(i):
            print(i) if verbose else 0
            count += 1
    return count
