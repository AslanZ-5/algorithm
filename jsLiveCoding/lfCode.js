const arr = [4, 3, 6, 8, 5, 2, 5, 2, 2, 54, 89, 0, 65, 34];

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

console.log(
  "fairy tales"
    .toLocaleLowerCase()
    .replace(" ", "")
    .split("")
    .sort()
    .join("") ===
    "rail safety".toLocaleLowerCase().replace(" ", "").split("").sort().join("")
);

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

// const arr = [1,8,3,9,12,13,2,3,4]

// const sortEven = (arr) => {
//   const evenArr = [...arr].filter((num) => {
//       if(num % 2 === 0){
//         return true
//       }
//       return false

//   })
//   evenArr.sort((a,b) => a - b)

//   return arr.map((num) => {
//     if (num % 2 === 0){
//       return evenArr.shift()
//     }
//     return num
//   })

// }

// console.log(sortEven(arr))
