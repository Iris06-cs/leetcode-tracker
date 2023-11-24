/**
 * @param {string} colors
 * @return {boolean}
 */
var winnerOfGame = function(colors) {
//     one player remove a letter will not make chance for the other aaabbb=>aabb
//     look for aaa bbb pattern substr
    let AliceScore=0
    let BobScore=0
//     length-2 not length -3
    // for(let i=0;i<colors.length-2;i++){//O(n)
    //     let subString=colors.slice(i,i+3)// O(3)
    //     // console.log(subString)
    //     if(subString==="AAA") AliceScore++
    //     else if(subString==="BBB") BobScore++
    // }
    
     for (let i = 0; i < colors.length - 2; i++) {
        if (colors[i] === colors[i+1] && colors[i+1] === colors[i+2]) {
            if (colors[i] === 'A') AliceScore++;
            else if (colors[i] === 'B') BobScore++;
        }
    }
    // console.log(AliceScore,BobScore)
    return AliceScore>BobScore
};