import re
from collections import defaultdict
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        dit = defaultdict(int)
        paragraph = paragraph.lower()
        paragraph = re.sub("[^a-zA-Z ]", " ", paragraph)
        for i in paragraph.split():
            if i in banned:
                continue
            dit[i] += 1
        dit = sorted(dit.items(), key=lambda x: x[1], reverse = True)
        return dit[0][0]