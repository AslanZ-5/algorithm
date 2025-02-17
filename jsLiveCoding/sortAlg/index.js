function InsertionSort(arr) {
  for (let i = 1; arr.length > i; i++) {
    let j = i;
    while (arr[j] < arr[j - 1]) {
      const temp = arr[j];
      arr[j] = arr[j - 1];
      arr[j - 1] = temp;
      j--;
    }
  }
  return arr;
}

console.log(InsertionSort([32, 35, 533, 27, 4, 1, 7, 9]));

function mergeSort(arr) {
  if (arr.length < 2) {
    return arr;
  }
  const mid = Math.floor(arr.length / 2);
  const rightArr = arr.slice(0, mid);
  const leftArr = arr.slice(mid);
  return merge(mergeSort(leftArr), mergeSort(rightArr));
}

function merge(leftArr, rightArr) {
  const sortedArr = [];
  while (leftArr.length && rightArr.length) {
    if (leftArr[0] < rightArr[0]) {
      sortedArr.push(leftArr.shift());
    } else {
      sortedArr.push(rightArr.shift());
    }
  }
  return [...sortedArr, ...leftArr, ...rightArr];
}

// function sortBuble(arr) {
//   for (let i = 0; arr.length > i; i++) {
//     for (let j = 0; arr.length > j; j++) {
//       if (arr[j] > arr[j + 1]) {
//         const temp = arr[j];
//         arr[j] = arr[j + 1];
//         arr[j + 1] = temp;
//       }
//     }
//   }
//   return arr;
// }

const sortArr = [3,5,87,32,4]


const bubleSort = (arr) => {
    let n = arr.length
    let swapped;
    do {
         swapped = false;
       for (let i = 0; i < n -1; i++){
           if (arr[i] > arr[i+1]){
               const temp = arr[i]
               arr[i] = arr[i + 1]
               arr[i + 1] = temp
           }
           swapped = true
       }
            n--
    } while(swapped)

    return arr;
}

console.log(bubbleSort(sortArr))

function selectionSort(arr) {
  for (let i = 0; arr.length > i; i++) {
    let minindex = i;
    for (let j = i + 1; arr.length > j; j++) {
      if (arr[minindex] > arr[j]) {
        minindex = j;
      }
    }
    const temp = arr[i];
    arr[i] = arr[minindex];
    arr[minindex] = temp;
  }
  return arr;
}

console.log(selectionSort([1, 2222, 4, 56, 8, 32, 4, 22, 5, 3]));

function quickSort(arr) {
  if (arr.length < 2) {
    return arr;
  }
  const pivot = arr[Math.floor(Math.random() * arr.length)];
  const left = [];
  const right = [];
  const equal = [];
  for (let i; i < arr.length; i++) {
    if (arr[i] > pivot) {
      left.push(arr[i]);
    } else if (arr[i] < pivot) {
      right.push(arr[i]);
    } else {
      equal.push(arr[i]);
    }
    return [...quickSort(left), ...equal, ...quickSort(right)];
  }
}

function sortRotatedArr(arr, target) {
  let left = 0;
  let right = arr.length - 1;

  while (left <= right) {
    let mid = Math.floor((left + right) / 2);

    if (num[mid] === target) {
      return mid;
    }

    if (nums[left] <= nums[mid]) {
      if (nums[left] <= target && target <= nums[mid]) {
        right = mid - 1;
      } else {
        left = mid + 1;
      }
    } else {
      if (nums[mid] <= target && target <= nums[right]) {
        left = mid + 1;
      } else {
        right = mid - 1;
      }
    }
  }
  return -1;
}
