import sys


print(dir(sys))

if not sys.argv:
    print("you have to pass a script")
else:
    print(sys.argv)
