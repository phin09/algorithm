'''
https://programmers.co.kr/learn/courses/30/lessons/42747
퀵정렬로 풂.
'''

def quick_sort_reverse(array, i, j):
    left = i
    right = j
    pivot = array[(i+j)//2]
    
    while left <= right:
        while array[left] > pivot : left += 1
        while array[right] < pivot : right -= 1
            
        if left <= right:
            array[left], array[right] = array[right], array[left]
            left += 1
            right -= 1
            
    if i < right: quick_sort_reverse(array, i, right)
    if left < j: quick_sort_reverse(array, left, j)

def solution(citations):
    if len(citations) == 1 and citations[0] != 0:
        return 1
    
    quick_sort_reverse(citations, 0, len(citations)-1)
    
    for i in range(0, len(citations)-1):
        if i+1 <= citations[i] and i+1 >= citations[i+1]:
            return i+1
        
    if len(citations) <= citations[-1]:
        return len(citations)
        
    return 0