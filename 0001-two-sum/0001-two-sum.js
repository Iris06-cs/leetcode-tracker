/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
      let record={}
    for(let i=0;i<nums.length;i++){
        const num=nums[i]
        const diff=target-num
        // 1-indexed
        if(record[diff]!=undefined) return [record[diff],i]
        record[num]=i
    }
    
};