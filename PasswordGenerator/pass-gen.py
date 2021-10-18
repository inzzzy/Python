#!/usr/bin/python3
import secrets
import string
from sys import exit
from sys import argv

if len(argv) > 2:
	print("Usage: python3 pass-gen <length> (default 30, max 500)")
	exit(1)

if len(argv) == 2:
	if not argv[1].isdigit():
		print("Invalid argument")
		exit(1)
	if int(argv[1]) > 500:
		print("Password too large")
		exit(1)

charset = string.ascii_letters + string.digits + string.punctuation + '          '

def generate(length=30):
	return ''.join(secrets.choice(charset) for i in range(length))

if len(argv) == 2:
	print(generate(int(argv[1])))
	exit(0)
 
print(generate())
exit(0)
