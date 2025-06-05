/**
 * @param {character[][]} grid
 * @return {number}
 */
var numIslands = function(grid) {
    const visited = new Set();
    let count = 0;
    for(let row=0;row<grid.length;row++){
        for(let col=0;col<grid[0].length;col++){
            if(grid[row][col]==="1" && !visited.has(`${[row,col]}`)){
                count++;
                const stack =[[row,col]];
                visited.add(`${[row,col]}`);
                while(stack.length) {
                    const node = stack.pop();
                    const currRow = node[0];
                    const currCol = node[1];
                    const neighbors = getNeighbors(currRow,currCol,grid);

                    for(const neighbor of neighbors){
                        if(!visited.has(`${neighbor}`)){
                            stack.push(neighbor);
                            visited.add(`${neighbor}`)
                        }
                    }
                }
            }
        }
    }
    return count;
    
};
function getNeighbors(row,col,grid) {
    const neighbors = [];
    if(row>=1 && grid[row-1][col]==="1") neighbors.push([row-1,col]);
    if(row<grid.length-1 && grid[row+1][col]==="1") neighbors.push([row+1,col]);
    if(col>=1 && grid[row][col-1]==="1") neighbors.push([row,col-1]);
    if(col<grid[0].length-1 && grid[row][col+1]==="1") neighbors.push([row,col+1]);
    return neighbors;
}