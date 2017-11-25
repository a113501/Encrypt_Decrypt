# -*- coding:utf-8 -*-

import base64


class TripleDES():
    def __init__(self, password, key):
        self.password = password
        self.encrypted_password = ''
        self.key = key

    def bit64(self):
        return bytes(self.password.encode('utf-8'))
if __name__=='__main__':
    a = TripleDES('我是联邦','bismuth')
    print(a.bit64())