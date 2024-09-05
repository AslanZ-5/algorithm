function leastBricks(wall) {
  const map = {};
  let max = 0;
  wall.forEach((row) => {
    let sum = 0;
    for (let n = 0; n < row.length; n++) {
      sum += row[n];
      map[sum] = map[sum] ? map[sum] + 1 : 1;
      max = Math.max(map[sum], max);
    }
  });
  console.log(map);
}

const wall = [
  [1, 2, 2, 1],
  [3, 1, 2],
  [1, 3, 2],
  [2, 4],
  [3, 1, 2],
  [1, 3, 1, 1],
];
