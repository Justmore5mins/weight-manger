from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from base64 import b64encode,b64decode,b85encode,b85decode
from core import *
from SideCode import userinfo

class AdavancedEncryption:
    def __init__(self,user:userinfo) -> None:
        self.username = user.username
        self.password = user.password
    def new(self):
        key = RSA.generate(2048)
        with open(f"keys/{self.username}pub.pem","wb") as file:
            file.write(key.public_key().export_key(passphrase=self.password))
        with open(f"keys/{self.username}pri.pem","wb") as file:
            file.write(key.export_key(passphrase=self.password))

    def encrypt(self,data:list[bytes]):
        with open(f"keys/{self.username}pub.pem","rb") as file:
            key = RSA.import_key(file.read(),self.password)
        encrypted:list[str] = []
        cipher = PKCS1_OAEP.new(key)
        for info in data:
            encrypted.append(b64encode(cipher.encrypt(info)).decode())
        return encrypted

    def decrypt(self,data:list[bytes]):
        decrypted:list[str] = []
        with open(f"keys/{self.username}pri.pem","rb") as file:
            key = RSA.import_key(file.read(),self.password)
            cipher = PKCS1_OAEP.new(key)
        for info in data:
            decrypted.append(cipher.decrypt(b64decode(info)).decode())
        return decrypted

class EasyEncrypt:
    def __init__(self,text:str) -> None:
        self.text = bytes(text)
    
    def encrypt(self):
        return b85encode(b64encode(self.text)).decode()
    
    def decrypt(self):
        return b64decode(b85decode(self.text)).decode()