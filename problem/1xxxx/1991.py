#전위 순회 preorder traversal 노드 -> 왼 -> 오
#중위 순회 inorder traversal 왼 -> 노드 -> 오
#후위 순회 postorder traversal 왼 -> 오 -> 노드 


class Node:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right

def preorder(node):
    print(node.data, end = '')
    if node.left != '.':
        preorder(tree[node.left])
    if node.right != '.':
        preorder(tree[node.right])

def inorder(node):
    if node.left != '.':
        inorder(tree[node.left])
    print(node.data, end = '')
    if node.right != '.':
        inorder(tree[node.right])

def postorder(node):
    if node.left != '.':
        postorder(tree[node.left])
    if node.right != '.':
        postorder(tree[node.right])
    print(node.data, end = '')

N = int(input())
tree = dict()

for i in range(N):
    data, left, right = input().split()
    tree[data] = Node(data, left, right)
    
preorder(tree['A'])
print()
inorder(tree['A'])
print()
postorder(tree['A'])
