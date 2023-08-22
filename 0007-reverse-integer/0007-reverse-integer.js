/**
 * @param {number} x
 * @return {number}
 */
var reverse = function(x) {
    if(x>=0&&x<=9) return x
    let res=""
    let strX=String(Math.abs(x))
    for(let i=strX.length-1;i>=0;i--){
        res+=strX[i]
    }
    res=x>0?Number(res):-Number(res)
    if(res<-Math.pow(2,31) ||res>Math.pow(2,31)) return 0
    return res
};