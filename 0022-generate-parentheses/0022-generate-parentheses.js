/**
 * @param {number} n
 * @return {string[]}
 */
var generateParenthesis = function(n) {
    // backtracking
    // add open paranthesis if open<n
    // add close paranthesis if close<open
    // one valid way when open=close=n
    const stack = []
    const res = []
    
    const backtracking=(openNum,closeNum)=>{
        if(openNum === closeNum && openNum === n){
    
            res.push(stack.join(""))
        }
        if(openNum < n){
            stack.push("(")
            backtracking(openNum + 1,closeNum)
            stack.pop()
        }
        if(closeNum < openNum){
            stack.push(")")
            backtracking(openNum, closeNum + 1)
            stack.pop()
        }
    
        
      
    }   
    
    backtracking(0,0)
      return res  
};