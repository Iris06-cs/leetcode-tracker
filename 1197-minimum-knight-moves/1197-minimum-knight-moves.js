/**
 * @param {number} x
 * @param {number} y
 * @return {number}
 */
var minKnightMoves = function(x, y) {
//     shortest path from [0,0] to column x row y 
    
//     define the moves
    const moves=[
        [2, 1], [1, 2], [2, -1], [1, -2], 
        [-2, 1], [-1, 2], [-2, -1], [-1, -2]
    ]
//     use BFS
    let queue=[[[0,0],0]]
    let visited=new Set(['0,0'])
 

    while(queue.length){
        let [[currX,currY],steps]=queue.shift()
        if(currX===x && currY===y) return steps
        // console.log(visited)
        moves.forEach(move=>{
            let nextX=currX+move[0]
            let nextY=currY+move[1]
            let nextCordinate=`${nextX},${nextY}`
            
            if(!visited.has(nextCordinate)){
                visited.add(nextCordinate)
                queue.push([[nextX,nextY],steps+1])
        
            }
            
        })
        
    }
    return -1
    
    
};

