/**
 * @param {number} n
 * @return {number}
 */
var countNumbersWithUniqueDigits = function(n) {
    
//     brute force O(10^n * n) too large
//     count=0
//     for(let i=0;i<Math.pow(10,n);i++){
//         if(isUnique(i)) count++
        
//     }
//     function isUnique(num){
//         let counts=new Array(10).fill(0)
// //         ASCII 0-9 48-57
//         let numStr=String(num)
//         for(let j=0;j<numStr.length;j++){
//             counts[numStr.charCodeAt(j)-48]++
//         }
//         for(let val of counts){
//             if(val>=2) return false
//         }
//         return true
//     }
//     return count
    if(n===0) return 1
    let res=10
    let middle=9
    let decrease=9
    while(n>1 && decrease>0){
        middle=middle*decrease
        res+=middle
        decrease--
        n--
    }
    return res
};