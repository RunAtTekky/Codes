try:
    with open("hello.py", "r") as f:
        content = f.read()
except:
    print("The file you are trying to access does not exist.")
