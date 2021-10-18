#!/usr/bin/python3
import secrets
import string
from sys import exit
from sys import argv

"""
Simple Secure Password generator made in Python.
Pretty straight-forward, only detail is
the secrets module was used instead of random since
secrets was designed for cryptographic usage
whereas the random module was not.
"""

if len(argv) > 2:
	print("Usage: python3 pass-gen <length> (default 30, max 500)")
	exit(1)

if len(argv) == 2:
	if not argv[1].isdigit():
		print("Invalid length")
		exit(1)
	if int(argv[1]) > 500:
		print("Password too large")
		exit(1)

charset = string.ascii_letters + string.digits + string.punctuation + '          '

def generate(length=30):
	return ''.join(secrets.choice(charset) for i in range(length))

def main():
	if len(argv) == 2:
		print(generate(int(argv[1])))
	else:
		print(generate())
	
if __name__ == "__main__":
	main()
	exit(0)


