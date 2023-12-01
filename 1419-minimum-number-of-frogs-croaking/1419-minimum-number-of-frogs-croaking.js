/**
 * @param {string} croakOfFrogs
 * @return {number}
 */
var minNumberOfFrogs = function(croakOfFrogs) {
//     track each letter from "croak" in input string
//     increment by 1 until reached k,count the c value(keep the max val) decrement by 1
//     after checking all letter in input string, if any char in trackker's count is greater than 1, it's invalid
   let counts={"c":0,"r":0,"o":0,"a":0,"k":0}
   let maxFrogs=0
   let croak="croak"
   for(let i=0;i<croakOfFrogs.length;i++){
       const char=croakOfFrogs[i]
       counts[char]++
    
       if(char === "c"){
            maxFrogs=Math.max(maxFrogs,counts["c"])
       }
       else{
           let prevChar=char !=="c"?croak[croak.indexOf(char)-1]:"c"
      
            if(counts[char]>counts[prevChar]){
            return -1
       }
       }
      
       
       if(char==="k"){
           
           for(let j=0;j<5;j++){
               counts["croak"[j]]--
           }
       }
   }
    for(let val of Object.values(counts)){
        if(val !==0) return -1
    }
    return maxFrogs
    };