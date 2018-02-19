class Nodes:
    def __init__(self, data1):
        self.data = data1
        self.next = None


class Linklist:
    def __init__(self):
        self.start = None

    def addnode(self, data):
        new_node = Nodes(data)
        if self.start is None:
            self.start = new_node
        else:
            temp = self.start
            while temp.next:
                temp = temp.next
            temp.next = new_node

    def display(self):
        temp = self.start
        while temp is not None:
            print(temp.data)
            temp = temp.next

    def swapNodes(self, x, y):

        if x == y:
            return

        temp1 = None
        temp2 = self.start
        while temp2 != None and temp2.data != x:
            temp1 = temp2
            temp2 = temp2.next

        temp3 = None
        temp4 = self.start
        while temp4 != None and temp4.data != y:
            temp3 = temp4
            temp4 = temp4.next

        if temp2 == None or temp4 == None:
            return

        if temp1 != None:
            temp1.next = temp4
        else:
            self.start = temp4

        if temp3 != None:
            temp3.next = temp2
        else:
            self.start = temp2

        temp = temp2.next
        temp2.next = temp4.next
        temp4.next = temp

l = Linklist()
num = int(input("Enter number of nodes to enter:-"))
for i in range(num):
    input_data = int(input("Enter the number:-"))
    l.addnode(input_data)

l.display()
print("after swaping values:-")
l.swapNodes(2,1)
l.display()
