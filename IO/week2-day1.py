# input : 3999 이하의 로마자 문자열
# 왼쪽부터 차례로 더해나가는 게 기본이지만 IV, IX, XL, XC, CD, CM은 예외다.
# output : 입력받은 로마자를 숫자로 변환한 결과값

# 성준님 풀이
# 로마자는 큰 수가 작은 수 앞에 오는 게 기본. 예외 사항만 작은 수 + 큰 수 조합. 이를 이용하여 현재와 다음 문자를 비교해서 예외 사항에 해당하는지 아닌지 알 수 있음. 

# 내 풀이
def roman_to_num(s):
    roman = {
        'I' : 1,
        'V' : 5,
        'X' : 10,
        'L' : 50,
        'C' : 100,
        'D' : 500,
        'M' : 1000
    }
    cases = {
        'IV' : -2,
        'IX' : -2,
        'XL' : -20,
        'XC' : -20,
        'CD' : -200,
        'CM' : -200
    }
    total = sum([roman[x] for x in s])

    for i in range(len(s)-1):
        curr = s[i:i+2]
        if curr in cases:
            total += cases[curr]

    return total
