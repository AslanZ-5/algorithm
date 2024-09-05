function fibonachiIter(n) {
  const fib = [0, 1];
  for (let i = 2; i < n + 1; i++) {
    fib[i] = fib[i - 1] + fib[i - 2];
  }
  return fib[fib.length - 1];
}
function fibonachiRec(n) {
  if (n < 2) {
    return n;
  }
  return fibonachiRec(n - 1) + fibonachiRec(n - 2);
}
