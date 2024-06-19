from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP,AES
from Crypto.Random import get_random_bytes
from base64 import b64encode,b64decode
from core import *

class AdavancedEncryption:
    def __init__(self,user:Mangement) -> None:
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

class EasyEncryption:
    def __init__(self,text:str,salt:bytes = get_random_bytes(32)) -> None:
        self.text = text
        self.salt = salt

    def encrypt(self) -> tuple[int,int,bytes]:
        """
        Returns encrypted, tag and nonce
        """
        cipher = AES.new(self.salt,AES.MODE_EAX)
        encrypted, tag = cipher.encrypt(bytes(self.text))
        nonce = cipher.nonce
        return encrypted,tag,nonce,self.salt
    
    def decrypt(self,nonce:bytes|str,tag:int):
        if type(nonce) == str:
            nonce =  bytes(nonce)
        cipher = AES.new(self.salt,AES.MODE_EAX)
        return cipher.decrypt_and_verify(self.text,tag).decode()