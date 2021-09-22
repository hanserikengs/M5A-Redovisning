def flippblipp(n):
    output = ""
    if n % 3 == 0:
        output = ("Flipp ")
    if n % 5 == 0:
        output = output + ("Blipp")
    if output == "":
        return str(n)
    else:
        return(output)

n = int(input("Ange värde n: "))
for x in range(1, n+1):
    print(flippblipp(x))