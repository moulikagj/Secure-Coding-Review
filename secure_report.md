# Secure Coding Review Report

## 1. Project Overview
This project demonstrates a security review of a Python-based
authentication system. It identifies common coding vulnerabilities
and provides secure alternatives.

## 2. Security Issues Identified

### 1. Hardcoded Secret
- Vulnerable code stores a secret directly in the source code.
- Attackers may discover exposed secrets.
- Fix: Store secrets securely using environment variables.

### 2. Plain-Text Passwords
- Passwords should never be stored as plain text.
- Fix: Use PBKDF2 password hashing with a unique random salt.

### 3. SQL Injection
- Building SQL queries using string formatting is unsafe.
- Malicious input may change the SQL query.
- Fix: Use parameterized SQL queries.

### 4. Debug Mode
- Debug mode can expose sensitive application information.
- Fix: Disable debug mode in production.

## 3. Security Improvements
- Password hashing using PBKDF2.
- Unique random salt for passwords.
- Parameterized SQL queries.
- Secure password comparison.
- Duplicate username handling.

## 4. Conclusion
The review identified important security weaknesses in the
vulnerable code and demonstrated safer coding practices.
The secure version reduces the risks of password exposure
and SQL injection.

## 5. Tools and Technologies
- Python
- SQLite
- hashlib
- secrets
- hmac

## 6. Vulnerability Analysis and Remediation

| Vulnerability | Risk | Recommended Fix |
|---|---|---|
| Hardcoded secret | Secret exposure | Use environment variables |
| Plain-text passwords | Password theft | Use secure password hashing |
| SQL injection | Unauthorized database access | Use parameterized queries |
| Debug mode | Information exposure | Disable debug mode in production |

## 7. Code Comparison

The vulnerable version uses unsafe SQL string formatting
and stores passwords in plain text.

The secure version uses parameterized SQL queries,
PBKDF2 password hashing with unique salts, and secure
password comparison.

## 8. Testing

- Tested valid login credentials.
- Tested duplicate username registration.
- Tested incorrect password rejection.
- Verified successful login using the secure version.
- Verified successful login using the vulnerable demonstration.

## 9. Final Result

The project demonstrates how manual code inspection
can identify security weaknesses and how secure coding
practices can reduce those risks.