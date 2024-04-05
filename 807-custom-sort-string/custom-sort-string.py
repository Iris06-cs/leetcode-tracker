class Solution:
    def customSortString(self, order: str, s: str) -> str:

        hash_table = {}
        res = ""
        for char in s:
            if char not in hash_table:
                hash_table[char] = 0
            hash_table[char] += 1
        for char in order:
            if char in hash_table:
                res += char * hash_table[char]
                del hash_table[char]
                
        for char,count in hash_table.items():
            res += char * count
            
        return res
        
        
