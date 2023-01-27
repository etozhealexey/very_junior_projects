def main():
    while True:
        num = input("What number are you thinking of? [1-1000] ")
        num = isnum_1_1000(num)
        if num:
            resultado = "It's an "
            resultado += "even" if num%2 == 0 else "odd"
            seguir = input(resultado + " number!\nCan you enter another number? [y/n]: ")
            if seguir.lower() == 'n':
                print("You have left the game. Goodbye!")
                break
        else:
            print("You must enter an integer number between 1 and 1000.")

def isnum_1_1000(n):
    if n.isdigit():
        n = int(n)
        if 1 <= n <= 1000:
            return n
    return None

if __name__ == "__main__":
    main()
