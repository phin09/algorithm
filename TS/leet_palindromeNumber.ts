// https://leetcode.com/problems/palindrome-number/

// Runtime: 2ms
function isPalindrome(x: number): boolean {
    if (x < 0) return false;
    if (0 <= x && x <= 9) return true;
    if (10 <= x && x/10 == 0) return false;

    let invertedX = 0;

    for (let tempX = x; tempX > 0; tempX = Math.floor(tempX/10)) {
        invertedX = invertedX * 10;
        invertedX = invertedX + tempX % 10;
    }

    if (invertedX == x) return true;
    return false;
};


// 이하 다른 사람의 코드. 위와의 차이 파악하기
// Runtime: 1ms
function isPalindrome(originalX: number): boolean {
    // Requirement: Solve without converting number to string

    // Deal with exceptions
    if (originalX < 0) {
        return false
    }

    // Create a reversed version of X
    let x = originalX;
    let reversedX = 0;

    while (x > 0) {
        const lastDigit = x % 10;

        // Multiply by 10 so we can simply add the next unit later
        // Example: 8 * 10 = 80; then 80 + 9 = 89
        reversedX *= 10;
        reversedX += lastDigit;

        const numberWithoutLastDigit = Math.floor(x / 10);
        x = numberWithoutLastDigit;
    }

    // Compare both versions
    return originalX === reversedX;
};

isPalindrome(123);