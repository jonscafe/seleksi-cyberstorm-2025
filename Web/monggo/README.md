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

## Vulnerability Analysis
This challenge contains a classic NoSQL injection vulnerability in the authentication logic. The backend uses user-supplied JSON directly in a MongoDB query without validation or sanitization. Specifically, the code in `src/middlewares/auth.js` does:

```js
const { username, password } = req.body;
const user = await User.findOne({ username, password }, { username: 1, _id: 0 });
```

This means any JSON object sent as `username` or `password` will be used directly in the query. MongoDB query operators like `$ne` (not equal) are accepted, allowing attackers to bypass authentication.

## Proof of Concept (PoC)
### NoSQL Injection Auth Bypass
Send this JSON POST request to `/login`:
```json
{"username":{"$ne": "x"},"password":{"$ne": "x"}}
```
This payload matches any user whose username and password are not `"x"`, which is almost all users. As a result, you are authenticated as the first user in the database, bypassing the need for valid credentials.

### User Lookup Injection
You can also retrieve users on `/lookup/{payload}` using a payload like:
```
' || 'a' == 'a
```

## Why This Works
- The backend does not validate or sanitize the input before passing it to MongoDB.
- MongoDB interprets objects like `{ "$ne": "x" }` as operators, not literal values.
- This allows attackers to inject query logic and bypass authentication or enumerate users.

## Mitigation
Always validate and sanitize user input before using it in database queries. Use strict schema validation and never trust raw user input in query objects.

---
