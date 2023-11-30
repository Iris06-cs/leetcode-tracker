/**
 * @param {string[]} operations
 * @return {number}
 */
var calPoints = function(operations) {
//     use stack to keep track of result
//     interate through the operations input
//     check each operation: integer/"+"/"D"/"C" and perform the operation accordingly(push to the result tracker/sum/double/pop)
    let res=[]
    for(let operation of operations){
        if(operation==="C") res.pop()
        else if(operation==="D") res.push(2*res[res.length-1])
        else if(operation==="+"){
            const score=Number(res[res.length-1])+Number(res[res.length-2])
            res.push(score)
        } 
        else res.push(Number(operation))
    }
    const totalScore=res.reduce((acc,val)=>acc+val,0)
    return totalScore
};