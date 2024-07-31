print('enter your name: ')
name = input()
print()

if name == 'rama':
    print('hey rama, how are you?')
elif name == 'krishna':
    print('hey, i know you are the mr. krishna!')
else:
    print('hey, welcome mr. '+name+'!')

print('\nenter your age:')
age = input()
if age:
    print('\nthanks for the age confirmation.')
    if int(age) > 18:
        print('your age is ' + age + ' greater than 18 years, so you can access the content.' )
    elif int(age) == 18:
        print('hey kid, you have to wait to turn your age more than 18 years.')
    else:
        print('hey kid, you are not allowed to access the content.')
else:
    print('you are not entered any data, thank you.')

print('\nDone')
