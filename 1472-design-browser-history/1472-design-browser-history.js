/**
 * @param {string} homepage
 */
// var BrowserHistory = function(homepage) {
    
// };
class BrowserHistory{
    constructor(homepage){
        this.history=[homepage]
        this.currIdx=0
      
    }
    visit(url){
//         this.history=this.history.splice(0,this.currIdx+1)
     
//         this.history.push(url)
//         this.currIdx=this.history.length-1
        this.history.length=this.currIdx+1
        this.history.push(url)
        this.currIdx++
        // console.log(this.history,"debug")
        
    }
    back(steps){
        this.currIdx=Math.max(0,this.currIdx-steps)
        return this.history[this.currIdx]
        
    }
    forward(steps){
    
        this.currIdx=Math.min(this.history.length-1,this.currIdx+steps)
        
        return this.history[this.currIdx]
        
    }
}

/** 
 * @param {string} url
 * @return {void}
 */
// BrowserHistory.prototype.visit = function(url) {
    
// };

// /** 
//  * @param {number} steps
//  * @return {string}
//  */
// BrowserHistory.prototype.back = function(steps) {
    
// };

// /** 
//  * @param {number} steps
//  * @return {string}
//  */
// BrowserHistory.prototype.forward = function(steps) {
    
// };

/** 
 * Your BrowserHistory object will be instantiated and called as such:
 * var obj = new BrowserHistory(homepage)
 * obj.visit(url)
 * var param_2 = obj.back(steps)
 * var param_3 = obj.forward(steps)
 */