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
