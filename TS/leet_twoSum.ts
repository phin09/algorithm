// https://leetcode.com/problems/two-sum/

// Runtime: 3ms
function twoSum(nums: number[], target: number): number[] {
    const indexRecord: Record<string, number> = {};

    for (const i in nums) {
        const index = +i
        const num = nums[index]

        if (num in indexRecord) return [indexRecord[num], index];
        indexRecord[`${target - num}`] = index;
    }
};

// 이하 다른 사람의 코드. 위와의 차이 파악하기
// Runtime: 0ms
function twoSum(nums: number[], target: number): number[] {
    const map = new Map<number, number>();
    for(let i = 0; i < nums.length; i++) {
        const res = target - nums[i]
        if(map[res] != undefined) return [map[res], i];
        map[nums[i]] = i
    }

    return []
};
