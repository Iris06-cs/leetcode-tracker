/**
 * @param {number[]} numbers
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(numbers, target) {
//     brute force

    for(let i=0;i<numbers.length-1;i++){
        const reminder=target-numbers[i]
        for(let j=i+1;j<numbers.length;j++){
            if(reminder===numbers[j]) return[i+1,j+1]
        }
        
    }
    
};