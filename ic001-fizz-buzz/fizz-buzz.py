# fizz buzz python 3

for i in range(1, 101):
    fizz = ""
    buzz = ""

    if i % 3 == 0:
        fizz = "fizz"

    if i % 5 == 0:
        buzz = "buzz"

    if fizz or buzz:
        print("{0}{1}".format(fizz, buzz))
    else:
        print(i)
