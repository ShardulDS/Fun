str1 = input('Enter Passwords separated by commas: ')
lst = str1.split(', ')


def check_password(password):
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    alpha_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if len(password) < 6 or len(password) > 12:
        print('Length of password should be between 6 to 12 characters.')
    sp = '@#$'
    password_sp = []
    for i in password:
        if i in sp:
            password_sp.append(i)
            break
    else:
        print('Password must contain at least one from @ # $')
    for i in password:
        if i in alpha:
            password_sp.append(i)
            break
    else:
        print('Password must contain at least one lowercase letter.')
    for i in password:
        if i in alpha_upper:
            password_sp.append(i)
            break
    else:
        print('Password must contain at least 1 upper case letter.')
    num = '123456789'
    for i in password:
        if i in num:
            password_sp.append(i)
            break
    else:
        print('Password must contain at least one number.')
    if 6 <= len(password) <= 12 and len(password_sp) == 4:
        return 'Pass'
    else:
        return 'Fail'


correct_pass = []
for j in lst:
    if check_password(j) == 'Pass':
        correct_pass.append(j)
print(correct_pass)
