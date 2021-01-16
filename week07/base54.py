import os
import sys
import requests
import datetime
from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex
 
cryptor = AES.new(key, AES.MODE_CBC, key)  

with open(os.path.join(download_path, c_fule_name + ".mp4"), 'ab') as f:
    f.write(cryptor.decrypt(res.content))