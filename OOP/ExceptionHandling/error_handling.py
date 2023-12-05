def error_handling():
    try:
        print(1/0)
    except:
        print("Something bad happened")

error_handling()