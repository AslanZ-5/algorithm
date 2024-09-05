let shuffle = function (arr) {
  for (let i = arr.lengh - 1; i > 0; i--) {
    let tmp = arr[i];
    let rnd = Math.floor(Math.random() * (i + 1));
    arr[i] = arr[rnd];
    arr[rnd] = tmp;
  }
  return arr;
};
