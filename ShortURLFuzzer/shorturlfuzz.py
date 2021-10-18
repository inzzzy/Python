import requests
import string
import secrets
import time

"""
Curious fuzzing tool that discovers random shortened URLS.
Can be modified for other sites.
"""

charset = '0123456789' + string.ascii_lowercase + string.ascii_uppercase

def fuzzURL(url):
	r = requests.get(f'https://shorturl.at/{url}')
  # '2021 ShortUrl.at...' is in the HTTP Response if the shortened URL does not exist
	if '2021 ShortUrl.at - Tool to shorten a long link.' in r.text:
		return -1

def genURL() -> str:
	return ''.join(secrets.choice(charset) for i in range(5))

def main():
	while True:
		u = genURL()
		if fuzzURL(u) != -1:
			print(f"Found: https://shorturl.at/{u}")

      # Write found URL to log file
			with open('foundurls.txt', 'a') as f:
				f.write(f'https://shorturl.at/{u}\n')
				
		time.sleep(1)

if __name__ == '__main__':
	main()
