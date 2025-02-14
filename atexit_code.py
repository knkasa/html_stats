import atexit

def goodbye():
    print("Goodbye, program is exiting!")

atexit.register(goodbye)
print("Hello, program is running!")