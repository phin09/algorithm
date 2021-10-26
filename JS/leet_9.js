/* https://leetcode.com/problems/palindrome-number/

number type의 자릿수 구하기
(O) num.toString().length
(O) String(num).length
(X) num.length -> undefined

idx 자리의 값 뽑기
(O) num.toString()[idx]
(X) num[idx]

array 만들기
String(num).split('')

JS의 array에서는 arr[-1]이 맨 뒤의 값이 아니라
-1이라는 key로 맵핑된 값을 가져오는 것
*/

// 방법 1
// 무난
var isPalindrome = function(x) {
    if (x < 0) {
        return false;
    }

    strX = x.toString()

    for (i=0; i <= strX.length/2-1; i++) {
        if (strX[i] !== strX[strX.length-i-1]) {
            return false
        }
    }

    return true;
};


// 방법 2
// pop, shift
var isPalindrome = function(x) {
    arrX = String(x).split('');

    while (arrX.length > 1) {
        if (arrX.pop() !== arrX.shift()) {
            return false;
        }
    }

    return true;
};