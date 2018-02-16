MyQueue = []
class Queue:

    def DisplayQueue(self):
        print("queue currently contains:")
        for Item in MyQueue:
            print(Item)
    def Push(self,Value):
        if len(MyQueue) < num:
            MyQueue.append(Value)
        else:
            print("queue is full!")
    def Pop(self):
        if len(MyQueue) > 0:
            MyQueue.pop(0)
        else:
            print("queue is empty.")

q = Queue()
num = int(input("Enter the size of queue:-"))
for i in range(num):
    value = int(input("Enter the number:-"))
    q.Push(value)
q.Push(45)
q.DisplayQueue()
q.Pop()
print("After poping an element from queue:-")
q.DisplayQueue()