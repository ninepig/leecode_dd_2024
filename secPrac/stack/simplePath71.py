class Solution:
    '''
    只有 .. 以及 /xxx 是我们需要的 别的不需要 . 表示当前, 空格是无效
    .. 表示返回上级
    xxx是文件名
    这个题也是做一遍就要记住的
    '''
    def simplifyPath(self, path: str) -> str:
        paths = path.split("/")
        stack = []
        for item in paths:
            if item == "..":
                if stack:
                    stack.pop()
            elif item and item != '.' : # filename
                stack.append(item)

        # /xxx/xxx/xx 所以需要一个/作为开头,同时join
        return "/" + "/".join(stack)
