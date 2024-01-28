class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        phone_dict = {
            "2" : "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        res = []

        def backtrack(path, index):
            if index == len(digits):
                res.append(path)
            else:
                digits = phone_dict[digits[index]]
                backtrack(path + digits,index + 1)

        backtrack('',0)
        return res


class Solution:
    def letterCombinations2(self, digits: str) -> List[str]:
        if not digits:
            return []

        phone_dict = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        def backtrack(combination, index):
            if index == len(digits):
                combinations.append(combination)
            else:
                digit = digits[index]
                for letter in phone_dict[digit]:
                    backtrack(combination + letter, index + 1)

        combinations = list()
        backtrack('', 0)
        return combinations