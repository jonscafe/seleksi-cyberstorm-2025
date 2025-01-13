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
