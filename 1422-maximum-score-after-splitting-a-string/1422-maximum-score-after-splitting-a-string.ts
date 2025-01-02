function maxScore(s: string): number {
    let n = s.length
    let ones_count = 0

    for(let i=0; i < n; i++){
        if(s[i] === "1"){
            ones_count++
        }
    }
    let zeroes_count = 0;
    let max_score = 0;

    for(let j=0; j < n-1; j++){
        if(s[j]==="1"){
            ones_count--
        }else{
            zeroes_count++
        }
        if((ones_count + zeroes_count) > max_score){
            max_score = ones_count + zeroes_count
        }
    }
    return max_score
};