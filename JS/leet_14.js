/* https://leetcode.com/problems/longest-common-prefix/
*
* array에서 최소값 뽑기
* (O) Math.min(...arr)
* (X) Math.min(arr) -> NaN 나옴
* https://jjeongil.tistory.com/949
*
* array 안 모든 값이 조건을 만족하는지 확인
* arr.every(testFunction)
*
* string 자르기
* str.slice(startIdx, endIdx+1) -> negative idx 사용이 가능하지만 맨 뒤가 -0 임을 유의
* str.substring(startIdx, endIdx) -> 인자 두개가 서로 뒤바뀌어도 결과가 같음. NaN값은 0으로 처리됨. negative idx 불가능.
* (X. 되긴 하지만 앞으로 쓰지 말것) str.substr(startIdx, lengthFromStartIdx)
* (X) str[:3] -> runtime error
* https://aljjabaegi.tistory.com/127
* */

// 방법 1
// 단순 이중 for문
var longestCommonPrefix = function(strs) {
    if (strs.length === 1) {
        return strs[0];
    }

    turn = Math.min(...strs.map(str => str.length));
    if (turn === 0) {
        return "";
    }

    let tmp = strs[0].substr(0, 1);
    for (i=1; i<=turn; i++) {
        for (let str of strs) {
            if (tmp !== str.substr(0, i)) {
                return tmp.substring(0, i-1);
            }
        }
        tmp = strs[0].substr(0, i+1)
    }
    return tmp.substring(0, i-1); // 가장 작은 길이의 문자열이 최대 prefix일 때
};

// 방법 2
// arr.every()
// https://leetcode.com/problems/longest-common-prefix/discuss/526694/Javascript-simple-solution-using-.every()-with-explanation
var longestCommonPrefix = function(strs) {
    if (!strs.length) {
        return "";
    }

    maxPrefixLength = Math.min(...strs.map(str => str.length))
    if (!maxPrefixLength) {
        return "";
    }
    prefix = "";

    for (i=0; i<maxPrefixLength; i++) {
        let char = strs[0][i];
        if (!strs.every(str => str[i] === char)) {
            break;
        }
        prefix += char;
    }
    return prefix;
};
