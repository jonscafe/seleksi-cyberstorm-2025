# Challenge Name:
jawa token

## Description:
jawaaaaaaaaaaaaaaaaaaa

## Category:
Web (Black Box)

## File:
./dist.zip

## Flag:
`STORM{JWT_Basic_Dec0ding_00ffed88facc}`

## Points:
500

## Author:
k.eii

## Vulnerability Analysis
This challenge demonstrates a basic JWT (JSON Web Token) vulnerability. When a user visits the site, the backend generates a JWT token containing the flag as a claim and sets it as a cookie named `jwt_token`.

**How to Solve:**
1. **Access the Site:** Visit the challenge site and inspect your browser cookies. You will find a cookie named `jwt_token`.
2. **Extract the JWT:** Copy the value of the `jwt_token` cookie.
3. **Decode the JWT:** Use any online JWT decoder (e.g., [jwt.io](https://jwt.io/)) or a script to decode the token. The payload is only base64-encoded, so you can see the flag directly after decoding.
4. **Retrieve the Flag:** The decoded payload will contain the flag in the `flag` field.

**Why This Works:**
- The JWT is signed but not encrypted, and the flag is stored directly in the payload.
- Anyone with access to the token can decode it and read the flag, regardless of the signature.

**Mitigation:**
- Never store sensitive data (like flags or secrets) directly in JWT payloads.
- Use JWTs only for non-sensitive claims, or encrypt the payload if sensitive data must be included.

## PoC
1. Visit the site and get the `jwt_token` cookie.
2. Decode the JWT using [jwt.io](https://jwt.io/) or a script.
3. The flag is revealed in the payload.