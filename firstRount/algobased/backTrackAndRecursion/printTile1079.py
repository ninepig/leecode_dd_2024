'''
给定一个代表活字字模的字符串 tiles，其中 tiles[i] 表示第 i 个字模上刻的字母。

要求：返回你可以印出的非空字母序列的数目。

**注意：**本题中，每个活字字模只能使用一次
'''
import collections


class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        helper_dict = dict() ## 如果用defaultdict 就不需要这么做
        for title in tiles:
            if title not in helper_dict:
                helper_dict[title] = 1
            else:
                helper_dict[title] += 1
        # helper_dict2 =collections.defaultdict()
        # for title in tiles:
        #     helper_dict2[title] += 1

        # 每个活字字模只能使用一次
        ans = 0
        def backtrack():
            nonlocal ans
            for key,value in helper_dict.items():
                if value == 0:
                    return # can not be used
                ans += 1 # 每次都可以加1
                helper_dict[key] -= 1 # reduce one
                backtrack()
                helper_dict[key] += 1

        return ans

class SolutionAns:
    ans = 0
    def backtrack(self, tile_map):
        for key, value in tile_map.items():
            if value == 0:
                continue
            self.ans += 1
            tile_map[key] -= 1
            self.backtrack(tile_map)
            tile_map[key] += 1

    def numTilePossibilities(self, tiles: str) -> int:
        tile_map = dict()
        for tile in tiles:
            if tile not in tile_map:
                tile_map[tile] = 1
            else:
                tile_map[tile] += 1

        self.backtrack(tile_map)

        return self.ans