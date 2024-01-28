class Solution:
    '''bfs
    对于complete二叉树 只要出现为空一次 就不能再出现空节点.利用直接加入queue的小技巧'''
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        queue = [root]
        is_exist = True
        while queue:
            size = len(queue)
            for i in range(size):
                cur_node = queue.pop(0)
                if not cur_node:
                    is_exist = False
                # 如果不为空的情况
                else:
                    if not is_exist : # if we have seen flag, one more node
                        return False
                    queue.append(cur_node.left)
                    queue.append(cur_node.right)

        return True