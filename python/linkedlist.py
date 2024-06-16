class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
    
    def push(self, new_val):
        new_node = Node(new_val)
        new_node.next = self.head
        self.head = new_node
    
    def insertAt(self,prev_node, new_val):
        if prev_node is None:
            print("Previous node seems to be empty")
        
        new_node = Node(new_val)
        new_node.next = prev_node.next
        prev_node.next = new_node
    
    def append(self, new_val):
        new_node = Node(new_val)
        if self.head is None:
            self.head = new_node
            return
        
        last_node = self.head
        while(last_node.next):
            last_node = last_node.next
        
        last_node.next = new_node
        
    def printlist(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next
            
if __name__ == '__main__':
    llist = LinkedList()
    llist.append(3)
    llist.push(4)
    llist.insertAt(Node(3),5)
    llist.printlist()