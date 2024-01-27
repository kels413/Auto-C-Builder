import sys


def check_script():
    if len(sys.argv) > 2:
         print(f"Error: Usage: {sys.argv[0]} <name of script>")
    elif len(sys.argv) != 2:
        print("you have to pass a script")
    else:
        print(sys.argv)


# open the file and write into it.

with open()



if __name__ == "__main__":
    check_script()
