
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana = dict()

        for i in strs:
            keys = ''.join(sorted(i))
            if keys not in ana:
                ana[keys] = []
            ana[keys].append(i)
        return(list(ana.values()))