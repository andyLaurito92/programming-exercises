"""
Given a unit measure conversion table, such as the following one:

1 yard -> 0.333 cm
1 yard -> 1.016 metric foot
1 yard -> 1 foot
1 mile -> x cm
...

and so on

Create a function that, given the above conversion table and a request input, such as:

2 yards

returns

0.666 cm

TODO :)
2 ways of solving it:

1. graph and bfs
2. I think union find would also do the trick here

In the end, what you care about is connected components, this is, understanding whether u can get
from measure X to measure Y via a path <--> iff they belong to the same disjoint set
"""
