# input : 여러 괄호들을 요소로 갖는 string
# 들어갈 수 있는 괄호 : '(', ')', '{', '}', '[', ']'
# 괄호를 여닫는 쌍이 맞고 괄호 순서가 유효해야 됨.
# output : 입력값이 유효한 괄호 순서인지 boolean

# 성준님 코드 참고
def is_valid(string):
    pair = {')':'(', ']':'[', '}':'{'}
    stack = []

    for i in string:
        if stack:
            if i in [')', '}', ']'] and pair[i] == stack[-1]:
                stack.pop()
                continue

        if i in ['(', '{', '[']:
            stack.append(i)
            continue
        
        return False

    return False if stack else True

# 처음 내 풀이
def is_valid(string):
    open_bracket = ['(', '{', '[']
    close_bracket = [')', '}', ']']
    stack = []

    for i in string:
        if stack:
            temp = stack.pop()
            if i in close_bracket and temp in open_bracket:
                if close_bracket.index(i) == open_bracket.index(temp):
                    continue
            stack.append(temp)
        if i in open_bracket:
            stack.append(i)
            continue
        return False

    if stack:
        return False
    return True

# 성준님 풀이
def is_valid(string):
    check = []
    for s in string:
        if len(check) > 0:
            if s == ')' and '(' == check[-1]:
                check.pop()
                continue
            if s == '}' and '{' == check[-1]:
                check.pop()
                continue
            if s == ']' anf '[' == check[-1]:
                check.pop()
                continue
        if s in ['(', '{', '[']:
            check.append(s)
        else:
            return False
    return True if len(check) == 0 else False

# 치오님 아이디어
# 실행 시간이 길다
for i in string:
    stack.append(i)
    if len(stack) > 1:
        b = stack.pop()
        a = stack.pop()
        if b in close_bracket and a in open_bracket:
            if close_bracket.index(b) == open_bracket.index(a):
                continue
        stack.append(a)
        stack.append(b)

    if stack:
        return False
    return True
