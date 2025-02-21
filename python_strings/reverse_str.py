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


"""
Common longest prefix in 2 strings
"""

str1 = "Esto es una prueba jdkla"

str2 = "Esto es una otra prueba"

def common_longest_prefix(str1: str, str2: str) -> str:
    i = 0
    n = len(str1)
    m = len(str2)
    shortest = min(n, m)

    for i in range(shortest):
        if str1[i] != str2[i]:
            return str1[:i]
    if n < m:
        return str1[:shortest]
    else:
        return str2[:shortest]
        
common_longest_prefix(str1, str2)

common_longest_prefix("En este caso, hay un string", "En este caso, hay un s")
