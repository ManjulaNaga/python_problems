names = ['Alice', 'Bob', 'Charlie', 'David', 'Eve']
ages = [24, 30, 22, 35, 28]
cities = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
people_list =[{"name":n,"age":a,"city":c} for n,a,c in zip(names,ages,cities)]
print(people_list)
# Output:
# [{'name': 'Alice', 'age': 24, 'city': 'New York'}, {'name': 'Bob', 'age': 30, 'city': 'Los Angeles'}, {'name': 'Charlie', 'age': 22, 'city': 'Chicago'}, {'name': 'David', 'age': 35, 'city': 'Houston'}, {'name': 'Eve', 'age': 28, 'city': 'Phoenix'}]

