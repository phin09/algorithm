/* https://leetcode.com/problems/remove-element/
*
* splice(startIdx, numberOfToBeRemoved)
* 삭제한 것들의 배열을 반환함
*/

// 방법 1
// splice
var removeElement = function(nums, val) {
    cnt = nums.length;
    for (i=0; i<=cnt; i++) {
        idx = nums.indexOf(val);
        if (idx > -1) {
            nums.splice(idx, 1);
        }
    }
    return nums.length;
};