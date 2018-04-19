#coding=utf-8
from aes import FILE_bmp


if __name__=='__main__':
          bmp=FILE_bmp()
          mode_str=raw_input("Please input AES encrypt mode:")
          bmp.encrypt(mode=mode_str)
          bmp.decrypt()
