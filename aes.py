#coding=utf-8 
from Crypto.Cipher import AES
from binascii import b2a_hex,hexlify,unhexlify
from Crypto.Util import Counter


class FILE_bmp():
    def __init__(self,img_path='origin.bmp'):
      self.img_path=img_path
      self.img_encrypted_path='encrypted.bmp'
      self.__getheaddata__()

    def __getheaddata__(self):
      self.headdata=open(self.img_path,'rb').read(54)
      self.data=open(self.img_path,'rb').read()
      
    def encrypt(self,key='keyskeyskeyskeys',mode='ECB'):
       self.key=key
       file_out=open(self.img_encrypted_path,'wb')
       file_out.write(self.headdata)
       image_data=self.data
       plaintext=unhexlify(hexlify(image_data))
       length=16
       count=len(plaintext)
       add=length-(count%length)
       plaintext=plaintext+(b'\0'*add)
       self.IV=self.key
       if mode in ['ECB','CBC','CFB','OFB']:
         self.mode_str='AES.MODE_{0}'.format(mode)
         mode=eval(self.mode_str)
         encryptor=AES.new(key,mode,IV=self.IV) 
       elif mode in ['CTR']:
         self.mode_str='AES.MODE_{0}'.format(mode)
         mode=eval(self.mode_str)
         ctr=Counter.new(128)
         encryptor=AES.new(key,mode,IV=self.IV,counter=ctr)
       else:
         print("You do not provide a valid mode,exitting!")
         quit()
        
       self.mode=mode
       ciphertext=unhexlify(b2a_hex(encryptor.encrypt(plaintext)).decode("ASCII"))
       self.ciphertext=ciphertext
       file_out.write(ciphertext)
       file_out.close()
    def decrypt(self):
       file_out=open('decrypted.bmp','wb')
       file_out.write(self.headdata)
       if self.mode_str =='AES.MODE_CTR':
         ctr=Counter.new(128)
         decryptor=AES.new(self.key,self.mode,IV=self.IV,counter=ctr)
       else:
         decryptor=AES.new(self.key,self.mode,IV=self.IV)
       decrypted_data=unhexlify(b2a_hex(decryptor.decrypt(self.ciphertext)))
       file_out.write(decrypted_data)
       file_out.close()
