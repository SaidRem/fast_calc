import random as rm


def main():
    print('Hello, genius!\nLets do it!')
    while True:
        n1 = rm.randint(8, 500)
        n2 = rm.randint(8, 500)
        result = n1 * n2
        print(f'{n1} * {n2}')
        
        answr = int(input('Enter your answer: -> '))
        if not answr:
            break
        else:
            if answr == result:
                print('GENIUS\nKEEP ON')
            else:
                print('You are WRONG')


if __name__ == '__main__':
    main()