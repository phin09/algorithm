/* https://leetcode.com/problems/two-sum/

배열 길이
(O) arr.length
(X) arr.length()

배열 내 특정 요소 check
(O) arr.includes(target)
(X) target in arr

Map
Map object에 key-value pair 넣기: map.set(key, value)
Map object에서 key로 value 가져오기: map.get(key)
Map object 내 특정 value check: map.has(target)
*/

// 방법 1
// 단순 이중for문
var twoSum = function(nums, target) {
    for (i=0; i < nums.length ; i++) {
        for (j=i+1; j < nums.length; j++) {
            if (nums[i] + nums[j] == target) {
                return [i, j];
            }
        }
    }
};


// 방법 2
// 속도도 메모리도 나은 점이 없음
var twoSum = function(nums, target) {
    for (i=0; i < nums.length ; i++) {
        num = target - nums[i]
        if (nums.slice(i+1).includes(num)) {
            return [i, i+1+nums.slice(i+1).indexOf(num)];
        }
    }
};


// 방법 3
// Map
var twoSum = function(nums, target) {
    let map = new Map();
    for(let i = 0; i < nums.length; i ++) {
        if(map.has(target - nums[i])) {
            return [map.get(target - nums[i]), i];
        } else {
            map.set(nums[i], i);
        }
    }
};
