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
