# deque objects are like double-ended queues

import collections
import string


# TODO: initialize a deque with lowercase letters
s = collections.deque(string.ascii_lowercase)
# TODO: deques support the len() function
print(len(s))
# TODO: deques can be iterated over
for l in s:
    print(l.upper())
# TODO: manipulate items from either end
s.appendleft("A")
print(s)
s.rotate(1)
print(s)
# TODO: use an index to get a particular item
print(s[2])