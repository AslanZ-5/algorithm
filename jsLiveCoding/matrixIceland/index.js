const grid = [
  ["1", "1", "0", "0", "0"],
  ["1", "1", "0", "0", "0"],
  ["0", "0", "1", "0", "0"],
  ["0", "0", "0", "1", "1"],
];

const munIslands = function (grid) {
  let counter = 0;
  let rowslen = grid.length;
  let colslen = grid[0].length;
  if (rowslen === 0) return 0;

  function markNeighbour(grid, R, C) {
    grid[R][C] = "2";
    if (grid[R][C - 1] === "1") {
      markNeighbour(grid, R, C - 1);
    }
    if (grid[R][C + 1] === "1") {
      markNeighbour(grid, R, C + 1);
    }
    if (grid?.[R - 1]?.[C] === "1") {
      markNeighbour(grid, R - 1, C);
    }
    if (grid?.[R + 1]?.[C] === "1") {
      markNeighbour(grid, R + 1, C);
    }
  }

  for (let R = 0; R < rowslen; R++) {
    for (let C = 0; C < colslen; C++) {
      if (grid[R][C] === "1") {
        counter++;
        markNeighbour(grid, R, C);
      }
    }
  }
  return counter;
};

console.log(munIslands(grid));
