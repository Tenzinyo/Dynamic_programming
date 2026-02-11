from collections import deque
class TreeNode:
    def __init__(self,left,val,right):
        self.val = val 
        self.left = left 
        self.right = right
    def __str__(self):
        return str(self.val)
    
    def pre_order(node):
        """
                        1 
                        
                2               3
                
            4       5       10
            
            DFS -> [1,2,4,5,3,10]
            
        """
        if not node:
            return 
        curr = node
        pre_order(curr.val)
        pre_order(curr.left)
        pre_order(curr.right)
        return curr
    #iterative
    def pre_order_iterative(node):
        stack = [node]
        result = []
        while stack:
            node =stack.pop()
            result.append(node)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return result
    def bfs_bst(node):
        queue = deque()
        queue.append(node)
        result = []
        while queue:
            curr = queue.popleft()
            result.append(curr)
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
        return result
    
    
    def search(node,target): # O(n) space = O(n)
        if not node:
            return
        if node.val == target:
            return True
        
        return search(node.left,target) or search(node.right,target)
    
                
                    
                
        def bst(node,target): # O(log(n)) space = O(1)
            queue = deque()
            queue.append(node)
            while queue:
                curr = queue.popleft()
                if curr>target:
                    if curr.right:
                        queue.append(curr.right)  
                elif curr<target:
                    if curr.left:
                        queue.append(curr.left)   
                elif curr == target:
                    return True
        
        