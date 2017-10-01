# Password Strength Calculator

This script check password strength and output overall score
1 - very weak password
10 - very strength password

Script do some checks:
1. password not exist in worst passwords list
2. check password length
3. password has a digit
4. password has a uppercase letter
5. password has a lowercase letter
6. password has a symbol

# How to use:

```bash

$ python password_strength.py <user_password> <weak_passwords_file.txt>

```

## Output example:

```bash
$ python password_strength.py /n,ici4lPF> 500-worst-passwords.txt
You password strength score : 10.0
```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
