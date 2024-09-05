function debounce(fn, ms) {
  let time;
  return function () {
    const fnCall = () => {
      fn.apply(this, arguments);
    };
    clearTimeout(time);
    time = setTimeout(fnCall, ms);
  };
}
