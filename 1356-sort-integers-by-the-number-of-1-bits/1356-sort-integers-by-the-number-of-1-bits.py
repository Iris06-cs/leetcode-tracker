class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        # sorted(iterable, key=None, reverse=False)
        # key: optional function which converts an item to a value to be compared
        
#        sort based on tuple(binary_num,num)==>will first sort by binary_num of count 1, if a tie than sort by x
        return sorted(arr,key=lambda x:(bin(x).count("1"),x))
        # arr.sort(key=lambda x:(bin(x).count("1"),x))
        # return arr
    
#     without lambda
        # def sorter_logic(num):
        #     counting=bin(num).count("1")
        #     return counting,num
        # arr.sort(key=sorter_logic)
        # return arr
        
        
        
        