/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function(s) {
    let lowerS=s.toLowerCase()
    let trimedS=""
    const alphaChar="abcdefghijklmnopqrstuvwxyz0123456789"
    for( let char of lowerS){
        if(alphaChar.includes(char)) trimedS+=char
    }
    // console.log(trimedS)
    if(! trimedS.length) return true
    let i=0
    let j=trimedS.length-1
    while(i<trimedS.length && j>=0){
        // console.log(trimedS[i],trimedS[j])
        if(trimedS[i]!==trimedS[j]) return false
        i++
        j--
    }
    return true
    
};