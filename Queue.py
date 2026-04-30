#======================================================================
# 이중 연결 리스트를 활용하여 큐(queue) 구현하기
#======================================================================
from DList import *

class QueueUnderFlow(Exception):
    pass

class Queue(DList):
    def add(self, value):
        self.append(value)

    def remove(self):
        if self.isEmpty():
            raise QueueUnderFlow("Queue is Empty!!")
        else:
            returnValue = self.head.data
            super().remove(self.head)
            return returnValue

#======================================================================
q = Queue()
q.add(100)
q.add(200)
q.add(300)
print(q.remove())
print(q.remove())
print(q.remove())
print(q.remove())


