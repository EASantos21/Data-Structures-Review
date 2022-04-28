class Node:
    def __init__(self, value = None):
        self.value = value 
        self.next = None 

class SLL():
    # Constructor -- Making a head and tail pointer
    def __init__(self):
        self.head = None 
        self.tail = None

    # Appending a function with tail
    def append(self, value):
        newNode = Node(value)
        # Check if the list will be empty
        if self.tail is None:
            self.head = newNode
            self.tail = newNode 

        # Append on a non-empty list
        if self.tail is not None:
            self.tail.next = newNode 
            self.tail = newNode
        
    def getHeadValue(self):
        return self.head.value

    def getTailValue(self):
        return self.tail.value

    # Printing the entire list
    def print(self):
        currNode = self.head 

        while currNode is not None:
            print(currNode.value)
            currNode = currNode.next

if __name__ == "__main__" :
    myList = SLL()

    myList.append('A')
    myList.append('B')
    myList.append('C')
    myList.print()
    print(myList.getHeadValue(), myList.getTailValue())