class Solution:
    def reverseWords(self, s: str) -> str:
        a=s.strip().split()
        return " ".join(a[::-1])
        