'''
If a node is root (has no parent) and isn't deleted,
when will we add it to the result.
https://leetcode.com/problems/delete-nodes-and-return-forest/solutions/328853/java-c-python-recursion-solution
'''
class Solution:
    '''
    更新左儿子（右儿子）为递归左儿子（右儿子）的返回值。
如果当前节点被删除，那么就检查左儿子（右儿子）是否被删除，如果没被删除，就加入答案。
如果当前节点被删除，返回空节点，否则返回当前节点。
最后，如果根节点没被删除，把根节点加入答案。


    '''
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        ans = []
        s = set(to_delete)
        def dfs(node: Optional[TreeNode]) -> Optional[TreeNode]:
            if node is None: return None
            node.left = dfs(node.left)
            node.right = dfs(node.right)
            if node.val not in s: return node
            if node.left: ans.append(node.left)
            if node.right: ans.append(node.right)
            return None
        if dfs(root): ans.append(root)
        return ans

