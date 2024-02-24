/**
 * @param {number[]} nums
 * @return {number}
 */
var majorityElement = function(nums) {
    if(nums.length === 1) return nums[0]
    let len = nums.length / 2
    
    // sort nums in place
    // for(let i = 0;i<nums.length-1;i++){
    //     for(let j = i+1;j<nums.length;j++){
    //         if(nums[i]>nums[j]){
    //             temp = nums[i]
    //             nums[i] = nums[j]
    //             nums[j] = temp
    //         }
    //     }
    // }
    
    for(let i = 0;i<nums.length-1;i++){
        let count = 1
        for(let j = i + 1;j<nums.length;j++){
            if(nums[j] === nums[i]) count ++
        }
        if(count > len) return nums[i]
        
        
        
    }
    
    
};