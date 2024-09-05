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
console.log(arrayRange(array));
