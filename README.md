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

$ python password_strength.py -h
usage: password_strength.py [-h] -p PASSWORD -f FILE

optional arguments:
  -h, --help            show this help message and exit
  -p PASSWORD, --password PASSWORD
                        User password for analyse (optional)
  -f FILE, --file FILE  File with worst passwords

```

## Output example:

**recommended**

```bash
$ python password_strength.py -f 500-worst-passwords.txt
Enter password for analyse:
You password strength score : 10.0
```
**or (not recommended)**

```bash
$ python password_strength.py -p /n,ici4lPF> -f 500-worst-passwords.txt
You password strength score : 10.0
```


# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
