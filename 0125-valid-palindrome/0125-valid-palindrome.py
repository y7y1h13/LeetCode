class Solution:
    def isPalindrome(self, s: str) -> bool:
        p = re.sub(r'[^A-Za-z0-9]',"", s.lower())
        print(p)
        head = 0
        tail = len(p) - 1
        for i in range(tail // 2 + 1):
            if p[head] != p[tail]:
                return False
            head += 1
            tail -= 1
        return True