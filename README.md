Secure Coding Review – CodeAlpha Internship

Project Description

This project demonstrates a security review of a Python authentication system. It compares vulnerable coding practices with improved secure coding techniques.

Project Files

- "vulnerable_code.py" – Demonstrates common security vulnerabilities.
- "secure_code.py" – Demonstrates improved security practices.
- "security_report.md" – Documents the identified vulnerabilities and their fixes.

Vulnerabilities Reviewed

1. Hardcoded secrets
2. Plain-text password handling
3. SQL injection
4. insecure debug configaration

Security Improvements

- PBKDF2 password hashing with random salts.
- Parameterized SQL queries.
- Secure password comparison.
- Duplicate username handling.

Technologies Used

- Python
- SQLite
- hashlib
- secrets
- hmac

How to Run

Open the project folder in VS Code and run:

python secure_code.py

Follow the prompts to register and test a login.

Disclaimer

This is an educational security review demonstration. It is not intended for production use.
