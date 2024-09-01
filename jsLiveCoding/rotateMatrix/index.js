const matrix = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9],
];

function rotateMatrix(mtrx) {
  const len = mtrx.length;
  const newMtrx = mtrx.map(() => []);

  for (let i = 0; i < len; i++) {
    for (let j = 0; j < len; j++) {
      newMtrx[j][len - 1 - i] = mtrx[i][j];
    }
  }
  return newMtrx;
}
console.log("__rotateMatrix__", rotateMatrix(matrix));

function rotate(matrix, direction) {
  var result = [],
    n = matrix.length,
    m = matrix[0].length,
    i,
    j,
    row;

  for (i = 0; i < m; ++i) {
    row = [];
    for (j = 0; j < n; ++j) {
      row.push(
        direction === "clockwise" ? matrix[n - j - 1][i] : matrix[j][m - i - 1]
      );
    }
    result.push(row);
  }

  return result;
}
