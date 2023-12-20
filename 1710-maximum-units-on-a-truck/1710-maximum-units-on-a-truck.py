class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        # sort list by total units, then box number
 
        boxTypes.sort(key=lambda x:x[1],reverse=True)
        print(boxTypes)
        res=0
        for boxType in boxTypes:
            print(boxType)
            if boxType[0]<=truckSize:
                res+=boxType[0]*boxType[1]
                truckSize-=boxType[0]
            else:
                res+=truckSize*boxType[1]
                break

        return res
            
        