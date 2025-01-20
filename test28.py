class Node :
    def __init__(self,value):
        self.value = value
        self.right = None
        self.left = None
class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self,value):
        new_node= Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while True :
              if new_node.value == temp.value:
                  return False
              if new_node.value < temp.value:
                  if temp.left is None:
                      temp.left = new_node
                      return True
                  temp = temp.left
              else :
                  if temp.right is None:
                      temp.right = new_node
                      return True
                  temp = temp.right
    def contains(self,value):
        if self.root is None :
            return False
        temp =self.root
        while temp is not None:
            if temp.value ==value :
                return True
            elif temp.value > value :
                temp = temp.left
            else :
                temp = temp.right
        return False


my_BST = BinarySearchTree()
my_BST.insert(6)
my_BST.insert(1)
my_BST.insert(9)

print(my_BST.root.value)
print(my_BST.root.left.value)
print(my_BST.root.right.value)

print(my_BST.contains(10))