function throttle(fn, ms) {
  let shouldWait = false;
  let args;
  let arThis;
  function wrapper() {
    if (shouldWait) {
      args = arguments;
      arThis = this;
      return;
    }
    fn.apply(this, arguments);
    shouldWait = true;
    setTimeout(() => {
      shouldWait = false;
      if (args) {
        wrapper.apply(arThis, args);
        arThis = args = null;
      }
    }, ms);
  }
  return wrapper;
}

function callFunc(a, b) {
  console.log(`${a} - ${b} called with thorttle`);
}

const callDeb = throttle(callFunc, 2000);
