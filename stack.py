MyStack = []
class Stack:

    def displayStack(self):
        print("Stack currently contains:")
        for Item in MyStack:
            print(Item)

    def Push(self,Value):
        if len(MyStack) < num:
            MyStack.append(Value)
        else:
            print("Stack is full!")
    def Pop(self):
        if len(MyStack) > 0:
            MyStack.pop()
        else:
            print("Stack is empty.")

s = Stack()
num = int(input("Enter the size of stack:-"))
for i in range(num):
    value = int(input("Enter the number:-"))
    s.Push(value)
s.Push(45)
s.displayStack()
s.Pop()
print("After poping an element from stack:-")
s.displayStack()