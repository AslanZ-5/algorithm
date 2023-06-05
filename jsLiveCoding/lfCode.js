function binSearch(arr, t) {
  let start = 0;
  let end = arr.length - 1;
  while (start <= end) {
    let mid = Math.floor((start + end) / 2);
    if (arr[mid] == t) {
      return mid;
    } else if (arr[mid] < t) {
      start = mid + 1;
    } else {
      end = mid - 1;
    }
  }
  return false;
}

function binSearchRec(arr, t, start = 0, end = arr.length - 1) {
  if (start > end) {
    return false;
  } else {
    let mid = Math.floor((start + end) / 2);

    if (arr[mid] == t) {
      return `index ${mid}`;
    } else if (arr[mid] > t) {
      return binSearchRec(arr, t, start, mid - 1);
    } else {
      return binSearchRec(arr, t, mid + 1, end);
    }
  }
}

// two sorted arrays intersection

function intersectionOfTwoArrays(arr1, arr2) {
  let i = 0;
  let j = 0;
  const intersections = [];
  while (arr1.length > i && arr2.length > j) {
    if (arr1[i] == arr2[j]) {
      if (arr1[i] !== arr1[i - 1]) {
        intersections.push(arr1[i]);
      }
      i += 1;
      j += 1;
    } else if (arr1[i] < arr2[j]) {
      i += 1;
    } else {
      j += 1;
    }
  }
  return intersections;
}

// console.log([121,3,2,3,5,7,11].sort((a,b) => a - b))
// console.log(intersectionOfTwoArrays([2,3,3,5,7,11], [3,3,5,7,15,31]))

function intersectionOfTwoSortedArrays(arr1, arr2) {
  let i = 0;
  let j = 0;
  const intersection = [];
  while (i < arr1.length && j < arr2.length) {
    if (arr1[i] === arr2[j]) {
      if (arr1[i] !== arr1[i - 1]) {
        intersection.push(arr1[i]);
      }
      i += 1;
      j += 1;
    } else if (arr1[i] < arr2[j]) {
      i += 1;
    } else {
      j += 1;
    }
  }
  return intersection;
}
console.log(
  "myintersection",
  intersectionOfTwoSortedArrays([2, 3, 3, 5, 7, 11], [3, 3, 7, 15, 31])
);

const arr = [4, 3, 6, 8, 5, 2, 5, 2, 2, 54, 89, 0, 65, 34];

function sortSelect(arr) {
  for (let i = 0; i < arr.length; i++) {
    let minIndex = i;
    for (let j = i + 1; j < arr.length; j++) {
      if (arr[minIndex] > arr[j]) {
        minIndex = j;
      }
    }
    let tmp = arr[i];
    // console.log(tmp)
    arr[i] = arr[minIndex];
    arr[minIndex] = tmp;
  }
  return arr;
}

function sortBuble(arr) {
  for (let i = 0; i < arr.length; i++) {
    for (let j = 0; j < arr.length - i; j++) {
      if (arr[j] > arr[j + 1]) {
        let tmp = arr[j];
        arr[j] = arr[j + 1];
        arr[j + 1] = tmp;
      }
    }
  }
  return arr;
}

function bubbleSorting(arr) {
  let isSorted = false;
  let count = 0;
  while (!isSorted) {
    isSorted = true;
    for (let j = 0; j < arr.length; j++) {
      if (arr[j] > arr[j + 1]) {
        isSorted = false;
        let tmp = arr[j];
        arr[j] = arr[j + 1];
        arr[j + 1] = tmp;
      }
      count += 1;
    }
  }
  console.log(count);
  return arr;
}

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

function insSort(arr) {
  for (let i = 1; i < arr.length; i++) {
    let j = i;
    while (arr[j] < arr[j - 1] && j > 0) {
      const tem = arr[j];
      arr[j] = arr[j - 1];
      arr[j - 1] = tem;
      j--;
    }
  }
  return arr;
}
console.log("__ins__& sorted", insSort(arr));
function insertionSort(arr) {
  for (let i = 1; i < arr.length; i++) {
    for (let j = i; j > 0; j--) {
      if (arr[j] < arr[j - 1]) {
        const tmp = arr[j];
        arr[j] = arr[j - 1];
        arr[j - 1] = tmp;
      } else {
        break;
      }
    }
  }
  return arr;
}
function insertionSort2(arr) {
  for (let i = 1; i < arr.length; i++) {
    j = i;
    while (arr[j] < arr[j - 1] && j > 0) {
      const tmp = arr[j];
      arr[j] = arr[j - 1];
      arr[j - 1] = tmp;
      j -= 1;
    }
  }
  return arr;
}

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

function qS(arr) {
  if (arr.length < 2) {
    return arr;
  }

  const pivot = Math.floor(Math.random * arr.length);
  const sl = [];
  const lr = [];
  const equal = [];
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] == arr[pivot]) {
      equal.push(arr[i]);
    } else if (arr[i] < arr[pivot]) {
      sl.push(arr[i]);
    } else {
      lr.push(arr[i]);
    }
  }
  return qS([...sl, ...equal, ...lr]);
}
console.log("___selectSort___", sortSelect([8, 6, 4, 23, 4, 6, 7, 2, 8, 0]));
console.log("___bubleSort2___", bubbleSorting([8, 6, 4, 23, 4, 6, 7, 2, 8, 0]));
console.log("___mergeSort___", mergeSort([8, 6, 4, 23, 4, 6, 7, 2, 8, 0]));
console.log("___bubleSort___", sortBuble([8, 6, 4, 23, 4, 6, 7, 2, 8, 0]));
console.log("___selectSort___", sortSelect([8, 6, 4, 23, 4, 6, 7, 2, 8, 0]));
console.log(
  "___insertionSort___",
  insertionSort([8, 6, 4, 23, 4, 6, 7, 2, 8, 0])
);
console.log(
  "___insertionSort2___",
  insertionSort2([8, 6, 4, 23, 4, 6, 7, 2, 8, 0])
);
console.log("___quickSort___", quickSort([8, 6, 4, 23, 4, 6, 7, 2, 8, 0]));

const mergeTimestart = new Date().getTime();
// console.log("___insetionSort___",insetionSort([8,6,4,23,4,6,7,2,8,0]))
// console.log("___insetionSort___",insetionSort([8,6,4,23,4,6,7,2,8,0]))
// console.log("___insetionSort___",insetionSort([8,6,4,23,4,6,7,2,8,0]))
// console.log("___insetionSort___",insetionSort([8,6,4,23,4,6,7,2,8,0]))
// console.log("___insetionSort___",insetionSort([8,6,4,23,4,6,7,2,8,0]))
// console.log("___insetionSort___",insetionSort([8,6,4,23,4,6,7,2,8,0]))
// console.log("___insetionSort___",insetionSort([8,6,4,23,4,6,7,2,8,0]))

const mEnd = new Date().getTime();

console.log("merge time measure", mEnd - mergeTimestart);

const testString = "this is My name ";

function firstUppercase(testString, inx = 0) {
  const tStr = testString.replace(" ", "");
  if (tStr[inx] == tStr[inx].toUpperCase()) {
    return tStr[inx];
  }
  if (inx == tStr.length - 1) {
    return "no uppercase letter found";
  }
  return firstUppercase(tStr, inx + 1);
}

function countlength(str) {
  let isCounting = true;
  let inx = 0;
  while (isCounting) {
    inx++;
    if (str[inx] == undefined) {
      isCounting = false;
    }
  }
  return inx;
}
function countlengthRec(str) {
  if (str == "") {
    return 0;
  }
  return 1 + countlengthRec(str.slice(1));
}
console.log(countlength("asadasfasdw adfd"));
console.log(countlengthRec("asadasfasdw adfd"));

function isCon(str) {
  const vowel = "aieou";
  let count = 0;
  for (let i = 0; i < str.length; i++) {
    if (!vowel.includes(str[i].toLowerCase())) {
      count += 1;
    }
  }
  return count;
}
function isConRec(str) {
  const vowel = "aieou";

  if (str == "") {
    return 0;
  }
  if (!vowel.includes(str[0].toLowerCase())) {
    return 1 + isConRec(str.slice(1));
  } else {
    return isConRec(str.slice(1));
  }
}
// console.log(isCon('LuCidProgrAMming'))
// console.log(isConRec('LuCidProgrAMming'))
function prod(x, y) {
  if (y == 1) {
    return x;
  }
  return x + prod(x, y - 1);
}

console.log(prod(5, 5));

// look and say sequence

function saySeq(a) {
  let seq = "";
  let i = 0;
  while (i < a.length) {
    let count = 1;
    while (a[i] == a[i + 1]) {
      count++;
      i++;
    }
    seq += a[i] + count;
    i++;
  }
  return seq;
}

function encodeChar(string) {
  let count = string.length - 1;
  let num = 0;
  for (let i = 0; i < string.length; i++) {
    num += 26 ** count * (string[i].charCodeAt() - "A".charCodeAt() + 1);
    count -= 1;
  }
  return num;
}

function isAlphabet(s) {
  return /[a-zA-Z]/.test(s);
}

function isPalindrom(str) {
  let i = 0;
  let j = str.length - 1;
  while (i < j) {
    while (!isAlphabet(str[i]) && i < j) {
      i += 1;
    }
    while (!isAlphabet(str[j]) && i < j) {
      j -= 1;
    }
    if (str[i].toLowerCase() !== str[j].toLowerCase()) {
      return false;
    }
    i += 1;
    j -= 1;
  }
  return true;
}

console.log("__isPalindrom__", isPalindrom("Was it a cat i saw?"));
console.log("__isPalindrom__", isPalindrom("Was isat a cat i saw?"));

console.log(
  "fairy tales"
    .toLocaleLowerCase()
    .replace(" ", "")
    .split("")
    .sort()
    .join("") ===
    "rail safety".toLocaleLowerCase().replace(" ", "").split("").sort().join("")
);
function isAnagram(str1, str2) {
  str1 = str1.toLocaleLowerCase().replace(" ", "");
  str2 = str2.toLocaleLowerCase().replace(" ", "");
  const ht = {};
  for (let i of str1) {
    if (i in ht) {
      ht[i] += 1;
    } else {
      ht[i] = 1;
    }
  }
  for (let i of str2) {
    if (i in ht) {
      ht[i] -= 1;
    } else {
      ht[i] = 1;
    }
  }
  for (let i in ht) {
    if (ht[i] !== 0) {
      return false;
    }
  }
  return true;
}

let testMoney = 1036.28;

let bills = {
  hundredDollar: 100.0,
  tenDollar: 10.0,
  fiveDollar: 5.0,
  oneDollar: 1.0,
  quarter: 0.25,
  dime: 0.1,
  nickel: 0.05,
  penny: 0.01,
};

function findChange(currency, amount) {
  let resultBills = {};
  let cashLeftover = amount;
  for (let i in currency) {
    while (cashLeftover > currency[i]) {
      if (i in resultBills) {
        resultBills[i] += 1;
      } else {
        resultBills[i] = 1;
      }
      cashLeftover = (cashLeftover - currency[i]).toFixed(2);
    }
    console.log("change bills: ", resultBills);
  }
}

// findChange(bills,testMoney)

function isPalindromPermutation(string) {
  const str = string.toLowerCase().replace(" ", "");
  const h = {};

  for (let i of str) {
    if (i in h) {
      h[i] += 1;
    } else {
      h[i] = 1;
    }
  }
  let countOdd = 0;
  for (let i in h) {
    if (h[i] % 2 !== 0 && countOdd === 0) {
      countOdd += 1;
    } else if (h[i] % 2 !== 0 && countOdd !== 0) {
      return false;
    }
  }
  return true;
}

// console.log('__isPalindromPermutation__', isPalindromPermutation('ddssds'))

function isPermutation(str1, str2) {
  str1 = str1.replace(" ", "").toLowerCase().split("").sort().join("");
  str2 = str2.replace(" ", "").toLowerCase().split("").sort().join("");
  if (str1.length !== str2.length) {
    return false;
  }
  for (let i = 0; i < str1.length; i++) {
    if (str1[i] !== str2[i]) {
      return false;
    }
  }
  return true;
}
// console.log("__isPermutation__",isPermutation('madam', 'adamm'))

function fibonachiIter(n) {
  const fib = [0, 1];
  for (let i = 2; i < n + 1; i++) {
    fib[i] = fib[i - 1] + fib[i - 2];
  }
  return fib[fib.length - 1];
}
function fibonachiRec(n) {
  if (n < 2) {
    return n;
  }
  return fibonachiRec(n - 1) + fibonachiRec(n - 2);
}

// console.log("___fibonach Iter__",fibonachiIter(6))
// console.log("___fibonach Rec__",fibonachiRec(6))

function factorial(n) {
  let fac = 1;
  for (let i = 2; i <= n; i++) {
    fac *= i;
  }
  return fac;
}

function factorialRec(n) {
  if (n <= 1) {
    return 1;
  }
  return n * factorialRec(n - 1);
}
console.log("__factorial__", factorial(5));
console.log("__factorialRec__", factorialRec(5));

function isPrime(n) {
  for (let i = 2; i < Math.sqrt(n); i++) {
    if (n % i === 0) return false;
  }
  return n > 1;
}
console.log("__isPrime__", isPrime(2));

function powerOfTwo(n) {
  while (n > 1) {
    console.log(n);
    if (n % 2 !== 0) {
      return false;
    }
    n /= 2;
  }
  return true;
}
console.log("__poweroftwo__", powerOfTwo(8));

function cartesianProd(arr1, arr2) {
  const arr = [];
  for (let i = 0; i < arr1.length; i++) {
    for (let j = 0; j < arr2.length; j++) {
      arr.push([arr1[i], arr2[j]]);
    }
  }
  return arr;
}
console.log("__cartesian__", cartesianProd([1, 2], [3, 4]));
// console.log('******')

function flatten(array) {
  const arr = [];
  for (let i = 0; i < array.length; i++) {
    const item = array[i];
    Array.isArray(item) ? arr.push(...flatten(item)) : arr.push(item);
    // if (Array.isArray(item)){
    // arr.push(...flatten(item)
    // }else{
    //     arr.push(item)
    // }
  }
  return arr;
}

console.log("__flattend__", flatten([[1], [[2, 3]], [[[4]]]])); // -> [1, 2, 3, 4]

function removeDupes(str) {
  // const chars = {}
  // const res = []

  // for (let i = 0; i < str.length; i++) {
  // if (!chars[str[i]]) {
  // chars[str[i]] = true
  // res.push(str[i])
  // }
  // }

  // return res.join('')

  return Array.from(new Set(str)).join("");
}

function highestFrequency(array) {
  const map = {};
  let maxFreq = 0;
  let maxFreqStr = array[0];

  for (let i = 0; i < array.length; i++) {
    const current = array[i];

    if (map[current]) {
      map[current]++;
    } else {
      map[current] = 1;
    }

    if (map[current] > maxFreq) {
      maxFreq = map[current];
      maxFreqStr = current;
    }
  }

  return maxFreqStr;
}
console.log("__removeDublicate__", Array.from(new Set("aaddss")));

function isRotated(string, compare) {
  if (string.length !== compare.length) {
    return false;
  }
  for (let i = 0; i < string.length; i++) {
    const rotated = string.slice(i, string.length) + string.slice(0, i);
    // const compared = string.slice(0,i) + (string.slice(i,string.length))
    if (rotated === compare) {
      return true;
    }
  }
  return false;
}

console.log("__isRotated__", isRotated("javascrip1", "scriptjava"));

function arraySubset(source, subset) {
  if (source.length < subset.length) {
    return false;
  }
  for (let i = 0; i < subset.length; i++) {
    const index = source.indexOf(subset[i]);
    if (index === -1) {
      return false;
    }
    delete source[index];
  }
  return true;
}
console.log("__arraySubset__", arraySubset([2, 1, 3], [1, 2, 3])); // -> true
console.log(arraySubset([2, 1, 1, 3], [1, 2, 3])); // -> true
console.log(arraySubset([1, 1, 1, 3], [1, 3, 3])); // -> false
console.log(arraySubset([1, 2], [1, 2, 3])); // -> false

function allAnagrams(array) {
  const sorted = array.map((str) => str.split("").sort().join(""));

  for (let i = 1; i < sorted.length; i++) {
    if (sorted[i] !== sorted[0]) {
      return false;
    }
  }
  return true;
}

console.log(allAnagrams(["abcd", "bdac", "cabd"])); // true
console.log(allAnagrams(["abcd", "bdXc", "cabd"])); // false

//ROTATE MATRIX
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

function validParantheses(prnt) {
  const openBrackets = "{[(";
  const hs = {
    "}": "{",
    ")": "(",
    "]": "[",
  };
  const stack = [];

  for (let i = 0; i < prnt.length; i++) {
    if (openBrackets.includes(prnt[i])) {
      stack.push(prnt[i]);
    }
    if (prnt[i] in hs) {
      if (stack[stack.length - 1] === hs[prnt[i]]) {
        stack.pop();
      } else {
        return false;
      }
    }
  }
  return !stack.length;
}
console.log("__validParantheses__", validParantheses("(()){(}{{}}"));

function isEqual(obj1, obj2) {
  if (Number.isNaN(obj1) && Number.isNaN(obj2)) {
    return true;
  }
  if (typeof obj1 !== "object") {
    return obj1 === obj2;
  }
  if (Object.keys(obj1).length !== Object.keys(obj2).length) {
    return false;
  }
  const keys = Object.keys(obj1);

  for (let key of keys) {
    if (!isEqual(obj1[key], obj2[key])) {
      return false;
    }
  }
  return true;
}

console.log(
  "__isEqual__",
  isEqual(
    { obj: 2, kd: 32, employee: { name: "aslan" } },
    { obj: 2, kd: 32, employee: { name: "aslan" } }
  )
);

// Bind function
Function.prototype.myBind = function (context, ...args) {
  return (...rest) => {
    return this.call(context, ...args.concat(rest));
  };
};

function debounce(fn, ms) {
  let time;
  return function () {
    const fnCall = () => {
      fn.apply(this, arguments);
    };
    clearTimeout(time);
    time = setTimeout(fnCall, ms);
  };
}

function throttle(fn, ms) {
  let shouldWait = false;
  let args;
  let arThis;
  function wrapper() {
    if (shouldWait) {
      args = arguments;
      arThis = this;
      return;
    }
    fn.apply(this, arguments);
    shouldWait = true;
    setTimeout(() => {
      shouldWait = false;
      if (args) {
        wrapper.apply(arThis, args);
        arThis = args = null;
      }
    }, ms);
  }
  return wrapper;
}

function callFunc(a, b) {
  console.log(`${a} - ${b} called with debounce`);
}

const callDeb = throttle(callFunc, 2000);

console.log("____________________---");
// const curry = (f, ...a) =>
//   a.length < f.length ? (...b) => curry(f, ...a, ...b) : f(...a);

// function curry(f, ...a){
//     console.log(a)
//     if (a.length < f.length) {

//         return (...args) => {
//             return curry(f, ...a, ...args)
//         }
//     }
//     return f(...a)
// }

function curry(f, ...a) {
  if (a.length < f.length) {
    return (...args) => {
      return curry(f, ...a, ...args);
    };
  }
  return f(...a);
}
function add(a, b, c) {
  return a + b + c;
}

const carriedAdd = curry(add);

console.log(carriedAdd(1)(2)(3));
console.log(carriedAdd(1, 2)(3));
console.log(carriedAdd(1)(2, 3));
console.log(carriedAdd(1, 2, 3));

var foo = {
  tag: "seq",
  left: {
    tag: "seq",
    left: { tag: "note", pitch: "a4", dur: 250 },
    right: { tag: "note", pitch: "b4", dur: 250 },
  },
  right: {
    tag: "seq",
    left: { tag: "note", pitch: "c4", dur: 500 },
    right: { tag: "note", pitch: "d4", dur: 500 },
  },
};

function iterateObj(obj) {
  for (let k in obj) {
    if (typeof obj[k] == "object") {
      iterateObj(obj[k]);
    } else if (Array.isArray(obj[k])) {
      obj[k].map((ob) => iterateObj(ob));
    } else {
      console.log(obj[k]);
    }
  }
}

iterateObj(foo);

console.log("____________________---");

function turtle(hill, move, rollDown) {
  let target = 0;
  let days = 0;
  while (target < hill) {
    target += move;
    target -= rollDown;
    days++;
  }
  return days;
}
// turtle(100,50,30) -> 5

function handShakeCounter(people) {
  let handShake = 0;
  for (let i = 1; i <= people; i++) {
    handShake += i;
  }
  return handShake;
}
//handShakeCounter(10) -> 55

function uniqueWords(str) {
  return Array.from(new Set(str.split(","))).join(",");
}

function arrayRange(array) {
  const groups = [];
  let start = array[0];

  array.push(NaN);

  for (let index = 1; index < array.length; index++) {
    const value = array[index],
      previous = array[index - 1];
    if (value === previous + 1 || value === previous) continue;

    if (start === previous) {
      groups.push("" + previous);
    } else {
      groups.push(start + "-" + previous);
    }
    start = value;
  }
  return groups;
}
let array = [1, 2, 3, 4, 7, 8, 12, 15, 21, 21, 22, 23];
