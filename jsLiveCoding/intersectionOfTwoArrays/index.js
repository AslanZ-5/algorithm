const A = [1, 2, 4, 4, 56];
const B = [1, 4, 6, 8, 9, 56];

function intersectionOneLine(arr1, arr2) {
  return arr1.filter((item) => arr2.includes(item));
}

console.log(intersectionOneLine(A, B));

function intersectionOfTwoArrays(arr1, arr2) {
  let i = 0;
  let j = 0;
  const intersections = [];
  while (arr1.length > i && arr2.length > j) {
    if (arr1[i] === arr2[j]) {
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
console.log(intersectionOfTwoArrays(A, B));
