from time import clock
from mypackage.mymodule import num_input


def square_sum(n):
    ss = 0
    for digit in str(n):
        ss += int(digit)**2
    return ss


def ishappy(n):
    ss = square_sum(n)
    while True:
        ss = square_sum(ss)
        # if ss == 89 or ss == 0: # either of these indicates not happy
        if ss in [89, 145, 42, 37, 58, 20, 4, 16]: # this turns out to be faster
            return False
            break
        elif ss == 1: # therefore happy
            return True
            break


def get_dist_happy(r):
    happy_numbers = []
    count = 0

    # cycle through range
    for i in range(1, r + 1):
        # sort number digit order
        i = int(''.join(sorted([d for d in str(i)])))
        if i not in happy_numbers: # check is distinct
            if ishappy(i):
                happy_numbers.append(i)
                count += 1
    return count, happy_numbers


def main():
    print('Distinct Happy Number Range Counter\n')
    # define range
    r = num_input('Number Range: ')
    time_start = clock() # start timer
    count, nums = get_happy(r)

    time_end = clock() # end timer
    time_delta = time_end - time_start
    print('Count Total: {count}'.format(count=count))
    print('Calc Time: {} s'.format(round(time_delta,5)))
    p = input('See number list? (y): ')
    if p == 'y':
        for n in nums:
            print(n)
        input()


if __name__ == "__main__":
    main()
