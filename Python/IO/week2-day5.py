# input : 요소가 두개 이상인 숫자 배열
# 임의의 요소 두개 간의 인덱스 차이와 둘 중 작은 요소를 곱한 값
# output : 가장 큰 결과 값

def get_max_area(height):
    max_value = 0

    for i in range(len(height)-1):
        for j in range(i+1, len(height)):
            if height[i] < height[j]:
                value = height[i] * (j-i)
            else:
                value = height[j] * (j-i)

            if max_value < value:
                max_value = value

        return max_value
