/*
https://app.codesignal.com/arcade/intro/level-1/s5PbmwxfECC52PWyQ
Arcade-Intro-3
*/

function checkPalindrome(inputString: string): boolean {
  const reversedString = inputString.split("").reverse().join("");
  return inputString === reversedString;
}

// 처음 풀이
// function checkPalindrome(inputString: string): boolean {
//     for (let i = 0; i < inputString.length / 2; i++) {
//         if (inputString[i] !== inputString[inputString.length-1-i]) {
//             return false;
//         }
//     }
//     return true;
// }
