import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

timestamp = 1736773716 #pcap timestamp

IV = timestamp.to_bytes(16, byteorder='big')

AES_KEY = b'\xff\x3d\xae\x3b\xcc\xef\x12\x44\xff\x3d\xae\x3b\xcc\xef\x12\x44'

ct_hex = "774b4d3953727234692f5866334f666f623937504c666b382b4375567158746c4b344a636b772b49786f5171754f32764a734d38594438537438754d362f5338362f4b6a5338594f6b6f73735665694b73444e7a515047676472497a546b627a453147696278675244537959426b5849464a32615359376b38732b524871524d"

ct_bytes = bytes.fromhex(ct_hex)
iv_bytes = bytes.fromhex(IV)

cipher = AES.new(AES_KEY, AES.MODE_CBC, iv_bytes)

decrypted_data = unpad(cipher.decrypt(ct_bytes), AES.block_size)

print("Decrypted Data:", decrypted_data)
