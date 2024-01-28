class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        final_list = []
        # 拼接起来 记住空格
        mega_word = " ".join(words)
        # 如果出现2次 就说明是子字符串
        for word in words:
            if mega_word.count(word) > 1:
                final_list.append(word)

        return final_list
