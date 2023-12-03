/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */
// var maxNonDecreasingLength = function(nums1, nums2) {
    
// //     choose smaller first element from nums1/nums2 as the first element in nums3
// //     loop from i=1 choose the smaller number that is greater than prev num in nums3, otherwise take the larger one
// //     keep track of the length
// //     -----this is not right if both nums1 nums2 has largest number at begining, it won't going to check other smaller numbers---
//     let nums3=[nums1[0]>=nums2[0]?nums2[0]:nums1[0]]
//     console.log(nums3)
//     let res=1
//     let currentlen=1
//     let n=nums1.length
//     let i=1
//     while(i<n){
// //         const num1=nums1[i]<=nums2[i]?nums1[i]:nums2[i]
// //         const num2=nums1[i]>nums2[i]?nums1[i]:nums2[i]
//         let prev=nums3[i-1]
// //         console.log("debug",num1,num2)
// //         if(num1<=num2 && num1>=prev) {
// //             nums3.push(num1)
// //             res++
// //             console.log(nums3)
// //             i++
// //             continue
// //         }
// //         else if(num2>=prev){
// //             nums3.push(num2)
// //             res++
// //             i++
// //             continue
// //         }
// //         else return res
// //     }
        
// //         return res
//         let num=Math.max(prev,Math.min(nums1[i],nums2[i]))
        
//         if(num>=prev){
//             currentlen++
//             prev=Math.min(nums1[i],nums2[i])
//         }
//         else{
//             res=Math.max(res,currentlen)
//             currentlen=1
//             prev=Math.min(nums1[i],nums2[i])
//         }
//         i++
//     } 
//         res=Math.max(res,currentlen)
//         return res
// };

var maxNonDecreasingLength = function(nums1, nums2) {
    let n = nums1.length;
    // Initialize DP arrays to keep track of the longest non-decreasing subarray lengths
    let dp1 = new Array(n).fill(1); // Tracking for nums1
    let dp2 = new Array(n).fill(1); // Tracking for nums2
    let maxLength = 1;

    for (let i = 1; i < n; i++) {
        // Check for nums1[i] with both nums1[i-1] and nums2[i-1]
        if (nums1[i] >= nums1[i - 1]) {
            dp1[i] = dp1[i - 1] + 1;
        }
        if (nums1[i] >= nums2[i - 1]) {
            dp1[i] = Math.max(dp1[i], dp2[i - 1] + 1);
        }

        // Check for nums2[i] with both nums1[i-1] and nums2[i-1]
        if (nums2[i] >= nums2[i - 1]) {
            dp2[i] = dp2[i - 1] + 1;
        }
        if (nums2[i] >= nums1[i - 1]) {
            dp2[i] = Math.max(dp2[i], dp1[i - 1] + 1);
        }

        // Update the maxLength with the maximum value from dp1[i] and dp2[i]
        maxLength = Math.max(maxLength, dp1[i], dp2[i]);
    }

    return maxLength;
};
