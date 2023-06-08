import rsa

# generate public and private keys with
# rsa.newkeys method,this method accepts
# key length as its parameter
# key length should be atleast 16
publicKey, privateKey = rsa.newkeys(512)

# this is the string that we will be encrypting
message = ['112223','sarath','mahesh',"dharan"]

# rsa.encrypt method is used to encrypt
# string with public key string should be
# encode to byte string before encryption
# with encode method
empty=[]
for i in message:
	encMessage = rsa.encrypt(i.encode(),
						publicKey)

	print("original string: ", message)
	print("encrypted string: ", encMessage)
	empty.append(encMessage)
	print('ho',empty)
	# x=empty

for i in  empty:
 decMessage = rsa.decrypt(i, privateKey).decode()

 print("decrypted string: ", decMessage)

# the encrypted message can be decrypted
# with ras.decrypt method and private key
# decrypt method returns encoded byte string,
# use decode method to convert it to string
# public key cannot be used for decryption

