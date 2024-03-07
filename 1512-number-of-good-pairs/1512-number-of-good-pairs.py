class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        # res = 0
        # for i in range(len(nums) - 1):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] == nums[j]:
        #             res += 1
        # return res
        counter = Counter(nums).values()
        res = sum((count - 1) * ((count-1)+1)//2 for count in counter)
        return res
        