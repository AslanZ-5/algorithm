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

// console.log('******')

// Bind function
Function.prototype.myBind = function (context, ...args) {
  return (...rest) => {
    return this.call(context, ...args.concat(rest));
  };
};

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
