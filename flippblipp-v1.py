n = int(input("Ange värde n: "))
for x in range(1, n+1):
    output = ""
    if x % 3 == 0:
        output = ("Flipp ")
    if x % 5 == 0:
        output = output + ("Blipp")
    if output == "":
        print(str(x))
    else:
        print(output)