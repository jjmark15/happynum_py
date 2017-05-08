import operator


def square_sum(n):
    ss = 0
    for digit in str(n):
        ss += int(digit)**2
    return ss


def ishappy(n):
    ss = square_sum(n)
    c = 1
    dups = {4: 0, 16: 0, 20: 0, 37: 0, 42: 0, 58: 0, 89: 0, 145: 0}
    while 0 in dups.values():
        ss = square_sum(ss)
        if ss == 1: # therefore happy
            return {}
            break
        if ss in dups.keys() and dups[ss] == 0:
            dups[ss] = c
        c += 1
    return dups


dups = {4: 0, 16: 0, 20: 0, 37: 0, 42: 0, 58: 0, 89: 0, 145: 0}
r = 100 # number range
for n in range(1, r + 1):
    new = ishappy(n)
    for dup in new.keys():
        if dups[dup] != 0:
            dups[dup] += new[dup]/r
        else:
            dups[dup] = new[dup]/r

print('For a number range of {n}:\n'.format(n=r))
print('Indicator vs average iterations until hit:')
min = min(dups.values())
for dup in dups.keys():
    if dups[dup] == min:
        min = dup
    print(dup, round(dups[dup],1))
print('\nEarliest indicator is', min)
