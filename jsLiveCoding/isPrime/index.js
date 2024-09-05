function isPrime(n) {
  for (let i = 2; i < Math.sqrt(n); i++) {
    if (n % i === 0) return false;
  }
  return n > 1;
}
console.log("__isPrime__", isPrime(2));
