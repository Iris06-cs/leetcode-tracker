/**
 * @param {number[]} arr
 * @param {number} k
 * @return {number}
 */
// var findLeastNumOfUniqueInts = function(arr, k) {
    
//     if(k>arr.length) return 0
    
//     const numCount={}
    
//     for(let num of arr){
//         if(!numCount[num]) numCount[num]=0
//         numCount[num]+=1
//     }
    
//     const countOrder=Object.values(numCount).sort()//nlog(n)
    
//     let uniqueCount=countOrder.length
//     for(let val of countOrder){
    
//         if(val<=k && k>0){
//             k-=val
//             uniqueCount-=1
//         }
//         else{
//             return uniqueCount
//         }
//     }
//     return uniqueCount
    
// };

var findLeastNumOfUniqueInts = function(arr, k) {
    let m = new Map();
    arr.forEach(num => m.set(num, m.get(num)+1 || 1));
    let occurrences = Array.from(m.values());
    occurrences.sort((a,b) => a-b);
    let res = occurrences.length;
    for (let num of occurrences) {
        if (k >= num) {
            k -= num;
            res--;
        }
        else return res;
    }
    return res;
    // Time Complexity: O(nlog(n))
    // Space Complexity: O(n)
};