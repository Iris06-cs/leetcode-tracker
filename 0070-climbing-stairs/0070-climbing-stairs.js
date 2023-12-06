/**
 * @param {number} n
 * @return {number}
 */
// var climbStairs = function(n) {
//     const innerFunc=(i,n)=>{
//         if(i>n)return 0
//         if(i===n) return 1
//         return innerFunc(i+1,n)+innerFunc(i+2,n)
//     }
//     return innerFunc(0,n)
    
    
    
// };

var climbStairs=function(n){
    
    if(n<=1) return n
    
    let first=1
    let second=2
    for(let i=3;i<=n;i++){
        let third=first+second
        first=second
        second=third
    }
    return second
}