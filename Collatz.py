import sys

'''
Collatz Conjecture
https://en.wikipedia.org/wiki/Collatz_conjecture
'''

def main():
    print('COLLATZ CONJECTURE', '-' * 17, sep='\n')
    while True:
        try:
            number = int(input('Give me a positive integer: '))
            if number < 1:
                print('The value must be a positive integer.')
                continue
        except:
            print('You should give me a positive integer.')
            continue

        steps = 0
        while True:
            n = collatz(number)
            if n > 1:
                print(n, end=' -> ')
            else:
                print(n)
            number = n
            steps += 1
            if number == 1:
                break

        print('\nTotal steps:', steps)
        continue_ = input('\nWould you like to try again? [exit: n] ')
        if continue_.lower() == 'n':
            print('\nGoodbye!')
            sys.exit()

def collatz(n):
    return n // 2 if n % 2 == 0 else 3 * n + 1

if __name__ == '__main__':
    main()
