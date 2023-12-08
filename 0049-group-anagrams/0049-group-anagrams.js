/**
 * @param {string[]} strs
 * @return {string[][]}
 */
// var groupAnagrams = function(strs) {
// // brute force , sort each word=> so the anagrams will be turned to same word 
// //     time complexity m*nlogn
    
// //     optimized--hashmap
//     let res={}
    
//     for(let str of strs){
//         let count=new Array(26).fill(0) // represent a to z
  
//         for(let i=0;i<str.length;i++){
//             count[str.charCodeAt(i)-97]++  //ascii code of "a" 97
//         }
//         if(!res[count])res[count]=[]
//         // console.log(res)
//         res[count].push(str)
//     }
    
//     return Object.values(res)
    
// };

var groupAnagrams = function(strs) {

    let res=new Map()
    
    for(let str of strs){
        let count=new Array(26).fill(0) // represent a to z
  
        for(let i=0;i<str.length;i++){
            count[str.charCodeAt(i)-97]++  //ascii code of "a" 97
        }
        let key=count.join("#")
        if(!res.has(key)) res.set(key,[])
        
        res.get(key).push(str)
        // console.log(res)
    }
    
    return Array.from(res.values())
   
};