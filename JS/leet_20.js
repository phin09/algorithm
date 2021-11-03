/* https://leetcode.com/problems/valid-parentheses/
 *
 * Map 만드는 법
 * new Map().set(key1, val1).set(key2, val2);
 * new Map([key1, val1], [key2, key2]);
 *
 * Map의 key를 담은 array
 * Array.from(map.keys())
 *
 * array 안에 특정 값이 있는지
 * arr.includes(val)
 *
 * 빈 array를 판별할 때
 * (O) arr.length === 0
 * (X) arr === []
 * []은 js에서 false가 아님
 */

// 방법 1
// Map
var isValid = function(s) {
    let brackets = new Map().set('(', ')').set('[', ']').set('{', '}');
    // let brackets = new Map([['(', ')'], ['[', ']'], ['{', '}']]);
    let keys = Array.from(brackets.keys());
    let opens = [];

    for (i=0; i<s.length; i++) {
        if (keys.includes(s[i])) {
            opens.push(s[i]);
        } else if (brackets.get(opens.pop()) !== s[i]) {
            return false;
        }
    }

    return opens.length === 0 ? true : false;
};