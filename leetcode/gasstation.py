"""
There are n gas stations along a circular route, where the amount of gas at the
ith station is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel
from the ith station to its next (i + 1)th station. You begin the journey with
an empty tank at one of the gas stations.

Given two integer arrays gas and cost, return the starting gas station's index
if you can travel around the circuit once in the clockwise direction, otherwise
return -1. If there exists a solution, it is guaranteed to be unique.
"""

import math
from typing import List

class Solution:
    """
    The best solution for this problem is the greedy solution. It
    can be solved in O(N) where N = len(gas)
    """
    def greedy(self, gas:list[int], cost:list[int]) -> int:
        total_cost = 0
        start = 0 
        current_interval = 0
        for k in range(len(gas)):
            edgeweight = gas[k] - cost[k]
            current_interval += edgeweight
            total_cost += edgeweight
            if current_interval < 0:
                start = k + 1
                current_interval = 0
        return -1 if total_cost < 0 else start
            
        
    def travelaroundfrom(self, gas:list[int], cost: list[int], i:int) -> bool:
        j = i
        n = len(gas)
        currentgas = 0
        while True:
            currentgas += gas[j] - cost[j]
            if currentgas < 0:
                return False
            j = (j + 1) % n
            if j == i:
                return True


    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        """
        Idea of this solution: Compressed the super big list into
        smaller chunks, find if there's solution. if it is, then
        find starting point in the smaller interval instead of
        looking into the entire array

        Why doesn't this work? Because the mapping between the original
        array an the compressed array doesn't return correctly the index
        of the partition in which the starting position lies into. The
        problem is because what we really care about is the path, and
        not the edges. When mapping this array into a compressed one,
        we are "destroying" the information of the edges
        """
        
        n = len(gas)
        factor = 9 # To think: How do we decide this?
        i = 0
        sizechunk = int(math.pow(2, factor))
        j = sizechunk
        compressed_gas = []
        compressed_cost = []
        while j < n:
            compressed_gas.append(sum(gas[i:j]))
            compressed_cost.append(sum(cost[i:j]))
            i = j
            j += sizechunk
            # compute last interval; i.e. n - j
        j = j - sizechunk
        compressed_gas.append(sum(gas[j:n]))
        compressed_cost.append(sum(cost[j:n]))

        res = self.canCompleteCircuit2(compressed_gas, compressed_cost)
        if res == -1:
            return -1
        else:
            # Res has the chunk in which we need to start
            i = sizechunk * res 
            j = min(i + sizechunk, len(gas))
            for k in range(i, j):
                if self.travelaroundfrom(gas, cost, k):
                    return k


    def canCompleteCircuit2(self, gas: List[int], cost: List[int]) -> int:
        """
        Works, but unoptimal. Worst case is still O(N^2) which is too much
        """
        gas_values = set(gas)
        cost_values = set(cost)

        if gas[0] == 0 and cost[0] == 0 and len(gas_values) == 1 and len(cost_values) == 1:
            # All values are 0, only situation when it makes sense to consider starting at a gas
            # station with 0 tank
            return 0

        initial_gas = []
        sum = 0
        for i, gascost in enumerate(zip(gas, cost)):
            gasi, costi = gascost
            sum += gasi - costi
            if gasi - costi >= 0 and gasi != 0:
                initial_gas.append(i)

        if sum < 0:
            return -1

        for idx in initial_gas:
            if self.travelaroundfrom(gas, cost, idx):
                return idx
        return -1


sol = Solution()

def read_array(pathfile: str) -> list[int]:
    with open(pathfile) as myfile:
        content = myfile.read()
        content = content[1:len(content)-1]
        content=content.replace('[', '').replace(']', '')
        res = [int(x) for x in content.split(',')]
        return res


inputdir = 'gasstation_input'
cost = read_array(f"{inputdir}/cost1.txt")
gas = read_array(f"{inputdir}/gas1.txt")

assert sol.greedy([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]) == 3

assert sol.greedy([2, 3, 4], [3, 4, 3]) == -1

cost = read_array(f"{inputdir}/cost1.txt")
gas = read_array(f"{inputdir}/gas1.txt")

assert sol.greedy(gas, cost) == 6690

cost = read_array(f"{inputdir}/cost2.txt")
gas = read_array(f"{inputdir}/gas2.txt")

assert sol.greedy(gas, cost) == 6690

assert sol.greedy([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]) == 3


sol.greedy(gas, cost)



"""
Note: This problem is actually called The Circular Walk with Net Zero Sum. It's stated as:

Given a circular array of values, is there a starting point from which you can walk the full circle, accumulating the values step-by-step, without the cumulative sum ever going negative?

The above problem pops up in system modeling (e.g. circuits, potential energy systems, balance models)

It appears in areas like:

-Scheduling with circular dependencies
-Energy/charge conservation in cyclic networks
-Circular buffer processing (e.g. audio/video streaming)

"""
