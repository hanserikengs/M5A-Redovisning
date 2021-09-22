def flippblipp(n):
    output = ""
    if n % 3 == 0:
        if n % 5 == 0:
            return "Flipp Blipp"
        else:
            return "Flipp"
    if n % 5 == 0:
        return "Blipp"
    else:
        return str(n)


def game():
    n = 1
    print("       1")
    n += 1
    while True:
        if input("Nästa: ").lower() != flippblipp(n).lower():
            print("Fel! " + flippblipp(n))
            break
        else:
            n += 1
    print("\nGame Over!")

game()