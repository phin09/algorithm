/* https://leetcode.com/problems/roman-to-integer/

string type을 한글자씩 돌기
(O) for (let s of str)
(X) for (let s in str) -> 한글자가 아닌 index를 뽑음
https://stackoverflow.com/questions/1966476/how-can-i-process-each-letter-of-text-using-javascript

Map =/= Object {key : value}

arr[invalidIdx] = undefined
*/

// 방법 1
// Map
var romanToInt = function(s) {
    let map = new Map();
    map.set('I', 1);
    map.set('V', 5);
    map.set('X', 10);
    map.set('L', 50);
    map.set('C', 100);
    map.set('D', 500);
    map.set('M', 1000);

    let tmp = 0;
    let sum = 0;
    for (let r of s) {
        if (tmp >= map.get(r)) {
            sum += map.get(r);
        } else {
            sum = sum + map.get(r) - 2*tmp;
        }
        tmp = map.get(r);
    }

    return sum;
};

// 방법 2
// Object
// 이 문제의 경우 Map 보다 빠름
var romanToInt = function(s) {
    roman = { 'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000};

    sum = 0;
    for (i=0; i < s.length; i++) {
        let curr = roman[s[i]];
        let next = roman[s[i+1]];

        if (curr < next) {
            sum -= curr;
        } else {
            sum += curr;
        }
    }

    return sum;
};
