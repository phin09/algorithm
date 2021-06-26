/*
https://app.codesignal.com/arcade/intro/level-1/egbueTZRRL5Mm4TXN
Arcade-Intro-2

파이썬과 달리 몫을 구하는 내장함수가 없다.
*/

const centuryFromYear: (a: number) => number = (year) => Math.ceil(year / 100);

// 처음 풀이
// function centuryFromYear(year: number): number {
//     let temp = Math.floor(year / 100);
//     if (year % 100 !== 0) {
//         temp++;
//     }
//     return temp;
// }
