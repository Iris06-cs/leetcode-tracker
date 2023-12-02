/**
 * @param {number} target
 * @param {number[]} nums
 * @return {number}
 */
var minSubArrayLen = function(target, nums) {
    
//     brute force nested loop try all subarray 
//     sliding window, with two pointers moving from left to right and keep track of sum and length
    let total=nums[0]
    let len=Infinity
    let left=0
    let right=0
    
    while(left<nums.length && right<nums.length){
        if(total<target) {
            right++
            total+=nums[right]
        }
        else{
            if(len>right-left+1)len=right-left+1
            total-=nums[left]
            left++
        }
        
    }
    if(len===Infinity) return 0
    return len
};