# https://www.reddit.com/r/dailyprogrammer/comments/68oda5/20170501_challenge_313_easy_subset_sum/

numlist = [1, 2, 12, 4, 5, 3]

def find_sum_zero(inlist):
    for number in inlist:
        if number*-1 in inlist:
            return True
        else:
            return False

print(find_sum_zero(numlist))