/**
 * @param {number[]} nums
 * @return {number}
 */
var removeDuplicates = function(nums) {
    let i=0
    let j=0
    while(j<nums.length){
        while(j+1<nums.length&&nums[j+1]==nums[j])  j++
        nums[i]=nums[j]
        i++
        j++
          
    }
    return i
};