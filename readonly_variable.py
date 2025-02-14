class MyClass:
    def __init__(self, x):
        self._x = x  # Private variable

    @property
    def x(self):
        """Read-only property for x."""
        return self._x

# Example usage
obj = MyClass(10)
print(obj.x)  # Accessing x works
# obj.x = 20  # This will raise an AttributeError because x is read-only