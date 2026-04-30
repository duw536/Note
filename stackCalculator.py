스택이랑 쿼리 임포트하기

"""
23.3 + (34 * 123) / 456.43
["23.3", "+", "(", "34", "*", "123", ")", "/", "456.63"]
"""
from Stack import *

# 중위 표기법으로 표현된 수식 문자열을 토큰단위로 쪼개서 리스트에 저장한다.
def toTokens(strInfix):
    chList = list(strInfix) # 입력 문자열을 문자단위로 쪼개서 리스트에 저장한다.
    ops = "+-*/()"
    nums = "0123456789."
    tokenList = []  # 토큰으로 분리된 문자열을 저장했다가 반환할 리스트
    numToken = ""   # 수 토큰으로 분리할 문자들 묶어 나갈 변수, (초기값은 빈 문자열)
    
    while chList:   # chList에 글자가 남아있으면 반복한다.
        ch = chList.pop(0)  # chList에서 맨 앞에 있는 문자를 하나 꺼낸다.
        if ch in ops:
            tokenList.append(ch)
        elif ch in nums:
            numToken += ch  # numToken 일단 저장한다.
            while chList:   # 수 토큰을 완성하기 위한 반복
                if chList[0] in nums:
                    numToken += chList.pop(0)
                else:
                    break
            tokenList.append(float(numToken))
            numToken = ""
        else:
            continue
    return tokenList
#-------------------------------------------------------------------------------------------------------------------------------------
# 중위 표기 수식을 후위이 표기로 변환 연습문제 중위 표기법 (infix notation) 순서로 저장된 토큰 리스트를 입력받아서 후위 표기법 (postfix notation) 순서로 저장된 queqe를 반환한다.
def infix2postfix(1stInfix)
    stack = Stack()
    queue = Queue()
    pass
#-------------------------------------------------------------------------------------------------------------------------------------

token = toTokens("1+2+(2*5.3)+1.4*251.5/3.4")
print(token)
queue = infix2postfix(tokens)
        
    

