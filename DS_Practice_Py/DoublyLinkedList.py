class Node:
    def __init__(self, value = None):
        self.head = None
        self.next = None 
        self.prev = None 
        self.value = value 

class DLL:
    def __init__(self):
        self.head = None 
        self.tail = None 

    def append(self, value):
        currNode = self.head 
        newNode = Node(value)
        # Checks whether list is empty or not
        if self.head is None:
            self.head = newNode 
            self.tail = newNode

        # If list is not empty then we append
        while currNode is not None:
            if currNode.next is None:
                self.tail.next = newNode
                newNode.prev = currNode 
                self.tail = newNode 
                break 
            else:
                currNode = currNode.next
    
    def getHeadValue(self):
        return self.head.value

    def getTailValue(self):
        return self.tail.value

    def print(self):
        currNode = self.head 

        while currNode is not None:
            print(currNode.value)
            currNode = currNode.next

if __name__ == "__main__":
    myList = DLL()

    myList.append('A')
    myList.append('B')
    myList.append('C')
    myList.print()
