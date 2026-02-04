#dict2.py
names =['Alice', 'Bob', 'Charlie', 'David', 'Eve']
grades = [85, 92, 78, 90, 88]
student_list=[{"name":n,"grade":g} for n, g in zip(names,grades)]
students_sorted=sorted(student_list, key=lambda x:x['grade'], reverse=True)
print(students_sorted)
