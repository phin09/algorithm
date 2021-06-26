/*
https://app.codesignal.com/arcade/intro/level-2/xzKiBHjhoinnpdh6m
Arcade-Intro-4

변수 선언시에도 타입 지정할 것. 하지 않아도 실행은 되지만 연습이 필요함.
변수 앞의 _ 는 함수 안에서만 쓰이는 private한 변수라는 뜻. 접근 범위를 알기 위한 네이밍컨벤션.
*/

// 다른 사람 풀이
// https://app.codesignal.com/arcade/intro/level-2/xzKiBHjhoinnpdh6m/solutions?solutionId=shhk7o8TNRctaQZJ9
function adjacentElementsProduct(inputArray: number[]): number {
  let _numbers: number[] = [];
  for (let i: number = 0; i < inputArray.length - 1; i++) {
    _numbers.push(inputArray[i] * inputArray[i + 1]);
  }
  return Math.max(..._numbers);
}

// 처음 풀이
// function adjacentElementsProduct(inputArray: number[]): number {
//     let maxValue = -9999999;
//     inputArray.forEach((element, index) => {
//         if (maxValue < element * inputArray[index+1]) {
//             maxValue = element * inputArray[index+1];
//         }
//     })
//     return maxValue;
// }
