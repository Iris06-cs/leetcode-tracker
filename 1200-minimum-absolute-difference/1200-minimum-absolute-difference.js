/**
 * @param {number[]} arr
 * @return {number[][]}
 */
// var minimumAbsDifference = function(arr) {
// //     sort arr
// //     get the adjecnt two element difference to find the minimum
//     let sortedArr= arr.sort((a,b)=>a-b)
//     let minDiff=Infinity
//     let res=[]
//     for(let i=0;i<arr.length-1;i++){
//         let diff=Math.abs(sortedArr[i+1]-sortedArr[i])
//         if(diff<minDiff){
//             minDiff=diff
           
//         }
       
//     }
//     for(let i=0;i<sortedArr.length;i++){
//         for(let j=1;j<sortedArr.length;j++){
//             if(sortedArr[j]-sortedArr[i]===minDiff) res.push([sortedArr[i],sortedArr[j]])
//         }
//     }
    
//     return res
// };
var minimumAbsDifference = function(arr) {
    // Sort the array
    arr.sort((a, b) => a - b);

    let minDiff = Infinity;
    let res = [];

    // Find the minimum difference
    for (let i = 0; i < arr.length - 1; i++) {
        minDiff = Math.min(minDiff, arr[i + 1] - arr[i]);
    }

    // Find all pairs with the minimum difference
    for (let i = 0; i < arr.length - 1; i++) {
        if (arr[i + 1] - arr[i] === minDiff) {
            res.push([arr[i], arr[i + 1]]);
        }
    }

    return res;
};