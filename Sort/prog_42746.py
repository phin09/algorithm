'''
https://programmers.co.kr/learn/courses/30/lessons/42746
퀵정렬로 풂.

버블 정렬, 셰이커 정렬로는 시간 초과.
'''

def compare_two_numbers(num1, num2):
    if str(num1) + str(num2) > str(num2) + str(num1):
        return True
    return False


def quick_sort(array, i, j):
    left = i
    right = j
    pivot = array[(i+j)//2]
    
    while left <= right:
        while compare_two_numbers(array[left], pivot): left += 1
        while compare_two_numbers(pivot, array[right]): right -= 1
        if left <= right:
            array[left], array[right] = array[right], array[left]
            left += 1
            right -= 1
    
    if i < right: quick_sort(array, i, right)
    if left < j: quick_sort(array, left, j)


def solution(numbers):
    quick_sort(numbers, 0, len(numbers)-1)
                
    answer = ''
    for i in numbers:
        answer += str(i)
        
    return answer.lstrip('0') if answer.lstrip('0') else '0'