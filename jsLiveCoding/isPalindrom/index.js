function isPalindrom(str) {
  console.log();
  if (str.length <= 1) return true;
  if (str[0] !== str[str.length - 1]) return false;
  return isPalindrom(str.slice(1, str.length - 1));
}

// console.log(isPalindrom("asasa"));

function isAlphabet(letter) {
  return /[A-Za-z]/.test(letter);
}

console.log(isAlphabet("1"));
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

///// ispalindrom number
const input11 = 12321; // Output: true
const input22 = -121; // Output: false
const input33 = 10; // Output: false

const isPalindromeNumber = function (x) {
  if (x < 0) return false;
  if (x < 10) return true;
  if (x % 10 === 0) return false;

  let rev = 0;

  while (x > rev) {
    console.log(x, rev);
    rev *= 10;
    rev += x % 10;
    x = Math.trunc(x / 10);
  }

  console.log(x, rev);

  return x === rev || x === Math.trunc(rev / 10);
};

console.log(isPalindromeNumber(input1));
console.log(isPalindromeNumber(input2));
console.log(isPalindromeNumber(input3));

///// longets Palindrom

const input1 = "babad"; // Output: 'bab' | "aba";
const input2 = "cbbd"; // Outupt: 'bb'
const input3 = "mississippississiississi"; // Outupt: 'ississi'
const input4 = "ac"; // Outupt: 'a' | 'c'

const longestPalindrome = function (s) {
  let start = 0;
  let end = 0;

  for (let i = 0; i < s.length; i++) {
    let len1 = expandFromCenter(s, i, i);
    let len2 = expandFromCenter(s, i, i + 1);
    let len = Math.max(len1, len2);

    if (len > end - start) {
      start = Math.ceil(i - (len - 1) / 2);
      end = Math.floor(i + len / 2);
    }
  }

  function expandFromCenter(s, L, R) {
    while (L >= 0 && R < s.length && s[L] === s[R]) {
      L--;
      R++;
    }
    return R - L - 1;
  }

  return s.substring(start, end + 1);
};

console.log(longestPalindrome(input1));
console.log(longestPalindrome(input2));
console.log(longestPalindrome(input3));
console.log(longestPalindrome(input4));
