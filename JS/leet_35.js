/* https://leetcode.com/problems/search-insert-position/
 *
 */

// 방법 1
// 양끝에서 하나씩 탐색
var searchInsert = function(nums, target) {
    if (nums.indexOf(target) !== -1) {
        return nums.indexOf(target);
    }

    let startIdx = 0;
    let endIdx = nums.length-1;
    if (nums[endIdx] < target) {
        return ++endIdx;
    }

    while (startIdx <= nums.length/2) {
        if (nums[startIdx] < target) {
            startIdx++;
        } else {
            return startIdx;
        }

        if (nums[endIdx] > target) {
            endIdx--;
        } else {
            return ++endIdx;
        }
    }
};


// 방법 2
// binary search
var searchInsert = function(nums, target) {
    return binarySearch(nums, target, 0, nums.length-1);
};

function binarySearch (arr, target, start, end) {
    if (start > end) return start;

    let mid = Math.floor((end + start)/2);
    if (arr[mid] === target) return mid;

    if (target < arr[mid]) {
        return binarySearch(arr, target, start, mid-1);
    } else {
        return binarySearch(arr, target, mid+1, end);
    }
}