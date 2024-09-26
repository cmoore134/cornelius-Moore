password = input('please Enter a new password:')
new_password = ""

for char in password:
    if char == 'o':
        new_password += '0'
    elif char == 'i':
        new_password += '1'
    elif char == 'a':
        new_password += '@'
    elif char == 'e':
        new_password += '3'
    elif char == 'A':
        new_password += '4'
    elif char == 'B':
        new_password += '8'
    elif char == 's':
        new_password += '$'
    else:
        new_password += char

new_password += "!"

print('your new strong password is:',new_password)