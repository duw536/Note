from Queue import *
#===========================================================================================================
# 이진 트리 (Binary Tree)
# 노드의 자식 수가 2인(degree가 2인) 트리
#===========================================================================================================
class BTree:
    def __init__(self, value):
        self.key = value
        self.left = None    # 생성되는 노드의 왼쪽 서브트리는 초기에는 없으므로 None
        self.right = None   # 생성되는 노드의 오른쪽 서브트리는 초기에는 없으므로 None
    #-----------------------------------------------------------------------------------------------------
    def __str__(self):
        return f"[{self.key}]"
    #-----------------------------------------------------------------------------------------------------
    # 노드 자신과 왼쪽 자식, 오른쪽 자식 노드의 관계를 함께 표현하는 문자열 반환하기
    def node(self):
        return f"{self.left}<-{self}->{self.right}"
    #-----------------------------------------------------------------------------------------------------
    # 노드의 왼쪽과 오른쪽 자식 노드를 지정하여 연결한다.
    def children(self, leftChild, rightChild):
        self.left = leftChild
        self.right = rightChild
    #-----------------------------------------------------------------------------------------------------
    # 전위순회  (preoreder traversal)
    # 1. 노드 자신 먼저 방문 (방문 -> 출력)
    # 2. 왼쪽 서브 트리 방문 
    # 3. 오른쪽 서브 트리 방문 
    def preOrder(self):
        print(self, end="")                 # 1. 현재 노드 먼저 방문(출력)
        if self.left:                       # 2. 왼쪽 자식 노드가 있으면 
            self.left.preOrder()            # 왼쪽 서브 트리에도 같은 방문 연산 처리 
        if self.right:                      # 3. 오른쪽 자식 노드가 있으면  
            self.right.preOrder()           # 오른쪽 서브 트리에도 같은 방문 연산 처리
    #-----------------------------------------------------------------------------------------------------
    # 중위순회  (inorder traversal)
    # 1. 왼쪽 서브 트리 방문 (방문 -> 출력)
    # 2. 노드 자신 방문 
    # 3. 오른쪽 서브 트리 방문 
    def inOrder(self):
        if self.left:                       # 1. 왼쪽 자식 노드가 있으면 
            self.left.inOrder()             # 왼쪽 서브 트리에도 같은 방문 연산 처리 
        print(self, end="")                 # 2. 현재 노드 먼저 방문(출력)
        if self.right:                      # 3. 오른쪽 자식 노드가 있으면  
            self.right.inOrder()            # 오른쪽 서브 트리에도 같은 방문 연산 처리
    #-----------------------------------------------------------------------------------------------------
    # 후위순회  (postorder traversal)
    # 1. 왼쪽 서브 트리 방문 (방문 -> 출력)
    # 3. 오른쪽 서브 트리 방문 
    # 2. 노드 자신 방문 
    def postOrder(self):
        if self.left:                       # 1. 왼쪽 자식 노드가 있으면 
            self.left.postOrder()           # 왼쪽 서브 트리에도 같은 방문 연산 처리 
        if self.right:                      # 2. 오른쪽 자식 노드가 있으면  
            self.right.postOrder()          # 오른쪽 서브 트리에도 같은 방문 연산 처리
        print(self, end="")                 # 3. 현재 노드 먼저 방문(출력)
    #-----------------------------------------------------------------------------------------------------
    # 레벨 순회 (levelorder traversal)
    # 레벨이 증가하는 순서대로, 왼쪽에서 오른쪽 순서대로 방문하는 것
    def levelOrder(self):
        #방문 순서를 정하기 위한 queue를 생성한다.
        queue = Queue()
        queue.add(self) #방문 예약을 위해 queue에 자신을 먼저 저장한다.

        while not queue.isEmpty():      # 방문해야 할 대상 노드가 queue에 남아 있으면 계속한다.
            node = queue.remove()       # queue에서 다음 방문할 노드를 꺼낸다.
            print(node, end="")         # 위에서 꺼낸 노드를 방문(출력)한다.
            if node.left:               # 현재 노드의 왼쪽 자식 노드가 있으면
                queue.add(node.left)    # 방문 예약 줄(queue)에 뒤에 가서 서도록 한다.
            if node.right:              # 현재 노드의 오른쪽 자식 노드가 있으면
                queue.add(node.right)   # 방문 예약 줄(queue)에 뒤에 가서 서도록 한다.
        print("")
    #-----------------------------------------------------------------------------------------------------
    # 트리의 노드 개수를 계산하여 반환
    def nodeCount(self):
        count = 1                           
        if self.left:                       
            count += self.left.nodeCount()  
        if self.right:                      
            count += self.right.nodeCount() 
        return count 
    #-----------------------------------------------------------------------------------------------------
    # self 노드를 root로 하는 이진트리의 높이를 계산하여 반환한다.  (재귀함수로 구현한다.)
    # 반환값: 왼쪽 서브트리의 height와 오른쪽 서브트리의 height 중에 큰 값 + 1(자신) 
    def height(self):
        if self.left is None and self.right is None:
            return 1
        if self.left is None:
            return 1 + self.left.height()
        if self.right is None:
            return 1 + self.right.height()
        return max(self.left.height(), self.right.height()) + 1
    #-----------------------------------------------------------------------------------------------------
    # 주어진 노드를 루트로 하는 트리가 완전 이진 트리인지 여부를 확인하여 true false 로 반환 #힌트 levelOrder로 접근 
    def isComplete(self):
        pass
    #-----------------------------------------------------------------------------------------------------
    # 주어진 노도를 루트로 하는 트리가 포화 이진 트리인지 여부를 확인하여 True False로 반환 count와 heifht만 계산하면 답 나옴
    def isPerfect(self):
        pass
#===========================================================================================================
def countsNodes(btree):
    if btree is None:
        return 0
    else:
        return 1 + countsNodes(btree.left) + countsNodes(btree.right);
#===========================================================================================================

nodeA = BTree("A")
nodeB = BTree("B")
nodeC = BTree("C")
nodeD = BTree("D")
nodeE = BTree("E")
nodeF = BTree("F")
nodeG = BTree("G")
nodeH = BTree("H")
nodeI = BTree("I")
nodeJ = BTree("J")
nodeK = BTree("K")
#------------------------------------------------------------------------------------------------------------
nodeA.children(nodeB, nodeC)
nodeB.children(nodeD, nodeE)
nodeC.children(nodeF, nodeG)
nodeD.children(nodeH, nodeI)
nodeE.children(nodeJ, nodeK)

# nodeA.preOrder()
# nodeA.inOrder()
# nodeA.postOrder()
nodeA.levelOrder()
# print(nodeA.nodeCount())
# print(countsNodes(nodeA))
print(nodeG.height())