/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var topKFrequent = function(nums, k) {
//     hashmap map number and its count
    let count=new Map()
    let res=[]
    for(let num of nums){
        if(!count.has(num)) count.set(num,0)
        count.set(num,count.get(num)+1)
 
    }
    const tracker=Array.from(count.entries())

    tracker.sort((a,b)=>{ //nlogn
        if(a[1]-b[1]>0) return -1
        if(a[1]-b[1]<0) return 1
        return 0
    })
   
    for(let i=0;i<k;i++){
        res.push(tracker[i][0])
    }
    return res
};