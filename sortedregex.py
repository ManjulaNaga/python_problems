##input:a4b3c2
##output:aaaabbbcc

s = input("Enter the compressed string: \n")
ans=''
l = len(s)
i=1
while(i<l):
    j=0
    while(j<int(s[i])):
        ans = ans +s[i-1]
        j += 1
    i += 2

ans = "".join(sorted(ans))
print(ans)