class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total = curr = res = 0
        
        for i in range(len(gas)):
            total += gas[i] - cost[i]
            curr += gas[i] - cost[i]
            
            if curr < 0:
                curr = 0
                res = i + 1
        if total >=0:
            return res
        return -1
        