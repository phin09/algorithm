# input : 문자열이 요소로 담긴 리스트
# 입력받은 리스트 안의 요소들의 공통된 시작 단어(prefix)를 반환
# output : string

# 치오님 풀이 참고
# 입력 배열을 정렬하고 맨앞, 맨뒤 요소만 뽑아 쓴 게 좋아보인다.
def get_prefix(strs):
  if len(strs) == 0:
    return ''
  
  # strs = sorted(strs)
  strs.sort()
  
  i = 0
  while True:
    try:
      if strs[0][i] != strs[-1][i]:
        break
    except:
      break
    i += 1

  return strs[0][:i]


# 내 풀이 - not pythonic...
def get_prefix(strs):
  temp_zero = [x[0] for x in strs]
  if len(strs) == 0 or len(set(temp_zero)) > 1:
    return ''

  i = 1
  while True:
    try:
      word_lst = [x[i] for x in strs]
    except:
      break
    if len(set(word_lst)) > 1:
      break
    i += 1

  return strs[0][:i]
