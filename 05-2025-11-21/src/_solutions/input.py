user_age = input('Please enter your age! ')
user_name = input('Please enter your name! ')
user_reg = input('Are you registered ? (True/False) ')

# Variant 1
print('Your current age is ', user_age)
print('Your name is ', user_name)
print('and your registration is ', user_reg)

# Variant 2: f string formatting
print(f'Your current age is {user_age}. Your name is {user_name} and your registration is {user_reg}')