class Solution:
    def romanToInt(self, num: int) -> str:
        result = ""
        ct = 0
        value = { 1000 : "M", 900 : "CM", 500 : "D", 400 : "CD",  100 : "C",90 : "XC", 50 : "L", 40 : "XL", 10 : "X", 9 : "IX",  5 : "V", 4:"IV", 1 : "I"}
        for k,v in value.items():
            ct = num//k
            if ct > 0:
                result += (ct * v )
            num = num % k
        return result 
                
instance = Solution()
print(instance.romanToInt(3750))
print(instance.romanToInt(58))
print(instance.romanToInt(1994))