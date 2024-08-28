#this the program says the hello world and ask for the name

print('Hello World!')

print()
print('What is your name?')
myName = input()        #ask for the name
print('Its good to meet you Mr. '+ myName + '.')
print('The length of your name is: ' + str(len(myName)))

print()
print('What is your age: ')
myAge = input()         #ask for the age
print('Your will be '+ str(int(myAge) + 1) + ' in a year.')

print()
print('Thank you...')
