/* https://leetcode.com/problems/remove-duplicates-from-sorted-array/
 *
 * idx+1 이 ++idx 보다 빠름
 */

// 방법 1
// 중복 삭제
var removeDuplicates = function(nums) {
    let idx = 0;

    while (idx < nums.length) {
        if (nums[idx] === nums[idx+1]) {
            nums.splice(idx, 1);
        } else {
            idx++;
        }
    }

    return idx+1;
};

// 방법 2
// 삭제하지 않음
var removeDuplicates = function(nums) {
    let idx = 0;

    for (i=0; i<nums.length; i++) {
        if (nums[idx] !== nums[i]) {
            nums[++idx] = nums[i];
        }
    }

    return idx+1;
};