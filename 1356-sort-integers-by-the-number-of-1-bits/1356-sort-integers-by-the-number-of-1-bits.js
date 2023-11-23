/**
 * @param {number[]} arr
 * @return {number[]}
 */
// var sortByBits = function(arr) {
//     let binArr=[]
// //     get binary version arr
//     for(let num of arr){
//         binArr.push(num.toString(2))
//     }
//     console.log(binArr)
// //     get count of 1 in each num
//     let digitOnes={}
//     for (let i=0;i<binArr.length;i++){
//         const num=binArr[i]
//         let digitOne=0
        
//         for(let j=0;j<num.length;j++){
//             let val=num[j]
//             if(val==="1") digitOne+=1
//         }
//         digitOnes[i]=digitOne
        
//     }
//     console.log(digitOnes)
// //     sort digitOnes key by value, if same, compare the original num
//     const sortedDigitOnes=Object.entries(digitOnes).sort((a,b)=>a[1]-b[1])//array
//     console.log(sortedDigitOnes)
    
// //     continue from here
    
    
// };

var sortByBits = function(arr) {
    // Convert each number to its binary representation
    const binArr = arr.map(num => num.toString(2));

    // Count the number of 1's in each binary number
    const digitOnes = binArr.map(num => {
        return num.split('').reduce((acc, digit) => {
            return acc + (digit === "1" ? 1 : 0);
        }, 0);
    });

    // Combine the original array with the count of 1's
    const combined = arr.map((num, index) => {
        return { num, countOnes: digitOnes[index] };
    });

    // Sort first by count of 1's, then by the number itself in case of a tie
    combined.sort((a, b) => {
        if (a.countOnes === b.countOnes) {
            return a.num - b.num;
        }
        return a.countOnes - b.countOnes;
    });

    // Map back to the original number
    const sortedArr = combined.map(item => item.num);

    return sortedArr;
};