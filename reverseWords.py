class Solution:
    def reverseWords(self, s: str) -> str:
        ar_str = list(s.split())
        print(ar_str)
        ans = ar_str[::-1]
        print(" ".join(ans))

instance = Solution()
res= instance.reverseWords("the sky is blue")