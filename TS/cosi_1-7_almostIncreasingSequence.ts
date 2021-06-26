/*
https://app.codesignal.com/arcade/intro/level-2/2mxbGwLzvkTCKAJMG
Arcade-Intro-7

if 실행문이 한개면 {} 안 써도 됨.
*/

function almostIncreasingSequence(sequence: number[]): boolean {
    let flag: number = 0;
    for (let i: number = 0; i < sequence.length; i++) {
        if (sequence[i] >= sequence[i+1]) {
                flag++;
            if (sequence[i-1] >= sequence[i+1]) {
                if (sequence[i] >= sequence[i+2]) {flag++;}
                i++;
            } 
        }
        if (flag > 1) {
            return false;
        }
    }
    return true;
}
