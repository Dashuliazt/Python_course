login_in = input('Are you registered? (Type enter \'YES\' or \'NO\')').upper()
if login_in == 'YES':
    with open('users.txt', 'w+') as file:
        users = file.read().split()
        login_user = input('Your login:')
        pass_user = input('Your password:')
        if login_user in users:
            print('Your welcome!')
        else:
            register_in = input(
                'Are you registrated now? (Type enter \'YES\' or \'NO\')').upper()
            if register_in == 'YES':
                login_user = input('Please enter you login:')
                pass_user = input('Please enter you password:')
                registr_f = open('users.txt', 'w+')
                registr_f.write(login_user + '-' + pass_user)
else:
    print('Have a nice day')