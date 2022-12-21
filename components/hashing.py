from  passlib.context import CryptContext


crypt_pwd=CryptContext(schemes=["bcrypt"])

class Hash:
    def encrypt(password):
        return crypt_pwd.hash(password)
    
    def decrypt(plain_password,hashedpassword):
        crypt_pwd.verify(plain_password, hashedpassword)