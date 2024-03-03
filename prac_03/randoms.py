"""
What did you see on line 1?
8

What was the smallest number you could have seen, what was the largest?
smallest: 5
largest: 20

What did you see on line 2?
9

What was the smallest number you could have seen, what was the largest?
smallest: 3
largest: 9

Could line 2 have produced a 4?
no

What did you see on line 3?
3.1895554610763117

What was the smallest number you could have seen, what was the largest?
smallest: 2.5
largest: 5.5

Write code, not a comment, to produce a random number between 1 and 100 inclusive.
"""
import random

LOWEST_THRESHOLD = 0
HIGHEST_THRESHOLD = 100

print(random.randint(LOWEST_THRESHOLD, HIGHEST_THRESHOLD))
