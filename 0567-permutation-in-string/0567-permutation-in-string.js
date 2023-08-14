/**
 * @param {string} s1
 * @param {string} s2
 * @return {boolean}
 */
var checkInclusion = function(s1, s2) {
     if(s1.length>s2.length) return false
    let s1Chars={}
    for(let char of s1){
        if(s1Chars[char]===undefined) s1Chars[char]=1
        else s1Chars[char]+=1
    }
    let left=0
    let right=s1.length-1
    while(right<s2.length){
        if(s1Chars[s2[left]]===undefined|| s1Chars[s2[right]===undefined]){
            left++
            right++
            continue
        }

        let record={}
        let subStr=s2.slice(left,right+1)
        for(let i=0;i<s1.length;i++){
            if(record[subStr[i]]===undefined) record[subStr[i]]=1
            else record[subStr[i]]+=1
        }
        let keys=Object.keys(record)
        let isMatch=true
        for(let key of keys){
            if(s1Chars[key]!=record[key]){
                isMatch=false
                break
            }
        }
        if(isMatch) return true

        left++
        right++
    }
    return false
};