// [1,2,3,6,8,5] | 7 => [2,5]

// function sumPair(array,targetSum) {
// const nums = {}
// for(let i=0; i< array.length; i++){
// const potentialNum = targetSum - array[i];
// if (potentialNum in nums) {
// return [array[i], potentialNum]
// } else {
// nums[array[i]] = 'true'
// }
// }

// }

// console.log(sumPair([1,2,3,6,8,5], 7))
//Cумма двух чисел в массиве
(nums1 = [2, 7, 11, 15]), (target1 = 9); //Output: [0,1]
(nums2 = [3, 2, 4]), (target2 = 6); //Output: [1,2]
(nums3 = [3, 2, 3]), (target3 = 6); //Output: [0,2]

function myTwoSum(nums, target) {
  const stack = [];
  for (let i = 0; i < nums.length; i++) {
    const a = nums[i];
    console.log(stack[stack.length - 1] + a, stack.length - 1, i, stack);
    if (stack.length >= 1 && stack[stack.length - 1] + a === target) {
      return [stack.length - 1, i];
    }
    stack.push(a);
  }
}
// var myTwoSum = function(nums, target) {
// for (let i =0; i< nums.length; i++){
// const a = nums[i]
// for(let j = i+1; j<= nums.length; j++){
// if((a + nums[j]) === target){
// return [i,j]
// }

// }
// }

// };
// console.log(1, myTwoSum(nums1, target1))
// console.log(2, myTwoSum(nums2, target2))
// console.log(3, myTwoSum(nums3, target3))
// —---

// function useStateWithHistory(initialState) {
// const [state, setInternalState] = useState(initialValue)
// const history = useRef([state]);
// const historyIndex = useRef(0);

// const setState = (newState) => {
// setInternalState(newState)
// history.current.push(newState)
// historyIndexy.current = history.current.length - 1
// }
// const goBack = () => {
// if( historyIndex.current === 0) return;
// historyIndex.current--;
// setInternalState(history.current[historyIndex.current])
// }
// const goForward = () => {
// if( historyIndex.current >= history.current.length) return;
// historyIndex.current++;
// setInternalState(history.current[historyIndex.current])
// }

// }

// MyComp(){
// const [state ,setState ,goBack ,goForward, history] = useStateWithHistory('first')
// setState('second')
// goBack()
// setState('third')
// }
// / Подсчет количества дубликатов
// Напишите функцию, которая будет возвращать количество отдельных буквенных символов и цифр без учета регистра, которые встречаются во входной строке более одного раза. Предполагается, что входная строка содержит только алфавитные символы (как прописные, так и строчные) и цифры.

// Формат ответа
// Число, количество символов.

// Пример
// "abcde" -> 0 # нет символов, повторяющихся более одного раза
// "aabbcde" -> 2 # 'a' и 'b'
// "aabBcde" -> 2 # 'a' встречается дважды и 'b' дважды (`b` и `B`)
// "indivisibility" -> 1 # 'i' встречается 6 раз

function dup(text) {
  let count = 0;
  let map = new Map();
  map.set("counter", count);
  for (let i = 0; i < text.length; i++) {
    if (map.has(text[i].toLowerCase())) {
      if (map.get(text[i].toLowerCase())) {
        map.set("counter", (count += 1));
        map.set(text[i].toLowerCase(), false);
      }
    } else map.set(text[i].toLowerCase(), true);
  }
  return map.get("counter");
}
console.log("result:", dup("aabBcde"));
