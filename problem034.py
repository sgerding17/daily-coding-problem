#!/usr/bin/python3

# 2019-09-27
#
# Given a string, find the palindrome that can be made by inserting the fewest
# number of characters as possible anywhere in the word. If there is more than
# one palindrome of minimum length that can be made, return the
# lexicographically earliest one (the first one alphabetically).
#
# For example, given the string "race", you should return "ecarace", since we
# can add three letters to it (which is the smallest amount to make a
# palindrome). There are seven other palindromes that can be made from "race"
# by adding three letters, but "ecarace" comes first alphabetically.
# 
# As another example, given the string "google", you should return "elgoogle".

STAR = '*'

def is_palindrome(pattern):
    for i in range(int(len(pattern) / 2)):
        if (pattern[i] != STAR and
            pattern[-(i+1)] != STAR and
            pattern[i] != pattern[-(i+1)]):
            return False
    return True

def make_palindrome(pattern):
    ret = ''
    for (i, s) in enumerate(pattern):
        ret += (s if s != STAR else pattern[-(i+1)])
    return ret

def permute(word, length):
    if len(word) == length: return [word]
    permutations = []
    for slot in range(len(word) + 1):
        new_word = word[:slot] + STAR + word[slot:]
        permutations += permute(new_word, length)
    return permutations

def shortest_palindrome(word):
    for length in range(len(word), 2 * len(word)):
        first_palindrome = ''
        for pattern in permute(word, length):
            candidate = make_palindrome(pattern)
            if is_palindrome(candidate):
                if not first_palindrome or candidate < first_palindrome:
                    first_palindrome = candidate
        if first_palindrome: return first_palindrome

assert is_palindrome('racecar') == True
assert is_palindrome('fastcar') == False
assert is_palindrome('google') == False
assert is_palindrome('elgoogle') == True
assert is_palindrome('**google') == True
assert is_palindrome('race***') == True
assert is_palindrome('d**oggone*') == True

#print(permute('race', 4))
#print(permute('race', 5))
#print(permute('race', 6))
#print(permute('race', 7))
#print(permute('google', 6))
#print(permute('google', 7))
#print(permute('google', 8))

print(shortest_palindrome('race'))
print(shortest_palindrome('google'))
