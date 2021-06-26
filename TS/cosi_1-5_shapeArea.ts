/*
https://app.codesignal.com/arcade/intro/level-2/yuGuHvcCaFCKk56rJ
Arcade-Intro-5

참고 링크 (js 재귀 함수)
https://velog.io/@jakeseo_me/%EC%9E%90%EB%B0%94%EC%8A%A4%ED%81%AC%EB%A6%BD%ED%8A%B8-%EA%B0%9C%EB%B0%9C%EC%9E%90%EB%9D%BC%EB%A9%B4-%EC%95%8C%EC%95%84%EC%95%BC-%ED%95%A0-33%EA%B0%80%EC%A7%80-%EA%B0%9C%EB%85%90-23-%EC%9E%90%EB%B0%94%EC%8A%A4%ED%81%AC%EB%A6%BD%ED%8A%B8-%EC%9E%90%EB%B0%94%EC%8A%A4%ED%81%AC%EB%A6%BD%ED%8A%B8-%EC%9E%AC%EA%B7%80Recursion-%EC%9D%B4%ED%95%B4%ED%95%98%EA%B8%B0

다른 사람 풀이에서 본 것
return n*n + (n-1)*(n-1);
return Math.pow(n, 2) + Math.pow(n - 1, 2);
*/

function shapeArea(n: number): number {
  if (n === 1) {
    return 1;
  } else {
    return shapeArea(n - 1) + 4 * (n - 1);
  }
}
