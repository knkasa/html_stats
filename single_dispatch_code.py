# When a function input can have different types, use singledispatch.

from functools import singledispatch

@singledispatch
def process(data):
    print("Default processing")

@process.register
def _(data: int):
    print("Processing integer")

process("text")
process(5)