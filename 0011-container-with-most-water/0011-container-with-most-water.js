/**
 * @param {number[]} height
 * @return {number}
 */
var maxArea = function(height) {
//     brute force O(n^2)
//     let amount=0
    
//     for(let i=0;i<height.length-1;i++){
        
//         for(let j=1;j<height.length;j++){
//             const currAmount=(j-i)* Math.min(height[i],height[j])
//             amount=Math.max(currAmount,amount)
//         }
//     }
        
//     return amount
    let amount=0
    let i=0
    let j=height.length-1
    while(i<j){
        const currAmount=(j-i)* Math.min(height[i],height[j])
        amount=Math.max(currAmount,amount)
        if(height[i]<height[j])i++
        else j--
        
        
    }
    return amount
};