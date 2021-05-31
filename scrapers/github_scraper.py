#!/usr/bin/env python3

from bs4 import BeautifulSoup as bs
import requests
import argparse
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# Input for repo name
parser = argparse.ArgumentParser(description="Search Github Repo")
parser.add_argument("-r", "--repo", type=str, default='leizafroilan')
args = parser.parse_args()

# GET request
url = 'https://github.com/' + args.repo
source = requests.get(url, verify=False)

# Test if URL is valid and exits if status code 404
if source.status_code == 404:
    print('Error code 404')
    exit(1)

# Creates BeautifulSoup object
soup = bs(source.text, 'lxml')

# Scrapes repo owner
try:
    name = soup.find('h1', class_ ='vcard-names').span.text.rstrip().lstrip()
except Exception as e:
    name = None
print(f'\nRepository Owner: {name}')

# Scrapes avatar
try:
    avatar = str(soup.find('img', alt="Avatar")).split('"')[7].split('"')[0]
except Exception as e:
    avatar = None

print(f'Avatar: {avatar}')

# Lists all repos
for repo in soup.find_all('div', class_ ='d-flex width-full flex-items-center position-relative'):
    try:
        href = 'https://github.com' + str(repo('a', href=True)).split('href')[1].split('"')[1]
    except Exception as e:
        href = None

    print(f'Repository: {href}')
print()
