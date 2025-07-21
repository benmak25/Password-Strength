print('Insert Password')
pwd = input()
min_length = 12
cap_char_count = 0
num_count = 0


for char in pwd:
    if char.isalpha():
        if char.isupper():
            cap_char_count += 1
    elif char.isnumeric():
            num_count += 1

pwd_check = (len(pwd) >= min_length) and (cap_char_count >= 1) and (num_count >= 1)

if pwd_check:
    print('Password is Strong')
else:
    print('Password is Weak, Missing the following conditions:')
    if(len(pwd) < min_length):
        print('- Needs to be at least 8 Characters long')
    if (cap_char_count < 1):
        print('- Needs at least 1 capital letter')
    if (num_count < 1):
        print('- Needs at least 1 number')




