"""
value structure --- Tree
"""
from __future__ import absolute_import, print_function, division

from collections import deque

class Solution:

    def __init__(self):
        self.values = []
        self.array = None

    def preorderTraversal(self, node):
        if node is None:
            return
        else:
            self.values.extend(node.value)
            self.preorderTraversal(node.left)
            self.preorderTraversal(node.right)
    
    def midorderTreacersal(self, node):
        if node is None:
            return
        else:
            self.midorderTreacersal(node.left)
            self.values.extend(node.value)
            self.midorderTreacersal(node.right)

    def postorderTreacersal(self, node):
        if node is None:
            return
        else:
            self.postorderTreacersal(node.left)
            self.postorderTreacersal(node.right)
            self.values.extend(node.value)
    
    def leverorder(self, node):
        '''
            二叉树层序遍历， 借助队列的数据结构，先进先出的是popleft()函数
        '''
        q = deque()
        q.append(node)
        tree_value = []
        while len(q) > 0:
            tmp_node = q.popleft()
            tree_value.append(tmp_node.value)
            if tmp_node.left is not None:
                q.append(tmp_node.left)
            if tmp_node.right is not None:
                q.append(tmp_node.right)
        return tree_value

    def sawtooth_order(self, node):
        flag = 1
        q = deque()
        tree_value = []
        if node is not None:
            q.append(node)
        else:
            raise Exception('node is None!')
        while len(q) > 0:
            tmp_value = q.popleft()
            tree_value.append(tmp_value.value)
            if flag == 0:
                if tmp_value.right is not None:
                    q.append(tmp_value.right)
                if tmp_value.left is not None:
                    q.append(tmp_value.left)
                flag = 1
            else:
                if tmp_value.left is not None:
                    q.append(tmp_value.left)
                if tmp_value.right is not None:
                    q.append(tmp_value.right)
                flag = 0
        return tree_value

    '''
    二叉树的顺序存储
    根节点position: n, 左子树：2*n+1, 右子树：2*n+2
    '''
    def tree2array(self, root, len):
        self.array = [None] * len
        self.__toArrar(root, 0)

    def __toArrar(self, node, pos):
        if node is None:
            return
        self.array[pos] = node.value
        self.__toArrar(node.left, 2*pos + 1)
        self.__toArrar(node.right, 2*pos + 2)

    '''
    二叉树最小深度
    '''
    def min_depth(self, node):
        if node is None:
            return 0
        if node.left is not None:
            if node.right is not None:
                return self.__min(self.min_depth(node.left), self.min_depth(node.right)) + 1
            else:
                return self.min_depth(node.left)
        elif node.right is not None:
            return self.min_depth(node.right) + 1
        else:
            return 1

    def __min(self, a, b):
        if a>=b:
            return b
        else:
            return a

    '''
    二叉树最大深度
    '''
    def max_depth(self, node):
        if node is None:
            return 0
        else:
            return self.__max(self.max_depth(node.left), self.max_depth(node.right)) + 1

    def __max(self, a, b):
        if a >= b:
            return a
        else:
            return b
    
    '''
    判断二叉树是否相同
    '''
    def isSampleTree(self, treeA, treeB):
        if treeA is None:
            return treeB is None
        if treeB is None:
            return False
        return (treeA.value == treeB.value) and self.isSampleTree(treeA.left, treeB.left) \
                and self.isSampleTree(treeA.right, treeB.right)


class TreeNode:

    def __init__(self, val=None, left=None, right=None):
        self.value = val
        self.left = left
        self.right = right

if __name__ == '__main__':
    '''
            D
        B       E
      A   C   G
                 F
    '''
    # 构建树
    tree = TreeNode('D', 
        TreeNode('B', TreeNode('A'), TreeNode('C')), \
        TreeNode('E', TreeNode('G', right=TreeNode('F'))))
    solution = Solution()
    print('前序遍历：')
    solution.preorderTraversal(tree)
    print(solution.values)
    print('中序遍历：')
    solution.values = []
    solution.midorderTreacersal(tree)
    print(solution.values)
    print('后序遍历：')
    solution.values = []
    solution.postorderTreacersal(tree)
    print(solution.values)
    print('层序遍历：')
    values = solution.leverorder(tree)
    print(values)
    print('二叉树的顺序存储：')
    solution.tree2array(tree, 16)
    print(solution.array)
    print("二叉树最小深度：")
    print(solution.min_depth(tree))
    print("二叉树最大深度：")
    print(solution.max_depth(tree))
    print("判断二叉树是否相等")
    treeB = TreeNode('D', \
        TreeNode('B', TreeNode('A'), TreeNode('C')), \
        TreeNode('E', TreeNode('G', right=TreeNode('F'))))
    print(solution.isSampleTree(tree, treeB))
    print("sawtooth order:")
    print(solution.sawtooth_order(tree))