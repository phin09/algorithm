/* https://leetcode.com/problems/sqrtx/
 *
 * 제곱근은 1부터 x/2+1 사이에 있음
 */

// 방법 1
// 느림
var mySqrt = function(x) {
    if (x < 1) return 0;
    if (1 <= x && x < 4) return 1;

    let seed = 2;
    while (true) {
        if (x == seed*seed) return seed;
        else if (seed*seed < x) seed = seed*seed;
        else break;
    }

    for (i=seed; i>=2; i--) {
        if (x >= i*i) return i;
    }
};


// 방법 2
// binary search
var mySqrt = function(x) {
    let left = 1;
    let right = x/2 +1;
    let mid;

    while (left <= right) {
        mid = Math.floor((left+right)/2);
        if (mid*mid < x) left = mid+1;
        else if (x < mid*mid) right = mid-1;
        else return mid;
    }
    return right;
};