#!/usr/bin/python3

# 2019-09-15
#
# Given a dictionary of words and a string made up of those words (no spaces),
# return the original sentence in a list. If there is more than one possible
# reconstruction, return any of them. If there is no possible reconstruction,
# then return null.
#
# For example, given the set of words 'quick', 'brown', 'the', 'fox', and the
# string "thequickbrownfox", you should return ['the', 'quick', 'brown',
# 'fox'].
#
# Given the set of words 'bed', 'bath', 'bedbath', 'and', 'beyond', and the
# string "bedbathandbeyond", return either ['bed', 'bath', 'and', 'beyond] or
# ['bedbath', 'and', 'beyond'].

class PrefixNode(object):
    def __init__(self):
        self.is_word = False
        self.next = {}

def build_prefix_tree(dictionary):
    root = PrefixNode()
    for word in dictionary:
        node = root
        for letter in word:
            if letter not in node.next:
                node.next[letter] = PrefixNode()
            node = node.next[letter]
        node.is_word = True
    return root

def recon_sen(partial, string, trie):
    if not string: return partial
    node = trie
    for i in range(len(string)):
        letter = string[i]
        if letter not in node.next: return []
        node = node.next[letter]
        if node.is_word:
            candidate = recon_sen(partial + [string[:i+1]], string[i+1:], trie)
            if candidate: return candidate
    return []

def reconstruct_sentence(string, dictionary):
    trie = build_prefix_tree(dictionary)
    return recon_sen([], string, trie)

print(reconstruct_sentence('thequickbrownfox',
                           ['quick', 'brown', 'the', 'fox']))
print(reconstruct_sentence('bedbathandbeyond',
                           ['bed', 'bath', 'bedbath', 'and', 'beyond']))

import random
from string import ascii_lowercase
for i in range(100):
    dictionary = [''.join([random.choice(ascii_lowercase)
                             for j in range(random.randrange(1, 10))])
                     for i in range(random.randrange(1, 100))]
    string = ''.join([random.choice(dictionary)
                          for i in range(random.randrange(1, 100))])
    sentence = reconstruct_sentence(string, dictionary)
    assert ''.join(sentence) == string
    for word in sentence: assert word in dictionary
