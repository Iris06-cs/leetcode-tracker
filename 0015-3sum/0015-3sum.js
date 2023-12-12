/**
 * @param {number[]} nums
 * @return {number[][]}
 */
// var threeSum = function(nums) {
//     nums.sort((a,b)=>a-b)
//     if(nums[0]>0 || nums[nums.length-1]<0) return []
    
//     let i=0
//     let res=[]
//     while(i<nums.length){
//         if(i>0 &&  nums[i]===nums[i-1]) continue
            
//         let j=i+1
//         let k=nums.length-1
//         while(j<k){
//             threeSum=nums[i]+nums[j]+nums[k]
//             console.log(threeSum,nums[i],nums[j],nums[k])
//             if(threeSum>0) k--
//             else if(threeSum<0) j++
//             else {
//                 res.push([nums[i],nums[j],nums[k]])     
//                 console.log("ijk",i,j,k,nums[i],nums[j],nums[k])
//                 while(nums[j]==nums[j+1] && j<k) j++
//                 while (j < k && nums[k] === nums[k - 1]) k--;
//                 j++;
//                 k--;
//                 }
            
//         }
//         i++
//     }  
//     return res
// };

var threeSum = function(nums) {
    nums.sort((a, b) => a - b);
    if (nums[0] > 0 || nums[nums.length - 1] < 0) return [];

    let res = [];
    for (let i = 0; i < nums.length; i++) {
        if (i > 0 && nums[i] === nums[i - 1]) continue;
        
        let j = i + 1;
        let k = nums.length - 1;
        while (j < k) {
            let sum = nums[i] + nums[j] + nums[k];
            if (sum > 0) k--;
            else if (sum < 0) j++;
            else {
                res.push([nums[i], nums[j], nums[k]]);
                while (j < k && nums[j] === nums[j + 1]) j++;
                while (j < k && nums[k] === nums[k - 1]) k--;
                j++;
                k--;
            }
        }
    }
    return res;
};
