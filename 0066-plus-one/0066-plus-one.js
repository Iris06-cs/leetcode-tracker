/**
 * @param {number[]} digits
 * @return {number[]}
 */
var plusOne = function(digits) {
//     not working for big integer, Number will loss accuracy
//     let digitsString=digits.join("")
//     console.log(digitsString)
//     let addOne=BigInt(digitsString)+1

//     console.log(addOne)
   // let addedDigits=String(Number(digitsString)+1).split("")
   // console.log(addedDigits)
   // addedDigits.forEach((digit,i)=>{
   //     addedDigits[i]=Number(digit)
   // })
   //  return addedDigits

    for(let i=digits.length-1;i>=0;i--){
        let digit=digits[i]

        if(digit<9){
            digits[i]=digit+1
            return digits
        }
        digits[i]=0
        
    }
    digits.unshift(1)
    return digits
};