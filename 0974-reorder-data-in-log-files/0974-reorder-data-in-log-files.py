class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        alph = list()
        num = list()

        for i in logs:
            if i.split()[1].isdigit():
                num.append(i)
            else:
                alph.append(i)
        alph.sort(key= lambda x : (x.split()[1:], x.split()[0]))
        return alph + num