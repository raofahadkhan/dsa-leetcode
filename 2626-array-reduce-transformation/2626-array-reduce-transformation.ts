type Fn = (accum: number, curr: number) => number

function reduce(nums: number[], fn: Fn, init: number): number {
    let initial_value = init
     for(let i = 0; i < nums.length; i++){
        initial_value = fn(initial_value, nums[i])
     }
     return initial_value
};