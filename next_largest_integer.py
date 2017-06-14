from itertools import permutations

# https://www.reddit.com/r/dailyprogrammer/comments/67q3s6/20170426_challenge_312_intermediate_next_largest/

integer = 1234

def next_largest(number):
    digits = [x for x in str(number)]
    perm = sorted(permutations(list(digits)))
    perm = [int(''.join(list(x))) for x in perm]
    return perm[perm.index(number) + 1]

print(next_largest(integer))