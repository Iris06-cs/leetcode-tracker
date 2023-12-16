class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        # hash map to track count of each number in array
        # remove from the less count number till k = 0
        count_tracker={}
        for num in arr:
            if num not in count_tracker.keys():
                count_tracker[num]=[num,0]
            count_tracker[num][1] += 1
        print(count_tracker)
        count_arr=count_tracker.values()
        sorted_arr=sorted(count_arr,key=lambda x:x[1])
        print(sorted_arr)
        n=len(sorted_arr)
        for i in range(n):
            num,count=sorted_arr[i]
            if k>0 and count<=k:
                k=k-count
                n-=1
                
        return n
            
            
