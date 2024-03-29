/**
 * @param {number[]} nums
 * @return {number}
 */
var longestConsecutive = function(nums) {
//     time must be O(n), cannot sort array
//     brute force sort nums
//         if(!nums.length) return 0
//         nums.sort((a,b)=>a-b)
//         let numSet=new Set(nums)
//     // console.log(numSet)
//         let maxLen=1
//         let subLen=1
//         let values=Array.from(numSet.values())
//         for(let i=1;i<numSet.size;i++){
//             if(values[i]===values[i-1]+1) {
//                 subLen++
//                 if(subLen>maxLen){
//                     maxLen=subLen
//                 }
//             }
            
//             else subLen=1

                           
//         }
//         return maxLen
    
    //without sorting
    if(!nums.length) return 0
    
    let numSet=new Set(nums)
    let seq={}
    for(let num of nums){
        if(!numSet.has(num-1)) seq[num]=1
    }
    
   
    for(let key in seq){
        let num=Number(key)+1
        // console.log(key,num)
        while(numSet.has(num)){
            seq[key]++
            num++
        }
    }
   let maxLen=1
   for(let val of Object.values(seq)){
       if(val>maxLen) maxLen=val
       else continue
   }
    return maxLen
};