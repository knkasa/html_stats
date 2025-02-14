# Notify when dataframe has been modified.

import pandas as pd

class NotifyDataFrame:
    def __init__(self, df):
        self._df = df

    def __getattr__(self, item):
        # Delegate attribute access to the underlying DataFrame
        return getattr(self._df, item)

    def __setitem__(self, key, value):
        # Override __setitem__ to notify when the DataFrame is modified
        print("DataFrame modified!")
        self._df[key] = value

    def __getitem__(self, key):
        # Delegate __getitem__ to the underlying DataFrame
        return self._df[key]

    def __repr__(self):
        # Delegate __repr__ to the underlying DataFrame
        return self._df.__repr__()

    def __eq__(self, other):
        # Delegate __eq__ to the underlying DataFrame
        return self._df.__eq__(other)

    # You can override other methods that modify the DataFrame as needed

class MyClass:
    def __init__(self, df):
        self.df1 = NotifyDataFrame(df)
        self.df2 = self.df1

# Example usage
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
my_class = MyClass(df)

# Modifying self.df2 will notify that self.df1 is modified
my_class.df2['C'] = [7, 8, 9]  # This will print "DataFrame modified!"

print(my_class.df1)