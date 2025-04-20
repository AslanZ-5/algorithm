const input1 = [
  [1, 1, 1],
  [1, 0, 1],
  [1, 1, 0],
]; // [[1,0,1],[0,0,0],[1,0,1]]

const input2 = [
  [0, 1, 2, 0],
  [3, 4, 5, 2],
  [1, 3, 1, 5],
]; //[[0,0,0,0],[0,4,5,0],[0,3,1,0]]

const setZeroes = function (matrix) {
  const zeroPositions = []
  
  for (let i = 0; i < matrix.length; i++){
      
      for (let j = 0; j < matrix[0].length; j++){
          if (matrix[i][j] === 0) {
              zeroPositions.push([i,j])
          }
      }
  }
  
  for (let inx = 0; zeroPositions.length > inx; inx++){
      const [row, col] = zeroPositions[inx]
       for (let i = 0; i < matrix.length; i++){
           matrix[row][i] = 0
       }
         for (let i = 0; i < matrix.length; i++){
           matrix[i][col] = 0
       }
  }
  return matrix;
};

console.log(setZeroes(input1));
console.log(setZeroes(input2));
