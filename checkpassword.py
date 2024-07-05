import requests
import hashlib
import sys

def requestApiData(queryChar):
  url = 'https://api.pwnedpasswords.com/range/' + queryChar
  res = requests.get(url)
  if res.status_code != 200:
    raise RuntimeError(f'Error fetching: {res.status_code}, check the api and try again')
  return res

def numTimesPasswordLeak(hashes, hashToCheck):
  hashes = (line.split(':') for line in hashes.text.splitlines())
  for h, count in hashes:
    if h == hashToCheck:
      return count
  return 0

def pwnedCheckApi(password):
  sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
  first5_char, tail = sha1password[:5], sha1password[5:]
  response = requestApiData(first5_char)
  return numTimesPasswordLeak(response, tail)

def main(args):
  for password in args:
    count = pwnedCheckApi(password)
    if count:
      print(f'{password} was found {count} times... you should probably change your password!')
    else:
      print(f'{password} was NOT found. Carry on!')
  return 'done!'

if __name__ == '__main__':
  sys.exit(main(sys.argv[1:]))

