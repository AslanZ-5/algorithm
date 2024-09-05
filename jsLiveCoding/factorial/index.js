function factorial(n) {
  let fac = 1;
  for (let i = 2; i <= n; i++) {
    fac *= i;
  }
  return fac;
}

function factorialRec(n) {
  if (n <= 1) {
    return 1;
  }
  return n * factorialRec(n - 1);
}
console.log("__factorial__", factorial(5));
console.log("__factorialRec__", factorialRec(5));

console.log(parseInt("332", 2));
