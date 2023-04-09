import secrets

print('Greetings user!')
print("To create a password just type what length and difficulty do you whant\
   your pass to be.\n Lenght should be from 4 to 25 characters.\n")

letters = 'QWERTYUIOPASDFGHJKLZXCVBNM'
letters_list = list(letters.lower()) + list(letters)
num_list = [str(x) for x in range(10)]
char_list = list('!@#$%^&*_-=+')
easy_list = letters_list
med_list = easy_list + num_list
dif_list = med_list + char_list


def get_pass_settings():
    while True:
        try:
            pass_len = int(input("Password length: "))
        except Exception:
            print('Type a NUMBER!!!\n')
        else:
            if pass_len > 25:
                print("Maximum password length is 25. Try again.\n")
            elif pass_len < 4:
                print("Minimum password length is 4. Try again.\n")
            else:
                break

    pass_diff = input(
        'Password difficulty (1/2/3): ')
    return pass_len, pass_diff


def generate_password(pass_len, pass_diff, count):
    password = ''
    match pass_diff.lower():
        case "1":
            for n in range(pass_len):
                password += secrets.choice(easy_list)
            print(f'Generated password №{count}: {password}')
        case "2":
            for n in range(pass_len):
                password += secrets.choice(med_list)
            print(f'Generated password №{count}: {password}')
        case "3":
            for n in range(pass_len):
                password += secrets.choice(dif_list)
            print(f'Generated password №{count}: {password}')
        case _:
            print(
                f'There is no such difficulty as {pass_diff.title()}' +
                'Try again.'
            )
    print('')
    return password


def bye(count, file):
    if count == 0:
        print('Thank you for using password generator.\n')
    elif count == 1:
        print(
            'Thank you for using password generator.\n' +
            f'You can find your {count} generated password in {file}.'
        )
    else:
        print(
            'Thank you for using password generator.\n' +
            f'You can find your {count} generated password in {file}.'
        )


def main():
    count = 0
    flag = True
    file = 'generated_passwords.txt'
    with open(file, 'w') as f:
        while flag:
            pass_len, pass_diff = get_pass_settings()
            count += 1
            password = generate_password(pass_len, pass_diff, count)
            f.write(f"{count}) {password}\n")

            if input("Continue? (yes/no) ").lower() == 'no':
                flag = False
            print('')
        bye(count, file)


if __name__ == "__main__":
    main()
