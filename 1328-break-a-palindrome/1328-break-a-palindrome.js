/**
 * @param {string} palindrome
 * @return {string}
 */
var breakPalindrome = function(palindrome) {
    if(palindrome.length<=1) return ""
    
//     let subString=palindrome.slice(0,Math.floor(palindrome.length/2)).split("")
//      let lastHalfStr=palindrome.slice(Math.floor(palindrome.length/2))

// //     if any char is not "a" change it to a
// //     if all chars are "a" change the last char to"b"
//     for(let i=0;i<subString.length;i++){
//         let char=subString[i]
//         if(char !=="a") {

//             subString[i]="a"
//             return subString.join("")+lastHalfStr
//         }
//     }    
//    let res= palindrome.split("")
//    res[res.length-1]="b"
//     res=res.join("")
//     return     res
    
     for (let i = 0; i < Math.floor(palindrome.length / 2); i++) {
        if (palindrome[i] !== 'a') {
            return palindrome.substring(0, i) + 'a' + palindrome.substring(i + 1);
        }
    }

    // All characters in the first half are 'a', change the last character to 'b'
    return palindrome.substring(0, palindrome.length - 1) + 'b';
};