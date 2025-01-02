function createCounter(n: number): () => number {
    let current = n
    
    return function() {
        return current++
    }
}


/** 
 * const counter = createCounter(10)
 * counter() // 10
 * counter() // 11
 * counter() // 12
 */