import random
n = int(input('Enter upper bound of range (1 to ?): '))
a = input('Do you want a random number ?: ')
if a == 'Yes':
    print('Your random number is '+str(random.randint(1, n))+'.')
else:
    print('Okay')

lower = 1
upper = n
index = (lower + upper) // 2
print('Is it '+str(index)+' ?')
b = input()
while b[-2:] != 'es':
    if b[-2:] == 'ow':
        if upper-lower == 1:
            print("It's "+str(upper)+'.')
            print('I feel defeated.')
            break
        else:
            lower = index
            index = (lower + upper) // 2
            print('Is it '+str(index)+' ?')
            b = input()
    elif b[-3:] == 'igh':
        if upper-lower == 1:
            print("It's "+str(lower)+'.')
            print('I feel defeated.')
            break
        else:
            upper = index
            index = (lower + upper) // 2
            print('Is it ' + str(index) + ' ?')
            b = input()
else:
    print('Yeah! Got it!')
