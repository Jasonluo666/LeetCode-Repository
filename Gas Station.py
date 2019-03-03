class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if not gas:
            return -1
        
        cost_efficiency = []
        for index in range(len(gas)):
            cost_efficiency.append(gas[index] - cost[index])
        
        if sum(cost_efficiency) < 0:
            return -1
        
        # O(n)
        start_pos = 0
        rest = 0
        leftover = 0
        for pos in range(len(cost_efficiency)):
            leftover += cost_efficiency[pos]
            rest += cost_efficiency[pos]
            # reset the start position
            if rest < 0:
                start_pos = pos + 1
                rest = 0
        if leftover >= 0:
            return start_pos
        else:
            return -1