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
console.log('dhd')
console.log(binSearch([1,2,3,4,5,6,7], 13))
console.log(binSearchRec([1,2,3,4,5,6,7], 13))
