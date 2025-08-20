# When a function input can have different types, use singledispatch.
# If the input variable "data" is int type, it will run _ function.

from functools import singledispatch

@singledispatch
def process(data):
    print("Default processing")

@process.register
def _(data: int):
    print("Processing integer")

process("text")

process(5)
