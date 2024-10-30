function isValid(s: string): boolean {
    let stack = []
    const bracked_map = { ")": "(", "]":"[", "}":"{" }

    for (let char of s) {
        if ("({[".includes(char)) {
            stack.push(char)
        } else if (stack && bracked_map[char] === stack[stack.length-1]){
            stack.pop()
        } else {
            return false
        }
    }

    return stack.length === 0
};