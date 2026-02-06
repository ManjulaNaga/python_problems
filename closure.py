# def make_counter():
#     count = 99  # This variable is "enclosed"

#     def incrementer():
#         nonlocal count  # Declare as non-local to modify the outer scope variable
#         count += 1
#         print(count)
#         return count

#     return incrementer  # Return the inner function (the closure)

# # Usage:
# counter_closure = make_counter()
# print(counter_closure()) # Output: 1
# print(counter_closure()) # Output: 2

class Counter:
    #def __init__(self):
    count = 0

    def increment(self):
        self.count += 1
        return self.count

# Usage:
counter_instance = Counter()
print(counter_instance.increment()) # Output: 1
print(counter_instance.increment()) # Output: 2
