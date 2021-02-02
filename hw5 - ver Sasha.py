def encrypt(filename, filename_before, key=1):
    with open(f'{filename}.txt') as file, \
        open(f'{filename_after}.txt', 'w', encoding="utf-8") as file1:
        file1.write(
            ''.join(list(map(lambda x: chr(ord(x)+key), file.read())))
        )


def decrypt(filename, filename_after, key=1):
    with open(f'{filename}.txt') as file, \
        open(f'{filename_after}.txt', 'w', encoding="utf-8") as file1:
        file1.write(
            ''.join(list(map(lambda x: chr(ord(x)-key), file.read())))
        )


def check_file(filename):
    try:
        with open(f'{filename}.txt') as file:
            return True
    except FileNotFoundError:
        return False


def check_key(new_key):
    try:
        int(new_key)
        return True
    except ValueError:
        return False


def main():
    while True:
        question = input('1.Encrypt \n2. Decrypt \n3. Exit')
        if question in '123':
            if question == '1':
                filename_for_encrypt = input('Enter name file for encrypt')
                new_key = input('Enter key for cezar')
                if check_file(filename_for_encrypt) and check_key(new_key):
                    name_file_after = input('Enter name file after encrypt')
                    encrypt(filename_for_encrypt,
                            name_file_after,
                            key=int(new_key))
                    break
                else:
                    print('file for encrypt or key incorrect')
                    continue
            if question == '2':
                filename_for_decrypt = input('Enter name file for encrypt')
                new_key = input('Enter key for cezar')
                if check_file(filename_for_decrypt) and check_key(new_key):
                    name_file_after = input('Enter name file after encrypt')
                    decrypt(filename_for_decrypt,
                            name_file_after,
                            key=int(new_key))
                    break
            else:
                break
        else:
            print('Try again')
            continue

main()