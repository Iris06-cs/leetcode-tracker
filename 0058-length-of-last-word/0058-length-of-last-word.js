/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLastWord = function(s) {
    let words=s.split(" ")

    let removedSpaceWords=[]
    words.forEach(word=>{
        if(word!="") removedSpaceWords.push(word)
    })
    return removedSpaceWords[removedSpaceWords.length-1].length
    
};