#===============================================================================
# 이중 연결 리스트를 이용하여 스택(Stack) 클래스 구현하기
#===============================================================================

from DList import *

class StackUnderFlow(Exception):
    pass

class Stack(DList): # DList를 상속받아 정의한다.
    # 스택에 새 항목을 추가하는 연산
    def push(self, value):
        self.insertFront(value)

    # 스택의 맨 위에 있는 데이터를 가져오는 연산
    def pop(self):
        if self.isEmpty():
            raise StackUnderFlow("Stack Empty!!")
        returnValue = self.head.data
        self.remove(self.head)
        return returnValue

    # 스택의 맨 위에 있는(top) 항목의 값을 읽어만 오는 (제거하지 않음) 연산
    def peak(self):
        if self.isEmpty():
            raise StackUnderFlow("Stack Empty!!")
        return self.head.data
#===========================================================================================
# 괄호 문자열(st)을 입력받아 매칭이 제대로 되어 있는지를 확인하고 결과를 반환한다.
# 반환값은 True, False
# 사용 가능한 괄호: (), <>, {}, []  입력 예: "{(<>[])}", "{<()}"
    def checkParenthese(st):
        print(f"검사할 문자열: {st}")

        pleft = "(<{["
        pright = ")>}]"
        paris = ["()", "<>", "{}", "[]"]
        
        stack = Stack()

        for ch in st:
            if ch in pleft:
                stack.push(ch)
            elif ch in pright:
                if stack.isEmpty():
                    print(f"매칭 오류 발생: {ch}")
                    return False
                item = stack.pop()
                if (item + ch) not in paris:
                    print(f"매칭 오류 발생: {item} {ch}")
                    return False

        if not stack.isEmpty():
            print("닫히지 않은 괄호가 남아 있습니다.")
            return False

        return True

#===========================================================================================
# st = Stack()
# st.push(100)
# st.push(200)
# st.push(300)
# st.show()
# print(st.pop())
# st.show()
# print(st.peak())
# st.show()

# st.checkParenthese("({<><>[]})")