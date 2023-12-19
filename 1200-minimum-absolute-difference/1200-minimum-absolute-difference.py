class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
#         brute force O(n^2)
        # min_diff=math.inf
        # arr.sort()
        # res=[]
        # for i in range(len(arr)-1):
        #     for j in range(i+1,len(arr)):
        #         min_diff=min(min_diff,abs(arr[i]-arr[j]))
        # for i in range(len(arr)-1):
        #     for j in range(i+1,len(arr)):
        #         if abs(arr[i]-arr[j])==min_diff:
        #             res.append([arr[i],arr[j]])
        # return res
        
#         optimize
#         because the arr will be sorted=>the diff between to nearest two num will be smaller than non-neighbor ones
#         no need to check all possible pairs
        arr.sort()
        min_diff=math.inf
        for i in range(len(arr)-1):
            min_diff=min(min_diff,abs(arr[i]-arr[i+1]))
            
        res=[]
        for i in range(len(arr)-1):
            if abs(arr[i]-arr[i+1])==min_diff:
                res.append([arr[i],arr[i+1]])
        return res
        