/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function(s, t) {
    if(s.length!==t.length) return false
    //track all letters
    let lettersS={}
    let lettersT={}
    for (let letter of s){
        if(!lettersS[letter]) lettersS[letter]=1
        else lettersS[letter]+=1
    }
    for (let letter of t){
        if(!lettersT[letter]) lettersT[letter]=1
        else lettersT[letter]+=1
    }
    for (let letter of s){
        if(lettersS[letter]!==lettersT[letter]) return false
    }
    return true
};