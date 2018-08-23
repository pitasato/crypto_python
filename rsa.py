from Crypto.PublicKey import RSA

rsa_keys = RSA.generate(1024)

pub_key = rsa_keys.publickey()

encrypted = pub_key.encrypt("tajne scisle", "klucz szyfrujacy")

rsa_keys.decrypt(encrypted)

print encrypted


