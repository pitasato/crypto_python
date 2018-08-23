import Crypto
from Crypto.PublicKey import RSA
from Crypto.Cipher import DES

# Generate Private Key
private = RSA.generate(1024)
m = open('python\\crypt\\mykey.pem','w')
m.write(private.exportKey('PEM'))
m.close()