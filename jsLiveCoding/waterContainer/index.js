const input = [1, 8, 6, 2, 5, 4, 8, 3, 7];

function waterContainer(arr) {
  let i = 0;
  let j = arr.length - 1;
  let maxres = 0;
  while (i < j) {
    let currentMax = Math.min(arr[i], arr[j]) * (j - i);
    if (currentMax > maxres) {
      maxres = currentMax;
    }
    if (arr[i] < arr[j]) {
      i++;
    } else {
      j--;
    }
  }
  return maxres;
}

console.log(waterContainer(input));
