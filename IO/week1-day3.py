# input : 문자열
# [leeetcode 링크](https://leetcode.com/problems/longest-substring-without-repeating-characters/)
# [참고 링크](https://minu94.tistory.com/5)
# 적합한 풀이가 생각나지 않아 같은 문제를 다른 언어도 푼 사람의 방법을 참고했다.
# output : length of the longest substring without repeating characters

# 코드카타 repl.it이 정지된 상태라 일단 풀어놓고 나중에 확인해야 됨. 

def get_len_of_str(s):
    window = []
    max_len = 0
    temp_len = 0
    for i in s:
        if i in window:
            if max_len < temp_len:
                max_len = temp_len
            while s[i] in window:
                window.pop(0)
        window.append(i)
        temp_len += 1

    return max_len
