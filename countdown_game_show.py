from itertools import permutations, product
# https://www.reddit.com/r/dailyprogrammer/comments/6fe9cv/20170605_challenge_318_easy_countdown_game_show/


def formatted(nums, ops):
    result = [str(nums[0])]
    for op, b in zip(ops, nums[1:]):
        result.append(op)
        result.append(str(b))
    return " ".join(result)

answer_list = []

op_table = {
    "+": lambda x,y: x+y,
    "-": lambda x,y: x-y,
    "*": lambda x,y: x*y,
    "/": lambda x,y: x/y
}

number_list = [1, 3, 7, 6, 8, 3]
target_number = 250

for i in number_list:
    for perm in permutations(number_list):
        perm = list(perm)
        for ops in product("+-*/", repeat=len(perm) - 1):
            current_result = perm[0]
            for op, b in zip(ops, perm[1:]):
                current_result = op_table[op](current_result, b)
                if current_result == target_number:
                    if (formatted(perm, ops), current_result) not in answer_list:
                        answer = formatted(perm, ops), current_result
                        answer_list.append(answer)
                        print(answer)

print(answer_list)

