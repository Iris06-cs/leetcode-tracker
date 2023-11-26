/**
 * @param {string[]} words
 * @return {string[]}
 */
// var removeAnagrams = function(words) {

    
//     let res=[words[0]]
//     for(let i=1;i<words.length;i++){//O(n)
//         const prev=words[i-1]
//         const curr=words[i]
//         const sortedPrev=prev.split("").sort().join("")//nlog(n)
//         const sortedCurr=curr.split("").sort().join("")
//         if(sortedPrev!==sortedCurr) res.push(curr)
//     }
//     //O(n*nlog(n))
//     return res
// };

//with helper function 

function areAnagrams(word1,word2){
    if(word1.length!==word2.length) return false
    
    let count=new Array(26).fill(0)
    for(let i=0;i<word1.length;i++){
        count[word1.charCodeAt(i)-97]++
        count[word2.charCodeAt(i)-97]--
    }
    for(let val of count){
        if(val) return false
    }
    return true
    
}
var removeAnagrams = function(words) {

    
    let res=[words[0]]
    for(let i=1;i<words.length;i++){//O(n)
        const prev=words[i-1]
        const curr=words[i]
        
        if(!areAnagrams(prev,curr)) res.push(curr)
    }
    //O(n*nlog(n))
    return res
};