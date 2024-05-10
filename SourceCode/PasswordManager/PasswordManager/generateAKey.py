from cryptography.fernet import Fernet      #do pip install cryptography for it to work
key = Fernet.generate_key()
# encryption key
file1 = open("topSecret.key","wb")
file1.write(key)
#help
# https://www.youtube.com/watch?v=H8t4DJ3Tdrg