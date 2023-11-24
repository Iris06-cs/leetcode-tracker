/**
 * @param {string} colors
 * @return {boolean}
 */
var winnerOfGame = function(colors) {
//     one player remove a letter will not make chance for the other aaabbb=>aabb
//     look for aaa bbb pattern substr
    let AliceScore=0
    let BobScore=0
    for(let i=0;i<colors.length-2;i++){
        let subString=colors.slice(i,i+3)
        // console.log(subString)
        if(subString==="AAA") AliceScore++
        else if(subString==="BBB") BobScore++
    }
    // console.log(AliceScore,BobScore)
    return AliceScore>BobScore
};