/**
 * @param {string} s
 * @return {boolean}
 */
// var isValid = function(s) {
 
//         let stack=[]
//         let opening=["(","{","["]
//         let closing={")":"(",
//                      "}":"{",
//                      "]":"["}
//         for(let char of s){
//            if(opening.indexOf(char)>=0) stack.push(char)
//             else{
//                 if(closing[char]&&closing[char]===stack[stack.length-1]) stack.pop()
//                 else return false
//             }
        
        
//     }
//     if(stack.length>0) return false
//     return true
    
// };

var isValid = function(s) {
// use stack to keep track of openning parentheses
// iterate through the string, if it's an openting parenthese, push it to the stack
    // if char is a closing parenthese, compare with the last element in stack
    // -if match with the last open parenthese, pop it off the stack and continue

    let stack=[]
    let openingParentheses="([{"
    let closingParentheses={")":"(",
                     "}":"{",
                     "]":"["}
    
    for(let char of s){
        if(openingParentheses.includes(char)) stack.push(char)
        else{
            if(closingParentheses[char] && closingParentheses[char]===stack[stack.length-1]) stack.pop()
            else return false
          
        }
    }
   if(stack.length>0) return false
    return true
    

  
    
};