"""
Thanks to array manipulation of hackerrank, I learned about prefix sum:
https://en.wikipedia.org/wiki/Prefix_sum

This data structure, also know as prefix sum, scan, cumulative sum, of a sequence [x0, x1, ... xn] is a second sequence [y0, y1, ... yn] of the sum prefixes of the original xi sequence. This is:

y0 = x0
y1 = x0 + x1
y2 = x0 + x1 + x2
y3 = x0 + x1 + x2 + x3

The above in programming is this:

xs = [x for x in range(10)]
ys = [0] * len(xs)

ys[0] = xs[0]
for i range(1, len(xs)):
	ys[i] += ys[i - 1] + xs[i]
"""


# Let's use prefixsum to compute factorial using
# the property that default values are stored in
# the function body of python

# Good thing of this implementation: We store in memory
# the already calculated values of factorial


def factorial(n, precalculated=[1]):
    if n == 0:
        return precalculated[0]
    elif n == 1:
        return precalculated[0]

    if len(precalculated) > n:
        return precalculated[n]
    else:
        start = len(precalculated)
        for i in range(start, n + 1):
            precalculated.append(precalculated[i-1] * i)
        return precalculated[n]


factorial(8)

factorial(3) #Precalculated value!

import inspect

# See how the below code returns the default vlaues
# of the function which contains our precalculated
# factorial values
inspect.signature(factorial)
