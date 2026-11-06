Secure Coding Review Report

1. Project Overview

This project demonstrates a manual security review of a Python-based authentication application. It compares insecure coding practices with improved secure coding techniques.

2. Vulnerabilities Identified

1. Hardcoded Secret

Finding: A secret key is directly stored in the source code.

Risk: Exposed source code may reveal sensitive configuration values.

Recommendation: Store secrets in environment variables or a secure secret manager.

2. Plain-Text Password Storage

Finding: The vulnerable application stores passwords directly in the database.

Risk: Anyone accessing the database can read user passwords.

Recommendation: Use password hashing with a unique salt, such as PBKDF2.

3. SQL Injection

Finding: User input is inserted into an SQL query using string formatting.

Risk: Malicious input can alter the intended database query.

Recommendation: Use parameterized SQL queries.

4. Insecure Debug Configuration

Finding: The vulnerable example contains a DEBUG flag set to True.

Risk: Enabling detailed debugging in a deployed application can expose sensitive information.

Recommendation: Disable debugging in production environments.

3. Security Improvements

The secure implementation includes:

- PBKDF2-HMAC-SHA256 password hashing.
- A unique random salt for each password.
- Parameterized SQL queries.
- Secure password hash comparison using hmac.compare_digest().
- Duplicate username handling.

4. Testing Performed

- Tested valid login credentials.
- Tested duplicate username registration.
- Tested incorrect password rejection.
- Verified successful login in the vulnerable demonstration.
- Verified successful registration and login in the secure implementation.

5. Conclusion

The manual code review identified common authentication security weaknesses. The improved implementation demonstrates safer password storage, database queries and password verification.

This project is an educational security review demonstration and is not intended for production deployment.

6. Technologies Used

- Python
- SQLite
- hashlib
- secrets
- hmac
