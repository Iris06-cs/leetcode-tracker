/**
 * @param {number[]} nums
 * @return {number[]}
 */
var productExceptSelf = function(nums) {
// dict record left side product of each num
//     dict record right side product of each number
//     get each total product 
//     let leftProduct={}
//     let rightProduct={}
//     for(let i=0;i<nums.length;i++){
//         const num=nums[i]
//         let prev=1
//         if(i===0) leftProduct[num]=prev
//         else{
//             prev=nums[i-1]
//             leftProduct[num]=prev*leftProduct[prev]
//         }
        
//     }
//     // console.log(leftProduct)
//     for(let j=nums.length-1;j>=0;j--){
//         const curr=nums[j]
//         let next=1
//         if(j===nums.length-1) rightProduct[curr]=next
//         else{
//             next=nums[j+1]
//             rightProduct[curr]=next*rightProduct[next]
//         }
//     }
//     // console.log(rightProduct)
//     let res=[]
//     for(let num of nums){
//         res.push(leftProduct[num]*rightProduct[num])
//     }
//     return res
    let length = nums.length;

  let leftProduct = new Array(length).fill(1);
  let rightProduct = new Array(length).fill(1);

  let leftTemp = 1;
  for (let i = 1; i < length; i++) {
    leftTemp *= nums[i - 1];
    leftProduct[i] = leftTemp;
  }
  let rightTemp = 1;
  for (let j = length - 2; j >= 0; j--) {
    rightTemp *= nums[j + 1];
    rightProduct[j] = rightTemp;
  }
  let res = [];
  for (let k = 0; k < length; k++) {
    res.push(leftProduct[k] * rightProduct[k]);
  }
  return res;
};