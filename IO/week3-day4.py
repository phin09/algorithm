# input : 숫자 배열
# input에 있는 모든 0을 뽑아서 배열의 마지막으로 이동
# 새로운 배열을 생성하지 말 것.
# output : 숫자 배열

def move_zeros(nums):
    for _ in range(len(nums)):
        nums.append(nums.pop(nums.index(0)))
    return nums

# input 숫자 배열의 길이만큼 for문을 돌 필요는 없어 보여서 수정한 코드
def move_zeros(nums):
    for _ in range(nums.count(0)):
        nums.append(nums.pop(nums.index(0)))
    return nums
        
