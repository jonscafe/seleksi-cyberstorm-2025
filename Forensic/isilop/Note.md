# isilop
enak ya jadi kalian, kalau kena hack lapor ke tim incident response. kami kalau kena hack lapor ke siapa?

`flag terbagi atas 3 part`

#### 3 part flag
- part1: `STORM{gampang_l4h_`
- part2: `chall_simple_`
- part3 : `ini_88e453eeac}`

#### distribution file:
- ad1
- pcap

#### scenario:
- python executable downloaded from internet (part 1 flag is here), the exe will download a python malware (entry.py)
- the python malware will ransom all file of the PC (in %userprofile% folder), encrypt it with AES as Base64 and send to attacker's host (part 2 flag is here in the python malware) (obfuscated.py)
- part 3 flag is in the encrypted victim's data


### Compile:
pyinstaller --onefile --collect-all Crypto --hidden-import=requests obfuscated.py

# 1. read %userprofile% Documents, Desktop, Downloads, Pictures, Videos, Music
# 2. encrypt the files with AES, key is ff3dae3bccef1244 iv is taken rand with seed taken from timestamp of now, the cttext is encoded as base64
# 3. the resulted base 64 is sent as hex stream by splitting it into 128 byte chunk through network using post to http://0x00.webhook.site/?data={hexstream}
