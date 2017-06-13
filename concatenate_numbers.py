from itertools import permutations

def magic(numList):
    s = ''.join(map(str, numList))
    return int(s)

def find_small_and_large(lst):
    list_of_permutations = []
    for perm in permutations(lst):
        concat_number = magic(list(perm))
        list_of_permutations.append(concat_number)
    list_of_permutations.sort()
    smallest = list_of_permutations[0]
    largest = list_of_permutations[-1]
    return smallest, largest

list_of_numbers = [79, 82, 34, 83, 69]
print(find_small_and_large(list_of_numbers))
