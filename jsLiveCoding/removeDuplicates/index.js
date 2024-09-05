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

const arr1 = [1, 1, 2];

const arr2 = [0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 3, 4];

// Solution1: Time complexity O(n^2) because nums.splice is O(n)
let removeDuplicates = function (nums) {
  for (let i = 0; i < nums.length; i++) {
    if (nums[i] === nums[i - 1]) {
      nums.splice(i, 1);
      i--;
    }
  }

  return nums.length;
};

// Solution2: Time complexity O(n)
let removeDuplicates2 = function (nums) {
  let start = 0;

  for (let i = 0; i < nums.length; ++i) {
    if (nums[i] != nums[i + 1]) {
      nums[start++] = nums[i];
    }
  }
  return start;
};

console.log(removeDuplicates(arr1));
console.log(arr1);

console.log(removeDuplicates2(arr2));
console.log(arr2);
