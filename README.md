# Pwned Password Checker

This script allows you to check if your password has been leaked in any data breaches by using the [Have I Been Pwned](https://haveibeenpwned.com/) API. It takes a password, hashes it using SHA-1, and checks the first five characters of the hash against the API to see if the password has been compromised.

## How It Works

1. **Hashing the Password:** The script hashes your password using the SHA-1 algorithm.
2. **Querying the API:** It then sends the first five characters of the SHA-1 hash to the Have I Been Pwned API.
3. **Checking for Leaks:** The API returns a list of hashes that match the provided prefix, along with the number of times each hash was found in data breaches. The script compares your hash with these results to determine if your password has been leaked.

## Usage

Clone the repository and run the script with your passwords as arguments:

```bash
git clone <your-repo-url>
cd <your-repo-directory>
python pwned_password_checker.py password1 password2 ...
```

Replace `password1 password2 ...` with the actual passwords you want to check.
