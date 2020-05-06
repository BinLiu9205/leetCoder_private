class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if strs is None or len(strs) == 0:
            return ""
        else:
            for i in range(0,len(strs[0])):
                char = strs[0][i]
                for j in range(1,len(strs)):
                    if i==len(strs[j]) or char!=strs[j][i]:
                        return strs[0][0:i]
                    else:
                        next
            return strs[0]
