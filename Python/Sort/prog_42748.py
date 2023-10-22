'''
https://programmers.co.kr/learn/courses/30/lessons/42748
퀵정렬로 풂.

deepcopy를 매번 하는 건 낭비 아닐까?
'''

from copy import deepcopy

def quick_sort(array, i, j):
    left = i
    right = j
    pivot = array[(i+j)//2]
    
    while left <= right:
        while array[left] < pivot: left += 1
        while array[right] > pivot: right -= 1
        if left <= right:
            array[left], array[right] = array[right], array[left]
            left += 1
            right -= 1
            
    if i < left: quick_sort(array, i, right)
    if j > right: quick_sort(array, left, j)

def solution(array, commands):
    answer = []
    
    for item in commands:
        temp = deepcopy(array)
        quick_sort(temp, item[0]-1, item[1]-1)
        answer.append(temp[item[0]-1:item[1]][item[2]-1])
    
    return answer