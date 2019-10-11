'''
Your function should take in a signle parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):
    if len(word) == 0 or "th" not in word:
        return 0
    return 1 + count_th(word.replace("th", "x", 1))


print(count_th("thhtthht"))
