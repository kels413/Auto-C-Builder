import sys


def check_script():
    if len(sys.argv) > 2:
         print(f"Error: Usage: {sys.argv[0]} <name of script>")
    elif len(sys.argv) != 2:
        print("you have to pass a script")
    else:
        print(sys.argv)


# open the file and write into it.

with open(sys.argv[1], "w") as file:
    name = "kelly\n"
    file.write(name)
print("data written", sys.argv[1])


if __name__ == "__main__":
    check_script()
