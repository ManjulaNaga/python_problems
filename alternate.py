s1 = "This is the best example."
s2 = "Ramaya Ramabhadraya Ramachandraya Vedase."
s1 = "Ramaya"
s2 = "Ramachandraya"
s3 = ""
i,j=0,0
while i < len(s1) or j < len(s2):
    if i < len(s1):
        s3 = s3 + s1[i]
        i += 1
    if j < len(s2):
        s3 = s3 + s2[j]
        j += 1
print(s3)