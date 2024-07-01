'''
Stack Initialization: Begin by pushing the nested list items onto the stack in reverse order.
On-The-Fly Processing in hasNext: Before retrieving the next integer, we ensure the top of the stack is an integer. If it's a list, we pop it and push its items onto the stack (again, in reverse). We repeat this until we find an integer or the stack is empty.
Fetching the Next Integer: Once hasNext ensures the top of the stack is an integer, next will simply pop it.
'''
class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        def flatten(nested):
            result = []
            for ni in nested:
                if ni.isInteger():
                    result.append(ni.getInteger())
                else:
                    result.extend(flatten(ni.getList()))
            return result

        self.flattened = flatten(nestedList)
        self.index = 0

    def next(self) -> int:
        self.index += 1
        return self.flattened[self.index - 1]

    def hasNext(self) -> bool:
        return self.index < len(self.flattened)