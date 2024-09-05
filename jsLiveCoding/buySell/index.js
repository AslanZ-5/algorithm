function buySell(arr) {
  let result = 0;

  for (let i = 0; i < arr.length; i++) {
    if (arr[i - 1] < arr[i]) {
      result += arr[i] - arr[i - 1];
    }
  }
  return result;
}

let prices = [7, 1, 5, 3, 6, 4];
let prices2 = [7, 6, 5, 4, 3];
console.log(buySell(prices));
console.log(buySell(prices2));
