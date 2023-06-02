/**
 * @param {number[]} nums
 * @return {number[]}
 */
var findDisappearedNumbers = function(nums) {
//     input with array of int ; range of int will be array.length
//     output array with num not in input array
//     loop thru input nums and range 1-n ;
//     track of the "disappeared num"
    let range=nums.length
    let res=[]
    for(let i=1;i<=range;i++){
        let num=i
        if(!nums.includes(num)) res.push(num)
    }
    return res
};