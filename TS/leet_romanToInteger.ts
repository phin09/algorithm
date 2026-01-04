// https://leetcode.com/problems/roman-to-integer/

// Runtime: 7ms
function romanToInt(s: string): number {
    const romanMap: Record<string,number> = {
        'I' : 1,
        'V' : 5,
        'X' : 10,
        'L' : 50,
        'C' : 100,
        'D' : 500,
        'M' : 1000,
    };

    const valueList: number[] = [];

    for (const letter of s) {
        const currentValue = romanMap[letter];
        const previousValue = valueList.at(-1);

        if (previousValue && previousValue < currentValue) {
            const valueToSubtract = valueList.pop();
            valueList.push(-valueToSubtract);
        }

        valueList.push(currentValue);
    }

    const sum = valueList.reduce((acc, curr) => {return acc+curr;}, 0);
    return sum;
};


// 이하 다른 사람의 코드. 위와의 차이 파악하기
// Runtime: 1ms
function romanToInt(s: string): number {
    const romanMap: Record<string, number> = {
        I: 1,
        V: 5,
        X: 10,
        L: 50,
        C: 100,
        D: 500,
        M: 1000
    };

    let sum = 0;

    for (let i = 0; i < s.length; i++) {
        const current = romanMap[s[i]];
        const next = romanMap[s[i + 1]];

        if (current < next) {
            sum -= current;
        } else {
            sum += current;
        }
    }

    return sum;
};