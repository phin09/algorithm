/*
https://app.codesignal.com/arcade/intro/level-2/bq2XnSr5kbHqpHGJC
Arcade-Intro-6

개수만 구하면 되는 문제는 개수만 체크해서 풀 수 있는 방법을 생각해보기.
*/

// 다른 사람 풀이
// https://app.codesignal.com/arcade/intro/level-2/bq2XnSr5kbHqpHGJC/solutions?solutionId=WnjnhKiuw9bwbLDS2
function makeArrayConsecutive2(statues: number[]): number {
    return Math.max(...statues) - Math.min(...statues) + 1 - statues.length;
}

// 처음 풀이
// function makeArrayConsecutive2(statues: number[]): number {
//     let answer: number = 0;
//     for (let i: number = Math.min(...statues); i < Math.max(...statues); i++) {
//         if (statues.find(element => element === i) === undefined) {
//             answer++;
//         }
//     }
//     return answer;
// }