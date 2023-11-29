/**
 * @param {number[][]} intervals
 * @return {number[][]}
 */
var merge = function(intervals) {
// sort intervals based on start value
    intervals.sort((a,b)=>a[0]-b[0])//O(nlogn)
    // console.log(intervals)
    res=[intervals[0]]
    
    for(let i=1;i<intervals.length;i++){
        let prevEnd=res[res.length-1][1]
        
        let start=intervals[i][0]
        let end=intervals[i][1]
        
//         is overlap
        if(start<=prevEnd) res[res.length-1][1]=Math.max(prevEnd,end) 
//         not overlap
        else res.push(intervals[i])
        
    }
    return res
};