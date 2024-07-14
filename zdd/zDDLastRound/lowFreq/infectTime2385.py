## https://leetcode.cn/problems/amount-of-time-for-binary-tree-to-be-infected/solutions/2753470/cong-liang-ci-bian-li-dao-yi-ci-bian-li-tmt0x
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        ans = 0
        def dfs(node: Optional[TreeNode]) -> (int, bool):
            if node is None:
                return 0, False
            l_len, l_found = dfs(node.left)
            r_len, r_found = dfs(node.right)
            nonlocal ans
            if node.val == start:
                # 计算子树 start 的最大深度
                # 注意这里和方法一的区别，max 后面没有 +1，所以算出的也是最大深度
                ans = max(l_len, r_len)
                return 1, True  # 找到了 start
            if l_found or r_found:
                # 只有在左子树或右子树包含 start 时，才能更新答案
                ## 因为有感染点。 所以就可以计算左右感染的全部时间
                ans = max(ans, l_len + r_len)  # 两条链拼成直径
                # 保证 start 是直径端点，返回拥有感染点的节点
                return (l_len if l_found else r_len) + 1, True
            return max(l_len, r_len) + 1, False
        dfs(root)
        return ans
