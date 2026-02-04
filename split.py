st = "one two three four five six"
s_list = st.split(" ")
l = []
for i in range(len(s_list)):
	if i%2==0:
		l.append(s_list[i])
	else:
		l.append(s_list[i][::-1])
print(l)