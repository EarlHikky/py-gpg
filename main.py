import argparse

import gnupg
import pyperclip


# with open('/Users/earl/Library/Mobile Documents/com~apple~CloudDocs/my_private_key.asc') as f:
#     key_data = f.read()
# import_result = gpg.import_keys(key_data)


def main():
    gpg = gnupg.GPG(gnupghome='')
    # gpg.encoding = 'utf-8'
    parser = argparse.ArgumentParser(description='gpg encrypt')
    parser.add_argument('file', help='encrypted file')
    path_file = parser.parse_args().file
    # decrypt file
    with open(path_file, 'rb') as enc_file:
        dec_data = gpg.decrypt_file(enc_file)
    if not dec_data.ok:
        print(dec_data.problems)
    pyperclip.copy(dec_data.data.strip().decode('UTF-8'))
    print(dec_data.status)


if __name__ == '__main__':
    main()
