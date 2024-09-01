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
