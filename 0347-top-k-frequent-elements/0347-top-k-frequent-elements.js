/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
// var topKFrequent = function(nums, k) {
// //     hashmap map number and its count
//     let count=new Map()
//     let res=[]
//     for(let num of nums){
//         if(!count.has(num)) count.set(num,0)
//         count.set(num,count.get(num)+1)
 
//     }
//     const tracker=Array.from(count.entries())

//     tracker.sort((a,b)=>{ //nlogn
//         if(a[1]-b[1]>0) return -1
//         if(a[1]-b[1]<0) return 1
//         return 0
//     })
   
//     for(let i=0;i<k;i++){
//         res.push(tracker[i][0])
//     }
//     return res
// };

var topKFrequent = function(nums, k) {

        let count=new Map()
        let res=[]
        for(let num of nums){
            if(!count.has(num)) count.set(num,0)
            count.set(num,count.get(num)+1)

        }
        let times=new Map()
        for(let i=0;i<=nums.length;i++){
            times.set(i,new Set())
            
        }
        for(let num of nums){
            let num_times=count.get(num)
            times.get(num_times).add(num)
        }

        for(let i=nums.length;i>=0 &&k>0;i--){
            if(times.get(i).size) {
                let values=Array.from(times.get(i).values())
                values.forEach(val=>{
                res.push(val)
                k--
                })


            }
    }

    return res
};