# class Solution:
#     def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
#         # hash map to track count of each number in array
#         # remove from the less count number till k = 0
#         count_tracker={}#O(n)
#         for num in arr:#O(n)
#             if num not in count_tracker.keys():
#                 count_tracker[num]=[num,0]
#             count_tracker[num][1] += 1
            
#         count_arr=count_tracker.values()#O(n)
#         sorted_arr=sorted(count_arr,key=lambda x:x[1])#O(n)  nlogn

#         n=len(sorted_arr)#O(1)
#         for i in range(n):#O(n)
#             num,count=sorted_arr[i]
#             if k>0 and count<=k:
#                 k=k-count
#                 n-=1
                
#         return n   #overall time O(n+nlogn) space O(n)


#         use python Counter collection
#         count_tracker=Counter(arr)   
# #         sort
#         sorted_counts=sorted(count_tracker.values())
#         n=len(sorted_counts)
    
# #         remove elements
#         for count in sorted_counts:
#             if k>=count:
#                 k-=count
#                 n-=1
#             else:
#                 break
#         return n  #nlong space O(n)
    
#     better way without sorting

from collections import Counter

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        # Count occurrences of each number
        count_tracker = Counter(arr)

        # Initialize buckets
        max_freq = max(count_tracker.values())
        buckets = [[] for _ in range(max_freq + 1)]

        # Group elements by their frequencies
        for num, freq in count_tracker.items():
            buckets[freq].append(num)

        # Remove elements starting from the lowest frequency
        unique_integers = len(count_tracker)
        for freq, bucket in enumerate(buckets):
            for num in bucket:
                if k >= freq:
                    k -= freq
                    unique_integers -= 1
                else:
                    return unique_integers

        return unique_integers
