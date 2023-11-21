/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function(s) {
    let lowerS=s.toLowerCase()
    // let trimedS=""
    // const alphaChar="abcdefghijklmnopqrstuvwxyz0123456789"
    let trimedS=lowerS.replace(/[^a-z0-9]/g,"")
    
    if(! trimedS.length) return true
    
    // for( let char of lowerS){
    //     if(alphaChar.includes(char)) trimedS+=char
    // }
    
    let i=0
    let j=trimedS.length-1
    // while(i<trimedS.length && j>=0){
    while(i<=j){
        // console.log(trimedS[i],trimedS[j])
        if(trimedS[i]!==trimedS[j]) return false
        i++
        j--
    }
    return true
    
};