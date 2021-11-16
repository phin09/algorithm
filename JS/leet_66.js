/** https://leetcode.com/problems/plus-one/
 */

// 방법 1
// 속도는 빠르지만 가독성 그닥
var plusOne = function(digits) {
    let len = digits.length;
    let end;

    for (i=0; i<len; i++) {
        end = digits.pop();
        if (end !== 9) {
            digits.push(end+1);
            break;
        }
    }

    let temp = len - digits.length;
    if (temp === len) digits.push(1);
    else digits.push(digits.pop())+1;

    for (i=0; i<temp; i++) {
        digits.push(0);
    }

    return digits;
};


// 방법 2
// 깔끔. 속도는 그닥
var plusOne = function(digits) {
    for (i=digits.length-1; i>=0; i--) {
        if (digits[i] === 9) {
            digits[i] = 0;
        } else {
            digits[i]++;
            return digits;
        }
    }

    digits.unshift(1);
    return digits;
};