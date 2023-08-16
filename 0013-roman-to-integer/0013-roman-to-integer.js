/**
 * @param {string} s
 * @return {number}
 */
var romanToInt = function(s) {
    const values={
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
    "IV": 4,
    "IX": 9,
    "XL": 40, 
    "XC": 90,
    "CD": 400,
    "CM": 900
}
    let res=0
    for(let i=0;i<s.length;i++){
        let curr=values[s[i]]
        // console.log(values[s[i+1]])
        if(i!=s.length-1 && curr>values[s[i+1]]){
            console.log("inside 1st if")
            res+=curr
        }
        else if(i!=s.length-1 && curr<values[s[i+1]]){
               console.log("inside 2nd if")
            res-=curr
        
        }
        else{res+=curr}
    }
    return res
    
};