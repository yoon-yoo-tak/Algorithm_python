
from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def dfs(index, path):
            if len(path) == len(digits): # 다 골랐으면
                result.append(path)      # 리스트에 추가 하고
                return                   # 끝
            for i in range(index, len(digits)): # 아직 다 안골랐으면
                for j in dic[digits[i]]:        # 숫자에 해당하는 문자들에 대해
                    dfs(i + 1, path + j)        # dfs로 탐색

        if not digits:
            return []

        dic = {"2" : "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        result = []
        dfs(0, "")
        return result


