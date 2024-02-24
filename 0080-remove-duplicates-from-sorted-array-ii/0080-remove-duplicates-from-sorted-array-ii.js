/**
 * @param {number[]} nums
 * @return {number}
 */
var removeDuplicates = function(nums) {
    let len = nums.length

    // special case
    if(len <= 2) return len;

    let slow = 2, fast = 2;

    while(fast < len) {
        /*num at position slow pointer -2, if != num at fast pointer=> hasn't have more than 2
           move num at fast to slow; move slow to the right
        */
        if(nums[slow - 2] !== nums[fast]) {
            nums[slow] = nums[fast]
            slow ++
        }
        fast ++
    }

    return slow
    
    
};