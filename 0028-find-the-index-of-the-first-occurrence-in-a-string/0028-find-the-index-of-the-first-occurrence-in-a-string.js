/**
 * @param {string} haystack
 * @param {string} needle
 * @return {number}
 */
var strStr = function(haystack, needle) {
//     O(N)
    // return haystack.indexOf(needle)
    
// check if needle is sub-string of haystack
// edge case, needle is longer than haystack=> cannot be sub-string return -1
// same length, check if needle and haystack is same string
// otherwise, get the length of needle
//     loop thru haystack to get each sub-stirng with same length as needle, and compare

    if(haystack.length<needle.length) return -1
    if(haystack.length===needle.length){
        if(haystack===needle) return 0
        return -1
    }
    const needleLength=needle.length
    for(i=0;i<haystack.length;i++){
        const subString=haystack.slice(i,i+needleLength)
        console.log(subString)
        if(subString===needle) return i
    
    }
    return -1
       
};