print(
"  ___ ___   __| | ___  ___| |__   ___  ___| | _____ _ __\n"
" / __/ _ \ / _` |/ _  / __| '_ \ / _ \/ __| |/ / _ | '__\n"
"| (_| (_) | (_| |  __| (__| | | |  __| (__|   |  __| |\n"
 "\___\___/ \__,_|\___ \___|_| |_|\___|\___|_|\_\___|_|\n")
a = input("Write code you want to check...\n")
try:
    try:
        print("Checking...")
        a
        print("Congrats! There are no errors in your code!")
    except SyntaxError:
        print("Sorry, but there is some wrong syntax in your code!")
except NameError as error:
    print(error)