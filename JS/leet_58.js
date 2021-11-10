/* https://leetcode.com/problems/length-of-last-word/
 *
 * split은 대상 string의 좌우에 seperator가 있을 경우
 * '  1 2 3  '.split(' ') => ['', '', '1', '2', '3', '', '']
 *
 * array의 뒷쪽에서 요소를 뽑을 때는 length-1 말고 pop()을 고려하기
 */

// 방법 1
// split
var lengthOfLastWord = function(s) {
    let arr = s.trim().split(' ')
    return arr[arr.length-1].length;
};


// 방법 2
// 메모리 줄이기
var lengthOfLastWord = function(s) {
    return s.trim().split(' ').pop().length;
};