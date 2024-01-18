class Solution:
    def divisibleTripletCount(self, nums: List[int], d: int) -> int:
        # brute force 3 nested loop
#         n = len(nums)
#         count = 0

#         # Iterate over all possible triplets
#         for i in range(n):
#             for j in range(i + 1, n):
#                 for k in range(j + 1, n):
#                     if (nums[i] + nums[j] + nums[k]) % d == 0:
#                         count += 1

#         return count

        n = len(nums)
        count = 0

        for l in range(n):
            remainder_map = {}

            for r in range(l + 1, n):
                # The remainder that the third element needs to have
                needed_remainder = (d - (nums[l] + nums[r]) % d) % d

                # If we have elements with the needed remainder, add their count
                if needed_remainder in remainder_map:
                    count += remainder_map[needed_remainder]

                # Update the remainder map with the current element
                current_remainder = nums[r] % d
                if current_remainder not in remainder_map:
                    remainder_map[current_remainder] = 0
                remainder_map[current_remainder] += 1

        return count