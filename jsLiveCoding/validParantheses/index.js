function validParantheses(prnt) {
  const openBrackets = "{[(";
  const hs = {
    "}": "{",
    ")": "(",
    "]": "[",
  };
  const stack = [];

  for (let i = 0; i < prnt.length; i++) {
    if (openBrackets.includes(prnt[i])) {
      stack.push(prnt[i]);
    }
    if (prnt[i] in hs) {
      if (stack[stack.length - 1] === hs[prnt[i]]) {
        stack.pop();
      } else {
        return false;
      }
    }
  }
  return !stack.length;
}
console.log("__validParantheses__", validParantheses("(()){(}{{}}"));
