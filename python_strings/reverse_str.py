"""
How do we efficiently reverse a string in Python?
"""

mystr = "hello how are you?"

"""
This is the most optimal way to reverse a string
Under the hood, the C code creates a new slice and
copy all elements to the new allocated memory
"""
print(mystr[::-1])

"""
This solution takes quadratic time because strings are immutable
in Python
"""

reversed_str = ""
for x in mystr:
    reversed_str = x + reversed_str


"""
U can also swap elements by transforming the string in a mutable list
Still linear time
"""

mylist = list(mystr)
i = 0
j = len(mylist) - 1
while i < j:
    mylist[i], mylist[j] = mylist[j], mylist[i]
    i += 1
    j -= 1

''.join(mylist)


"""
Similar to the above, remembering that strings are iterables in Python
and reversed returns an iterable that goes in reverse order
"""

''.join(reversed(mystr))
