class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        digit_letters = {"2":["a","b","c"],
            "3":["d","e","f"],
            "4":["g","h","i"],
            "5":["j","k","l"],
            "6":["m","n","o"],
            "7":["p","q","r","s"],
            "8":["t","u","v"],
            "9":["w","x","y","z"]
            }
        res = []
        def backtracking(idx, path):
            if len(path) == len(digits):
                res.append("".join(path))
                return
            letters = digit_letters[digits[idx]]
            for letter in letters:
                path.append(letter)
                backtracking(idx+1, path)
                path.pop()
        backtracking(0,[])
        return res
        
        
            
        
        
        