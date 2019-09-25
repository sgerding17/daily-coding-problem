#!/usr/bin/python3

# 2019-09-21
#
# Write an algorithm to justify text. Given a sequence of words and an integer
# line length k, return a list of strings which represents each line, fully
# justified.
# 
# More specifically, you should have as many words as possible in each line.
# There should be at least one space between each word. Pad extra spaces when
# necessary so that each line has exactly length k. Spaces should be
# distributed as equally as possible, with the extra spaces, if any,
# distributed starting from the left.
# 
# If you can only fit one word on a line, then you should pad the right-hand
# side with spaces.
# 
# Each word is guaranteed not to be longer than k.
# 
# For example, given the list of words ["the", "quick", "brown", "fox",
# "jumps", "over", "the", "lazy", "dog"] and k = 16, you should return the
# following:
# 
#     ["the  quick brown", # 1 extra space on the left
#      "fox  jumps  over", # 2 extra spaces distributed evenly
#      "the   lazy   dog"] # 4 extra spaces distributed evenly

def justify(words, k):
    lines = []

    prev_idx = idx = 0
    while idx < len(words):
        line_chars = 0
        while idx < len(words) and line_chars + len(words[idx]) <= k:
            line_chars += len(words[idx]) + 1
            idx += 1

        extra_spaces = k - (line_chars - 1)
        num_gaps = idx - prev_idx - 1
        spaces_per_gap = 1 + int(extra_spaces / num_gaps)
        extra_extra_spaces = extra_spaces % num_gaps

        line = ''
        for i in range(prev_idx, idx):
            line += words[i]
            if i < (idx - 1):
                line += ' ' * spaces_per_gap
            if (i - prev_idx) < extra_extra_spaces:
                line += ' '
        lines.append(line)

        prev_idx = idx

    return lines

print(justify(["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"], 16))
