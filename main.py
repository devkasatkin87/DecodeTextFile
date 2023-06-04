import pyAesCrypt

path = 'data.txt'

# Ввол пароля пользователем
password = input('Please enter password for encrypt file')

#ecrypt
# pyAesCrypt.encryptFile(path, path.split('.')[0] + '.aes', password)

#decrypt
pyAesCrypt.decryptFile('data.aes', 'decrypted.txt', password)