function binSearch(arr,t) {
    let start = 0;
    let end = arr.length - 1
    while(start <= end){
        let mid = Math.floor((start + end) / 2)
        if (arr[mid] == t){
            return mid
        }else if (arr[mid] < t){
            start = mid + 1
        }else{
            end = mid - 1
        }
    }
    return false

}

function binSearchRec(arr,t,start=0,end=arr.length - 1){
    if (start > end){
        return false
    }else{
        let mid = Math.floor((start + end) / 2)

        if (arr[mid] == t){
            return `index ${mid}`
        }else if (arr[mid] > t){
            return binSearchRec(arr,t,start,mid-1)
        }else{
            return  binSearchRec(arr,t,mid+1,end)
        }

    }
}

// two sorted arrays intersection

function intersectionOfTwoArrays(arr1,arr2){
    let i = 0;
    let j = 0;
    const intersections = []
    while( arr1.length > i && arr2.length > j){
        if(arr1[i] == arr2[j]){
            if (arr1[i] !== arr1[i - 1]){
                intersections.push(arr1[i])
                
            }
            i += 1
            j += 1
        }else if (arr1[i] < arr2[j]){
            i += 1
        }else{
            j += 1
        }
    }
    return intersections
}

// console.log([121,3,2,3,5,7,11].sort((a,b) => a - b))
// console.log(intersectionOfTwoArrays([2,3,3,5,7,11], [3,3,7,15,31]))

const arr = [4,3,6,8,5,2,5,2,2,54,89,0,65,34]

function sortSelect(arr){
    for (let i = 0; i < arr.length; i++ ){
        let minIndex = i
        for (let j = i + 1; j < arr.length; j++){
            if (arr[minIndex] > arr[j]) {
                minIndex = j
            }}
        let tmp = arr[i]
        // console.log(tmp)
        arr[i] = arr[minIndex]
        arr[minIndex] = tmp 
        }
    return arr
    }

    function sortBuble(arr){
        let count = 0
        for (let i = 0; i < arr.length; i++ ){
            for (let j = 0; j < arr.length - i ; j++){
                    if (arr[j] > arr[ j+ 1]){
                        let tmp = arr[j]
                        arr[j] = arr[j+1]
                        arr[j + 1] = tmp 
                    }
                    count += 1
            }
        
        }
        console.log(count)
        return arr
    }

    function bubbleSorting(arr){
        let isSorted = false
        let i = 0;
        let count = 0;
       while (!isSorted){
        isSorted = true
            for (let j = 0; j < arr.length - i ; j++){
                    if (arr[j] > arr[ j+ 1]){
                        isSorted = false
                        let tmp = arr[j]
                        arr[j] = arr[j+1]
                        arr[j + 1] = tmp 
                    }
                    count += 1
            }
        }
        console.log(count)
        return arr
       
    } 
    

function mergeSort(arr){
    if(arr.length < 2){
        return arr
    }
    const mid = Math.floor(arr.length / 2)
    const rightArr = arr.slice(0,mid)
    const leftArr = arr.slice(mid)
    return merge(mergeSort(leftArr), mergeSort(rightArr))
}

function merge(leftArr, rightArr){
    const sortedArr = []
    while(leftArr.length && rightArr.length){
        if(leftArr[0] < rightArr){
            sortedArr.push(leftArr.push())
        }}
    return [...sortedArr, ...leftArr, ...rightArr]
}


function insetionSort(arr){
    for (let i = 1; i < arr.length; i++){
        for (let j = i; j > 0; j--){
            if (arr[j] < arr[j - 1]){
                const tmp = arr[j]
                arr[j] = arr[j - 1]
                arr[j - 1] = tmp
            }else{
                break
            }
        }
    }
    return arr
}
function insetionSort2(arr){
    for (let i = 1; i < arr.length; i++){
        j = i
       while(arr[j] < arr[j - 1] && j > 0){
        const tmp = arr[j]
        arr[j] = arr[j - 1]
        arr[j - 1] = tmp
        j -= 1
       }
    }
    return arr
}

function quickSort(arr){
    if (arr.length < 2){
        return arr
    }
    const pivot = arr[Math.floor(Math.random() * arr.length)]
    const left = []
    const right = []
    const equal = []
    for (let i; i < arr.length; i++){
        if (arr[i] > pivot){
            left.push(arr[i])
        } else if (arr[i] < pivot){
            right.push(arr[i])
        } else{
            equal.push(arr[i])
        }
    return [ ...quickSort(left), ...equal, ...quickSort(right) ]
    }

}
console.log("___selectSort___",sortSelect([8,6,4,23,4,6,7,2,8,0]))
console.log("___bubleSort2___",bubbleSorting([8,6,4,23,4,6,7,2,8,0]))
console.log("___mergeSort___",bubbleSorting([8,6,4,23,4,6,7,2,8,0]))
console.log("___bubleSort___",sortBuble([8,6,4,23,4,6,7,2,8,0]))
console.log("___selectSort___",sortSelect([8,6,4,23,4,6,7,2,8,0]))
console.log("___insetionSort___",insetionSort([8,6,4,23,4,6,7,2,8,0]))
console.log("___insetionSort2___",insetionSort2([8,6,4,23,4,6,7,2,8,0]))
console.log("___quickSort___",insetionSort2([8,6,4,23,4,6,7,2,8,0]))


const mergeTimestart = new Date().getTime()
// console.log("___insetionSort___",insetionSort([8,6,4,23,4,6,7,2,8,0]))
// console.log("___insetionSort___",insetionSort([8,6,4,23,4,6,7,2,8,0]))
// console.log("___insetionSort___",insetionSort([8,6,4,23,4,6,7,2,8,0]))
// console.log("___insetionSort___",insetionSort([8,6,4,23,4,6,7,2,8,0]))
// console.log("___insetionSort___",insetionSort([8,6,4,23,4,6,7,2,8,0]))
// console.log("___insetionSort___",insetionSort([8,6,4,23,4,6,7,2,8,0]))
// console.log("___insetionSort___",insetionSort([8,6,4,23,4,6,7,2,8,0]))





const mEnd = new Date().getTime()

console.log('merge time measure',mEnd - mergeTimestart)



const testString = 'this is My name '

function firstUppercase(testString, inx=0){
    const tStr = testString.replace(' ', '')
    if (tStr[inx] == tStr[inx].toUpperCase()){
        return tStr[inx]
    }
    if (inx == tStr.length - 1){
        return 'no uppercase letter found'
    }
    return firstUppercase(tStr, inx + 1)
}


function countlength(str){
    let isCounting = true;
    let inx = 0;
    while(isCounting){

        inx++
        if (str[inx] == undefined){
            isCounting = false
        }
    }
    return inx
}
function countlengthRec(str){
    if (str == ''){
        return 0
    }
    return 1 + countlengthRec(str.slice(1))
}
console.log(countlength('asadasfasdw adfd'))
console.log(countlengthRec('asadasfasdw adfd'))

function isCon(str){
    const vowel = 'aieou'
    let count = 0
    for (let i = 0; i < str.length; i++){
        if (!vowel.includes(str[i].toLowerCase())){
            count += 1
        }
    }
    return count 
}
function isConRec(str){
    const vowel = 'aieou'

    if (str == ''){
        return 0
    }
    if (!vowel.includes(str[0].toLowerCase())){
        return 1 + isConRec(str.slice(1))
    }else{
        return isConRec(str.slice(1))
    }
}
// console.log(isCon('LuCidProgrAMming'))
// console.log(isConRec('LuCidProgrAMming'))
function prod(x,y){
    if (y == 1){
        return x
    }
    return x + prod(x, y - 1 )
}

console.log(prod(5,5))


// look and say sequence

function saySeq(a){
    let seq = ''
    let i = 0;
    while (i < a.length){
        let count = 1;
        while( a[i] == a[i + 1]){
            count++
            i++
        }
        seq += a[i] + count
        i++
    }
    return seq
}

function encodeChar(string){
    let count = string.length -1;
    let num = 0;
    for (let i = 0; i < string.length; i++){
        num += 26**count * (string[i].charCodeAt() - 'A'.charCodeAt() + 1)
        count -= 1
    }
    return num

}

function isAlphabet(s){
    return /[a-zA-Z]/.test(s)
}

function isPalindrom(str){
    let i = 0;
    let j = str.length - 1
    while ( i < j){
        while (!isAlphabet(str[i]) && i < j){
            i += 1
        }
        while (!isAlphabet(str[j]) && i < j ){
            j -= 1
        }
        if (str[i].toLowerCase() !== str[j].toLowerCase()){
            return false
        }
        i += 1
        j -= 1
    }
    return true
}

// console.log("__isPalindrom__",isPalindrom('Was it a cat i saw?'))
// console.log("__isPalindrom__",isPalindrom('Was isat a cat i saw?'))

console.log( 'fairy tales'.toLocaleLowerCase().replace(' ', '').split('').sort().join('') === 'rail safety'.toLocaleLowerCase().replace(' ', '').split('').sort().join(''))
function isAnagram(str1,str2){
    str1 = str1.toLocaleLowerCase().replace(' ', '')
    str2 = str2.toLocaleLowerCase().replace(' ', '')
    const ht = {}
    for (let i of str1){
        if (i in ht){
            ht[i] += 1
        }else{
            ht[i] = 1
        }
    }
    for (let i of str2){
        if (i in ht){
            ht[i] -= 1
        }else{
            ht[i] = 1
        }
    }
    for (let i in ht){
        if (ht[i] !== 0){
            return false
        }
       
    }
    return true

}

console.log('___isAnagram___',isAnagram('fairy tales', 'rail safety'))