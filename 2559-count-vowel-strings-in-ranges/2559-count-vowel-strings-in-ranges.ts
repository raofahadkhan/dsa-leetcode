function isVowelWord(word: string): boolean {
    let vowels = ['a', 'e', 'i', 'o', 'u']

    return vowels.includes(word[0]) && vowels.includes(word[word.length - 1])
}

function vowelStrings(words: string[], queries: number[][]): number[] {
    let n = words.length

    // Create the pefix sum array
    let prefix_sum = new Array(n + 1).fill(0)

    // Adding the prefix sum to the prefix sum array
    for (let i = 0; i < n; i++) {
        prefix_sum[i + 1] = prefix_sum[i] + (isVowelWord(words[i]) ? 1 : 0)
    }

    let results: number[] = []

    for(const [l,r] of queries){
        results.push(prefix_sum[r + 1] - prefix_sum[l])
    }

    return results

};