s = input("enter a alphanumeric string:\n")
alphabet=[]
digit=[]
for ch in s:
    if ch.isalpha():
        alphabet.append(ch)
    else:
        digit.append(ch)
res = ''.join(sorted(alphabet) + sorted(digit))
print(res)