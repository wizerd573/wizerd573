
import time

def count(*args):
    def myfunc(func):
        # print(args)
        n = time.time()
        func(args)
        gap = time.time() - n
        print("Duration %s" % gap)
        def nirob(*args):
            return func(args)
        nirob(args)
        print("Duration %s" % gap)
        def kamrul(*args):
            return func(args)
        kamrul(args)
        def masum(*args):
            return func(args)
        masum(args)
        gap = time.time() - n
        print("take time %s" % gap)
        # print(gap)
    return myfunc
@count(45)
def print_hello(*args):
    print(args)
    for _ in range(10):
        print("Hello")
print_hello

# def nothing(func):


n = time.time()
gap = time.time() - n
@count(1, 10)
def piku(*args):
    # n = time.time()
    # gap = time.time() - n
    # print("Duration %s" % gap)
    print(args)
    for _ in range(6):
        print("an")
    print("Duration %s" % gap)
    def alu(*args):
        print(args)
    for _ in range(3):
        print("alu")
piku
# print_hello()

