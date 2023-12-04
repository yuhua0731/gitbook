# Tree traversal order

## **DFS**

### Inorder(left, root, right)

```python
 # recursive
 def inorder(root):
     return  inorder(root.left) + [root.val] + inorder(root.right) if root else []
 ​
 # iterating
 def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
     ans = []
     curr = []
     # append and pop elements from the end of curr list
     while True:
         while root:
             curr.append(root.left)
             root = root.left
         if not root: return ans
         temp = curr.pop()
         ans.append(temp.val)
         root = temp.right
     return ans
```

### Preorder(root, left, right)

```python
 # recursive
 def preorder(root):
     return [root.val] + preorder(root.left) + preorder(root.right) if root else []
 ​
 # iterating
 def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
     if not root: return []
     ans = []
     curr = deque([root])
     while curr:
         temp = curr.popleft()
         ans.append(temp.val)
         if temp.right: curr.appendleft(temp.right)
         if temp.left: curr.appendleft(temp.left)
     return ans
```

### Postorder(left, right, root)

```python
 # recursive
 def postorder(root):
     return  postorder(root.left) + postorder(root.right) + [root.val] if root else []
 ​
 # iterating, this is a reverse order of (root, right, left)
 def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
     if not root: return []
     ans = []
     curr = deque([root])
     while curr:
         temp = curr.popleft()
         ans.append(temp.val)
         if temp.left: curr.appendleft(temp.left)
         if temp.right: curr.appendleft(temp.right)
     return ans[::-1]
```

