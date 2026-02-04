class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        list1 = list(s.strip().split(" "))
        n= len(list1)
        print(list1[n-1])

instance = Solution()
instance.lengthOfLastWord("Hello World")
instance.lengthOfLastWord("   fly me   to   the moon  ")
instance.lengthOfLastWord(" luffy is still joyboy")