/**
 * @param {string[]} strs
 * @return {string}
 */
var longestCommonPrefix = function(strs) {
    if(strs.length===0) return ""

    let i=1
    let prefix=strs[0]
    while(i<strs.length){
        while(strs[i].indexOf(prefix)!=0){
            prefix=prefix.substring(0,prefix.length-1)
        }
        i++
     
    }
    return prefix
};