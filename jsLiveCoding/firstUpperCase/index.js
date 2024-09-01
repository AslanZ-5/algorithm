function firstUppercase(string, i = 0) {
  const str = string.replace(" ", "");
  if (str[i] === str[i].toUpperCase()) {
    return str[i];
  }
  if (i === str.length - 1) {
    return "no uppercase found";
  }
  return firstUppercase(str, i + 1);
}

console.log(firstUppercase("this is acTesting string"));

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

console.log(saySeq("aaaadsdklskjflwklklkdds"));
