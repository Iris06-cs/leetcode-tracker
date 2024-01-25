class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        if len(skill) == 2:
            return skill[0] * skill[1]
        sorted_skill=sorted(skill)
        print(sorted_skill)
        i = 0
        j = len(skill)-1
        total=sorted_skill[i]+sorted_skill[j]
        product=0
        while i<j:
            if sorted_skill[i]+sorted_skill[j] != total:
                return -1
            else:
                product+=sorted_skill[i]*sorted_skill[j]
            i+=1
            j-=1
        return product
        
        