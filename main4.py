try:
    try:
        print("start code")
        print(error)
        print("No errors")
    except SyntaxError:
        print("Wrong syntax!")
except NameError as error:
    print(error)