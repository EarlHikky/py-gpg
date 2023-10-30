import argparse

import gnupg
import pyperclip


def main():
    gpg = gnupg.GPG()
    parser = argparse.ArgumentParser(description='gpg encrypt')
    parser.add_argument('filename', help='encrypted filename')
    filename = parser.parse_args().filename
    path_file = f'/Users/earl/.password-store/{filename}.gpg'
    try:
        with open(path_file, 'rb') as enc_file:
            dec_data = gpg.decrypt_file(enc_file)
        if not dec_data.ok:
            print(dec_data.problems)
        pyperclip.copy(dec_data.data.strip().decode('UTF-8'))
        print(dec_data.status)
    except FileNotFoundError:
        print('wrong filename or file doesn\'t exists:', path_file)


if __name__ == '__main__':
    main()
