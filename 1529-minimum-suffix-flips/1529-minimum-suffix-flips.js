/**
 * @param {string} target
 * @return {number}
 */
var minFlips = function(target) {
//     brute force O(n^2)
//       const n= target.length
//     let s=new Array(n)
//     s.fill("0")
//     // console.log(s)
//     let operations=0
//     for(let i=0;i<n;i++){
//         if(s[i]!==target[i]){
//             operations+=1
     
//             for(let j=i;j<n;j++){
//                 s[j]= s[j]==="0"?"1":"0"
                
//             }
//         }
//     }
//     return operations
    
//     O(n) solution
    let operations=0
    let current="0"
    for(let i=0;i<target.length;i++){
        if(target[i]!==current){
            operations++
            current=current==="0"?"1":"0"
        }
    }
    return operations
};