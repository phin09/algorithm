// https://leetcode.com/problems/longest-common-prefix/

// Runtime: 1ms
function longestCommonPrefix(strs: string[]): string {
    let shortestStr = '';
    let maximumLengthOfCommonPrefix = 200;

    for (const str of strs) {
        if (maximumLengthOfCommonPrefix < str.length) continue;

        shortestStr = str;
        maximumLengthOfCommonPrefix = str.length;
    }

    if (!maximumLengthOfCommonPrefix) return '';

    let lengthOfCommonPrefix = maximumLengthOfCommonPrefix;

    for (const str of strs) {
        for (let index = 0; index < maximumLengthOfCommonPrefix; index++) {
            if (str[index] != shortestStr[index]) {
                if (index < lengthOfCommonPrefix) lengthOfCommonPrefix = index;
                break;
            }
        }
    }

    return shortestStr.slice(0, lengthOfCommonPrefix);
};

// 이하 다른 사람의 코드. 위와의 차이 파악하기
// Runtime: 0ms
function longestCommonPrefix(strs) {
    let prefix = strs[0];

    for (let i = 1; i < strs.length; i++) {
        while (!strs[i].startsWith(prefix)) {
            prefix = prefix.slice(0, -1);
        }

        if (prefix === '') {
            return prefix;
        }
    }

    return prefix;
};