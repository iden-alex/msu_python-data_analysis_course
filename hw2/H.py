from collections import deque


class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.data = value
    def insert(self, value):
        if self.data is None:
            self.data = value
        else:
            if value < self.data:
                if self.left is None:
                    self.left = Node(value)
                else:
                    self.left.insert(value)
            elif value > self.data:
                if self.right is None:
                    self.right = Node(value)
                else:
                    self.right.insert(value)
        return
    def search(self, value):
        if self.data is None:
            return False
        if self.data == value:
            return True
        elif value < self.data:
            if self.left is None:
                return False
            else: 
                return self.left.search(value)
        else:
            if self.right is None:
                return False
            else:
                return self.right.search(value)
            
class BinarySearchTree:
    def __init__(self, root_val = None):
        self.root = Node(root_val)
    def append(self, value):
        self.root.insert(value)
    def __contains__(self, value):
        return self.root.search(value)
    def __iter__(self):
        queue = deque()
        queue.append(self.root)
        while queue:
            cur = queue.popleft()
            if (cur is not None) and (cur.data is not None):
                yield cur.data
            if cur.left is not None:
                queue.append(cur.left)
            if cur.right is not None:
                queue.append(cur.right)
