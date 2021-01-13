# Represent a node of the singly linked list  
class Node:  
    def __init__(self,data):  
        self.data = data  
        self.next = None  
          
class SortList:  
    # Represent the head and tail of the singly linked list  
    def __init__(self):  
        self.head = None
        self.tail = None  
          
    # addNode() function will add a new node to the list  
    def addNode(self, data):  
        # Create a new node  
        newNode = Node(data)  
          
        # Checks if the list is empty  
        if(self.head == None):  
            # If list is empty, both head and tail will point to new node  
            self.head = newNode  
            self.tail = newNode  
        else:  
            # newNode will be added after tail such that tail's next will point to newNode  
            self.tail.next = newNode;  
            # newNode will become new tail of the list  
            self.tail = newNode  
              
    # sortList() will sort nodes of the list in ascending order  
    def sortList(self):  
        # Node current will point to head  
        current = self.head  
        index = None  
          
        if(self.head == None):  
            return;  
        else:  
            while(current != None):  
                # Node index will point to node next to current  
                index = current.next;  
                  
                while(index != None):  
                    # If current node's data is greater than index's node data, swap the data between them  
                    if(current.data > index.data):  
                        temp = current.data  
                        current.data = index.data  
                        index.data = temp  
                    index = index.next  
                current = current.next  
                  
    # display() function will display all the nodes present in the list  
    def display(self):  
        # Node current will point to head  
        current = self.head;  
        if(self.head == None):  
            print("List is empty")  
            return;  
        while(current != None):  
            # prints each node by incrementing pointer  
            print(current.data),  
            current = current.next 
        print (" ")  
   
sList = SortList()  
          
# adding data to the list  
sList.addNode(13)  
sList.addNode(4)  
sList.addNode(2)  
sList.addNode(5)  
sList.addNode(6)  
   
# displaying original list  
print("Original list: ") 
sList.display()  
  
# Sorting list  
sList.sortList()  
   
# displaying sorted list  
print("Sorted list: ")  
sList.display()  