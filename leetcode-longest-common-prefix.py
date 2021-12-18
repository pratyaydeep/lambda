# 1st Form
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        all_equal = lambda x: len(set(x))==1
        takewhile = __import__('itertools').takewhile
        return ''.join([x[0] for x in  takewhile(all_equal , zip(*strs))])


# Final Form
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        return ''.join([x[0] for x in  __import__('itertools').takewhile(lambda x: len(set(x))==1 , zip(*strs))])
