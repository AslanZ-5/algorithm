function curry(f, ...a) {
  if (a.length < f.length) {
    return (...args) => {
      return curry(f, ...a, ...args);
    };
  }
  return f(...a);
}
function add(a, b, c) {
  return a + b + c;
}

const carriedAdd = curry(add);
