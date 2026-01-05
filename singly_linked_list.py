class Node:
    def __init__(self,data):
        self.data = data
        self.address = None
class Linkedlist:
    def __init__(self):
        self.head = None
    """ 
        traversal in singly linked list
        1. if linked list is empty -> if head == None
        2. if it is not empty -> if head!= None
    """
    def traverse(self):
        if self.head is None:
            return None
        else:
            n = self.head
            while n is not None:
                value = n.data
                print(value, "---->")
                n = n.address #get the address to next data
    def add_beginning(self,data):
        new_node = Node(data)
        new_node.address = self.head
        self.head = new_node
        print(self.head.data)
        
    def add_end(self,data): #point new node -> 
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.address is not None:
                temp = temp.address
            temp.address = new_node
    def add_in_between(self,data,target):
        new_node = Node(data)
        temp = self.head
        while temp is not None:
            if target == temp.data:
                break
            temp = temp.address
        if temp is None:
            return None
        else:
            new_node.address = temp.address
            temp.address = new_node
    def add_after(self,data,target):
        if self.head is None:
            return None
        if self.head.data == target:
            new_node = Node(data)
            new_node.address = self.head
            self.head = new_node
            return
        
        #get previous, add new node after prev
        while temp.address is not None:
            temp = self.head
            if temp.address.data == target:
                break
            temp = temp.address
        if temp.address is None:
            return None
        else:
            new_node = Node(data)
            new_node.address = temp.address
            temp.address = new_node
            
            
                
                
            
            
            
        
        
         
            
            
            

ll1 = Linkedlist()  
ll1.add_beginning(10)
ll1.add_beginning(100)
ll1.add_end(1)  
ll1.traverse()   
# def single_linked_list():


    
    