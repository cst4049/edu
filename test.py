#测试代码（基本结构粗略模型）
from enum import Enum
class burTree:
    #知识的树型结构
    def __init__(self,rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self,newNode):
        if self.leftChild == None:
            self.leftChild = burTree(newNode)
        else:
            t = burTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self,newNode):
        if self.rightChild == None:
            self.rightChild = burTree(newNode)
        else:
            t = burTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t

    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self,obj):
        self.key = obj

    def getRootVal(self):
        return self.key


###枚举类型
class structenum(Enum):
    choice = 1
    fillin = 2
    textinput = 3
    anwser = 4


r = burTree('a')
r.insertLeft("b")
r.insertRight("c")
