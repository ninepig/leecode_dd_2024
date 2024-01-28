class Solution:
    '''这道题无论是对 dfs 还是bst的理解都是非常好的题
    1 如果val 在左侧, 我们去左边删除节点. 返回的是root
    2 如果val 在右侧 ,我们去右侧删除节点, 返回的是root
    3 如果val是当前节点
        1 节点左侧没有节点 , 返回右侧子节点
        2 节点右侧没有节点, 返回左侧节点 这
        3 节点左右都有, 把左侧节点挂在右侧节点的最左边(bst 原理 非常巧妙)
    4 dfs 返回的当前的新的root # 这个看代码理解
    '''
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root :
            return root
        if key < root.val:
            root.left = self.deleteNode(root.left,key) # 走左侧,返回的是左侧的头
            return root
        elif key > root.val:
            root.right =self.deleteNode(root.right,key)
            return root
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                # 把node左侧接到node右侧最左边,返回的node右侧 ,整个左子树挂到右侧的动作, 非常牛. 同时维护了bst的性质
                cur = root.right
                while cur:
                    cur = cur.left
                cur.left = root.left
                return root.right
