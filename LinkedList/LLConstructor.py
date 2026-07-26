'''linked list always contains a node, and this node is used in case of append, prepend and insert.
It's good to have a class Node which can create a node when every element is passed'''

class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

my_linked_list = LinkedList(4)
print(my_linked_list.head.value)
print(my_linked_list.tail.value)

'''When the program is run, my_linked_list calls class LinkedList and passes value as 4
The default constructor init runs, the first line new_node = Node(value) calls the class Node.
so new_node.value = 4
new_node.next=None

new_node becomes like a dictionary.
new_node = {'value':4,'next':None}

my_linked_list.head = new_node = {'value':4,'next':None}
Same with my_linked_list.tail = new_node = {'value':4,'next':None}
So when we print my_linked_list.head.value we get 4'''
