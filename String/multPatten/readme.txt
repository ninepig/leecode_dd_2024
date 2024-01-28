Trie tree的模板相对固定
        cur = self.root
        for ch in word:
            if ch not in cur.children:
                return 0 //xxxx search or insert
            cur = cur.children[ch]
        xxxxx
   逻辑都是走完这里

可以把trie 变成一个句子
这样就是 xxx  xxx xxx sentense seearch ， 每一个node里放的是一个词
参见file system


todo 336 太难了 等面经
todo 440 太难了 等面经
