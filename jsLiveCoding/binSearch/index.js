function binSearch(arr, t) {
  let start = 0;
  let end = arr.length - 1;

  while (start <= end) {
    let mid = Math.floor((start + end) / 2);
    if (arr[mid] === t) {
      return arr[mid];
    } else if (arr[mid] > t) {
      end = mid - 1;
    } else {
      start = mid + 1;
    }
  }
  return false;
}

// console.log(binSearch([1, 2, 3, 4, 5, 6], 6));

function binSearchReq(arr, t, start = 0, end = arr.length - 1) {
  if (start > end) return false;

  let mid = Math.floor((start + end) / 2);
  if (arr[mid] == t) {
    return arr[mid];
  } else if (arr[mid] > t) {
    return binSearchReq(arr, t, start, mid - 1);
  } else {
    return binSearchReq(arr, t, mid + 1, end);
  }
}

// console.log(binSearchReq([1, 2, 3, 4, 5, 6], 1));
function binSquareRoot(num) {
  let low = 0;
  let high = num;
  let count = 0;
  while (low <= high) {
    count += 1;
    const mid = Math.floor((low + high) / 2);
    if (mid ** 2 <= num) {
      low = mid + 1;
    } else {
      high = mid - 1;
    }
  }
  return [low - 1, count];
}

console.log(binSquareRoot(1300099));
