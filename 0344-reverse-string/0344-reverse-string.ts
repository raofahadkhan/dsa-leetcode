/**
 Do not return anything, modify s in-place instead.
 */
function reverseString(s: string[]): void {
    let left = 0
    let right = s.length - 1

    while(left < right){
        console.log('before swapping', s);
        [s[left], s[right]] = [s[right], s[left]];
        console.log("after swapping", s)
        left++
        right--
    }
    
};