/* https://leetcode.com/problems/implement-strstr/
 *
 * slice와 substring의 차이
 * 1. startIdx > endIdx 일 때
 * 2. startIdx나 endIdx가 음수일 때
 * https://hianna.tistory.com/340
 */

// 방법 1
// indexOf
var strStr = function(haystack, needle) {
    return haystack.indexOf(needle);
};

// 방법 2
// string을 계속 새로 만드는.. 별로인 방법
var strStr = function(haystack, needle) {
    let lengthOfNeedle = needle.length;
    if (lengthOfNeedle === 0) return 0;

    for (i=0; i<haystack.length; i++) {
        if (needle === haystack.substring(i, i+lengthOfNeedle)) {
            return i;
        }
    }

    return -1;
};