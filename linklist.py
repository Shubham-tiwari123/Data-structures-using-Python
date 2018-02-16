class Nodes:
    def __init__(self, data1):
        self.data = data1
        self.next = None


class Linklist:
    def __init__(self):
        self.start = None

    def addnode_last(self, data):
        new_node = Nodes(data)
        if self.start is None:
            self.start = new_node
        else:
            temp = self.start
            while temp.next:
                temp = temp.next
            temp.next = new_node

    def addnode_start(self,data):
        new_node = Nodes(data)
        new_node.next = self.start
        self.start = new_node

    def addnode_middle(self,data):
        new_node = Nodes(data)
        a = int(input("enter place to enter:-"))
        temp = self.start
        count = 0
        while count < a:
            temp1 = temp
            temp = temp.next
            count = count+1
        new_node.next = temp
        temp1.next = new_node

    def display(self):
        temp = self.start
        while temp is not None:
            print(temp.data)
            temp = temp.next

    def search(self):
        nums = int(input("enter the data to be searched:-"))
        temp = self.start
        while temp.data is not nums:
            temp = temp.next
        if temp.data is nums:
            print("data found:- ",temp.data)
        else :
            print("data not present")

    def delete_element(self):
        nums = int(input("Enter the data to be deleted:-"))
        temp = self.start
        if self.start.data is nums:
            self.start = temp.next
            temp.next=None
            del temp
        else:
            while temp.data is not nums:
                temp1 = temp
                temp = temp.next
            temp1.next = temp.next
            temp.next = None
            del temp


l = Linklist()
num = int(input("Enter number of nodes to enter:-"))
for i in range(num):
    input_data = int(input("Enter the number:-"))
    l.addnode_last(input_data)

l.display()
print("Adding in the start:-")
l.addnode_start(45)
l.display()
print("Adding in the middle:-")
l.addnode_middle(40)
l.display()
l.search()
l.delete_element()
l.display()
