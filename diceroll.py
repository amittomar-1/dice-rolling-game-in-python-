from random import randint
ques = input('Do you want to dice Y/N : ')

while ques.upper() == 'Y':
    print(f'your number is {randint(1,6)}')
    ques = input('Do you want to roll again !! (Y/N)')
else:
    print('Thank you For Playing')