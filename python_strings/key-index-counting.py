"""
This is a sorting algorithm that takes O(N) runtime and O(N) space time to run!

How is it possible that it's faster than the lower bound of O(N log N) ? Because that
bound which says that u cannot have an algorithm that runs faster than that is for
algorithm that do COMPARISSONS

This algorithm doesn't do any comparisson at all :)

Why do we study this algorithm with strings? Because if we want to sort strings,
we can use the fact that these are built from the alphabet they are represented.
If we take ASCII, we have 2^8=256 characters we can have as elements of the string

256 entries for an array is something totally managable!
"""


"""
Let's assume that we can only have characters from a to f
"""
a = ['d', 'a', 'c', 'f', 'f', 'b', 'd', 'b', 'f', 'b', 'e', 'a']
r = 6
count = [0, 0, 0, 0, 0, 0, 0] # 1 per each letter + 1 more
mapping = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5}
aux = [0] * n
n = len(a)

"""
In this step, we count the number of frequencies of each letter
and we put that number in the position after it's own
"""
for i in range(n):
    count[mapping.get(a[i]) + 1] += 1

"""
In this step, we accumulative count the number of repetitions of
the count array. The idea is that we have in count[i] how many
letters less than i exist. This will denote where we need to start
positioning our letter {i}
"""
for i in range(r):
    count[i+1] += count[i]

"""
Put element a[i] in aux[position_letter{i}] according to our count
and increment +1 that counter
"""
for i in range(n):
    aux[count[mapping.get(a[i])]] = a[i]
    count[mapping.get(a[i])] += 1
    print(aux)

"""
Finally, copy back the auxiliary array to a
"""
for i in range(n):
    a[i] = aux[i]



"""
Cormen presents the counting-sort algorithm similar, but not like this.
The only difference is that it usees r spaces for the count array. Instead
then of incrementing the idx, it decrements the count. So instead of starting
from the first element to set up to the last one, you go backwards in Cormen

IMPORTANT FACT of the above: You need to implement the last loop backwards
to keep stability!

Why the above? Think of it by taking a as example.
If u start forward, u pick the first a u have and u put it in the LAST position of the a's. Then u grab your second a and u put it in the before last position and so on. By doing this, you are inverting the order of the elements
"""

a = ['d', 'a', 'c', 'f', 'f', 'b', 'd', 'b', 'f', 'b', 'e', 'a']
n = len(a)
count_cormen = [0] * r
aux = [0] * n

for i in range(n):
    count_cormen[mapping.get(a[i])] += 1

for i in range(1, r):
    count_cormen[i] += count_cormen[i - 1]

for i in reversed(range(n)):
    aux[count_cormen[mapping.get(a[i])] - 1] = a[i]
    count_cormen[mapping.get(a[i])] -= 1

for i in range(n):
    a[i] = aux[i]
