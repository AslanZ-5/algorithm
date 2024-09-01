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
