def add_sprinkles():
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return f"{result} with sprinkles"
        return wrapper
    return decorator

def add_chocolate():
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return f"{result} with chocolate"
        return wrapper
    return decorator

@add_sprinkles()
def make_ice_cream(flavor):
    return f"Ice Cream with {flavor} flavor"

# Example usage
print(make_ice_cream("strawberry"))  # Output: Ice Cream with strawberry flavor
print(make_ice_cream("vanilla"))    # Output: Ice Cream with vanilla flavor