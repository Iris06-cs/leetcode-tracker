/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s) {
 
        let stack=[]
        let opening=["(","{","["]
        let closing={")":"(",
                     "}":"{",
                     "]":"["}
        for(let char of s){
           if(opening.indexOf(char)>=0) stack.push(char)
            else{
                if(closing[char]&&closing[char]===stack[stack.length-1]) stack.pop()
                else return false
            }
        
        
    }
    if(stack.length>0) return false
    return true
    
};