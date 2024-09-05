function sumOfTwo(arr, target) {
  if (arr.length <= 1) {
    return false;
  }
  const obj = {};
  for (let i = 0; arr.length > i; i++) {
    if (arr[i] in obj) {
      return [arr[i], obj[arr[i]]];
    } else {
      obj[target - arr[i]] = arr[i];
    }
  }
  return false;
}

console.log(sumOfTwo([1, 3, 11, 2, 7], 9));

function twoSum(numbers, target) {
  for (var i = 0; i < numbers.length - 1; i++) {
    for (var j = i + 1; j < numbers.length; j++) {
      if (numbers[i] + numbers[j] === target) return [i, j];
    }
  }
}
