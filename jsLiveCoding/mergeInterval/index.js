const input1 = [
  [1, 3],
  [8, 10],
  [15, 18],
  [2, 6],
];
const input2 = [
  [1, 4],
  [1, 5],
];
const input3 = [
  [11, 12],
  [2, 3],
  [5, 7],
  [1, 4],
  [8, 10],
  [6, 8],
];

function mergeIntervals(arr) {
  if (arr.length < 2) {
    return arr;
  }

  arr.sort((a, b) => a[0] - b[0]);
  const res = [arr[0]];
  for (let interval of arr) {
    let recent = res[res.length - 1];
    if (recent[1] >= interval[0]) {
      recent[1] = interval[1];
    } else {
      res.push(interval);
    }
  }
  return res;
}

console.log(mergeIntervals(input1));
console.log(mergeIntervals(input2));
console.log(mergeIntervals(input3));
