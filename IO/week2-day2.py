# inupt : 숫자 요소를 갖는 배열
# 과반수가 넘은 숫자를 반환. 가정으로 입력 배열의 길이는 무조건 2개 이상이라 되어있지만 test.py를 보면 길이가 1인 input도 있다. 그리고 가정으로 써있지는 않지만 test.py를 보면 과반수가 넘는 숫자가 없는 경우가 없다... 일단 가정에는 없으니 None 처리를 해줬다.
# 과반수라는 조건을 만족하는 요소는 딱 1개 나오는 거니까 조건 만족시 바로 return 함. 만일 majority 조건이었다면 만족하는 요소가 여러개일 수 있으니 입력 배열 전체를 확인해야 됨.
# output : 과반수가 넘은 숫자

def more_than_half(nums):
    for x in set(nums):
        if nums.count(x) > len(nums)//2:
            return x
    return None
