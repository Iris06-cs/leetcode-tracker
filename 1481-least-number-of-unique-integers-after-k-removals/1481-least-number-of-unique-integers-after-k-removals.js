/**
 * @param {number[]} arr
 * @param {number} k
 * @return {number}
 */

// Note map object is more effcient in JavaScript
var findLeastNumOfUniqueInts = function(arr, k) {
    if(k>arr.length) return 0
    const numCount=new Map()
    for(let num of arr){
        if(!numCount.get(num)) numCount.set(num,0)
        numCount.set(num,numCount.get(num)+1)
    } 
    console.log(numCount)
    let countOrder=numCount.values()//nlog(n)
    countOrder=Array.from(countOrder).sort((a,b) => a-b)
    console.log(countOrder)
    let uniqueCount=countOrder.length
    for(let val of countOrder){
        if(k>=val){
            k-=val
            uniqueCount--
        }
        else{
            break
        }
    }
    return uniqueCount

};

// var findLeastNumOfUniqueInts = function(arr, k) {
//     let m = new Map();
//     arr.forEach(num => m.set(num, m.get(num)+1 || 1));
//     let occurrences = Array.from(m.values());
//     occurrences.sort((a,b) => a-b);
//     console.log(occurrences)
//     let res = occurrences.length;
//     for (let num of occurrences) {
//         if (k >= num) {
//             k -= num;
//             res--;
//         }
//         else return res;
//     }
//     return res;
//     // Time Complexity: O(nlog(n))
//     // Space Complexity: O(n)
// };