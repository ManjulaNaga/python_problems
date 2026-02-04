##input: aaaabbbccz
##output: 4a3b2c1z

s = input("Enter the expanded string format: \n")
ans =''
count = 1
l = len(s)  #10
for i in range(l):
    if(i+1 <l):
        if s[i] == s[i+1]:
            count += 1
            
        else:
            ans = ans + str(count) + s[i]
            count = 1
    if i == l-1:
        ans = ans + str(count) + s[i]
print(ans)