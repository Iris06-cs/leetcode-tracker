/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function(s) {
//     start left right point at index 0
//     define a set to track the char already included
//     with new char added to set, at the same time increase right point
//     with same char already in set, remove that char from set, and increase left pointer
    if (s.length<=1) return s.length
    let left=0
    let right=0
    let charSet=new Set()
    let maxLength=0
    
    while(right<s.length){
        
        while(charSet.has(s[right])){
            charSet.delete(s[left])
            left++
        }
        charSet.add(s[right]) 

        maxLength=Math.max(maxLength,right-left+1)
        right++
    }
    console.log(charSet)
    return maxLength
    
    
};