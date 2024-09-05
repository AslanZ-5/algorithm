function isEqual(obj1, obj2) {
  if (Number.isNaN(obj1) && Number.isNaN(obj2)) {
    return true;
  }
  if (typeof obj1 !== "object") {
    return obj1 === obj2;
  }
  if (Object.keys(obj1).length !== Object.keys(obj2).length) {
    return false;
  }
  const keys = Object.keys(obj1);

  for (let key of keys) {
    if (!isEqual(obj1[key], obj2[key])) {
      return false;
    }
  }
  return true;
}

console.log(
  "__isEqual__",
  isEqual(
    { obj: 2, kd: 32, employee: { name: "aslan" } },
    { obj: 2, kd: 32, employee: { name: "aslan" } }
  )
);
