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
