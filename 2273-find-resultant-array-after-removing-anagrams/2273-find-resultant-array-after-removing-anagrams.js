/**
 * @param {string[]} words
 * @return {string[]}
 */
var removeAnagrams = function(words) {
//     brute force sort each word,only store 1 unique 
    
    let res=[words[0]]
    for(let i=1;i<words.length;i++){
        const prev=words[i-1]
        const curr=words[i]
        const sortedPrev=prev.split("").sort().join("")
        const sortedCurr=curr.split("").sort().join("")
        if(sortedPrev!==sortedCurr) res.push(curr)
    }
    return res
};
