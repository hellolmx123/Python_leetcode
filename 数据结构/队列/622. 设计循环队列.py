class MyCircularQueue:

    def __init__(self, k: int):
        self.Queue = [0] * (k + 1)
        self.pre = 0
        self.cur = 0
        self.l = k + 1

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.Queue[self.pre] = value
        self.pre = (self.pre + 1) % self.l
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.cur = (self.cur + 1) % self.l
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.Queue[(self.pre - 1) % self.l]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.Queue[self.cur]

    def isEmpty(self) -> bool:
        if self.cur == self.pre:
            return True

    def isFull(self) -> bool:
        if (self.pre + 1) % self.l == self.cur:
            return True

obj = MyCircularQueue(k = 3)
obj.enQueue(1)
obj.enQueue(2)
obj.enQueue(3)
obj.enQueue(4)
a = obj.Rear()
print(a)
obj.isFull()
obj.deQueue()
obj.enQueue(4)
b = obj.Rear()
print(b)