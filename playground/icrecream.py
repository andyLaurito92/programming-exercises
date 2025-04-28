"""
A queue of people are waiting to buy ice cream for you.
Each person buys one ice cream, which sells for $5
Each customer is holding a bill of $5, $10 or $20.
Your initial balance is 0.

find whether you will be able to give change for every customer in the queue.
You must serve customers in the order they come in
"""

def icreCreamQueue(queue: list[int]) -> bool:
    res = True
    r = [0] * 3
    for client in queue:
        if client == 5:
             r[0] += 1
        elif client == 10:
             # need to return 5, only 1 way
             if r[0] == 0:
                  return False
             else:
                 r[0] -= 1 # Give san martin back
                 r[1] += 1
        elif client == 20:
           if r[1] >= 1 and r[0] >= 1:
               # First check if you can return 10 given that
               # it's only useful for this case 
               r[1] -= 1
               r[0] -= 1
           elif r[0] >= 3:
               r[0] -= 3 
           else:
               return False
    return True # Pude consumir toda la queue


assert True == icreCreamQueue([5, 5, 5, 10, 20])
assert True == icreCreamQueue([5, 5, 10])
assert False == icreCreamQueue([10, 10])
assert False == icreCreamQueue([10, 5])
