
// var HitCounter = function() {
    
// };

// /** 
//  * @param {number} timestamp
//  * @return {void}
//  */
// HitCounter.prototype.hit = function(timestamp) {
    
// };

// /** 
//  * @param {number} timestamp
//  * @return {number}
//  */
// HitCounter.prototype.getHits = function(timestamp) {
    
// };
class HitCounter{
    constructor(){
        this.timestamps=[]
        
    }
    hit(timestamp){
        this.timestamps.push(timestamp)
    }
    getHits(timestamp){
        let count=0
        
        for(let i=this.timestamps.length-1;i>=0;i--){
            if(timestamp-this.timestamps[i]<300) count++
        }
        return count
    }
}

/** 
 * Your HitCounter object will be instantiated and called as such:
 * var obj = new HitCounter()
 * obj.hit(timestamp)
 * var param_2 = obj.getHits(timestamp)
 */