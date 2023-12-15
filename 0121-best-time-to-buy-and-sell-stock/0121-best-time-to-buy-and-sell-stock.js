/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
    //brute force O(n^2)
//     let profit =0
    
//     for(let i=0;i<prices.length-1;i++){
//         for(let j=i+1;j<prices.length ;j++){
//             const currProfit=prices[j]-prices[i]
//             profit=Math.max(profit,currProfit)
//         }
//     }
//     return profit
    
    let profit=0
    
    let buy=0
    let sell=1
    while(sell<prices.length){
        
        if(prices[buy]<prices[sell]){
            const currProfit=prices[sell]-prices[buy]
        profit=Math.max(profit,currProfit)
            
        }
        else buy=sell
        sell++
    }
    return profit
};