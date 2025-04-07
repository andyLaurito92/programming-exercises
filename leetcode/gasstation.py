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

# 1 2 3 4 5; 3 4 5 1 2
# 3 7 5; 7 6 2  
# -4 1 3 

# -2 -2 -2 3 3

# -1 -1 1

import math
from typing import List

class Solution:
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
            j += j
            # compute last interval; i.e. n - j
        j = j - sizechunk
        compressed_gas.append(sum(gas[j:n]))
        compressed_cost.append(sum(cost[j:n]))

        res = self.canCompleteCircuit2(compressed_gas, compressed_cost)
        if res == -1:
            return -1
        else:
            if n < sizechunk:
                return res
            # We need to map the idx with the original value
            partition_num = res // sizechunk
            i = sizechunk * partition_num
            j = i + sizechunk
            for k in range(i, min(j+1, n)):
                if self.travelaroundfrom(gas, cost, k):
                    return k


    def canCompleteCircuit2(self, gas: List[int], cost: List[int]) -> int:
        """
        Works, but unoptimal. Worst case is still O(N^2) which is too much
        """
        n = len(gas)
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

assert sol.canCompleteCircuit2([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]) == 3

assert sol.canCompleteCircuit2([2, 3, 4], [3, 4, 3]) == -1

assert sol.canCompleteCircuit(gas, cost) == 6690


assert sol.canCompleteCircuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]) == 3

