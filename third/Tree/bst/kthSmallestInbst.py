def kthSmallest_dfs_early_stopping(self, root, k):
	res = []
	def _inorder(node):
		if not node: return
		_inorder(node.left)
		if len(res) == k:
			return
		res.append(node.val)
		_inorder(node.right)
	_inorder(root)
	return res[-1]