/**
 * @param {number[]} numbers
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(numbers, target) {
//     brute force  O(n^2)

//     for(let i=0;i<numbers.length-1;i++){
//         const reminder=target-numbers[i]
//         for(let j=i+1;j<numbers.length;j++){
//             if(reminder===numbers[j]) return[i+1,j+1]
//         }
        
//     }
    
//     two pointer
    let i=0
    let j=numbers.length-1
    
    while(i<numbers.length && j>=0){
        if(numbers[i]+numbers[j]>target) j--
        else if(numbers[i]+numbers[j]===target) return [i+1,j+1]
        else i++
    }
    
};