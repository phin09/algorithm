# input : 숫자를 요소로 갖는 배열 nums와 숫자 k
# nums에 등장한 빈도가 높은 순으로 숫자 k 개를 담은 배열을 반환
# output : 숫자를 요소로 갖는 배열

def top_k(nums, k):
    temp_lst = []

    for i in set(nums):
        temp_lst.append((i, nums.count(i)))

    count_lst = sorted(temp_lst, key=lambda x:-x[-1])

    return [j[0] for j in count_lst[:k]]
