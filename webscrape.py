import requests
from bs4 import BeautifulSoup

# define the URL of the blog
url = 'https://calnewport.com/blog/'

# send an HTTP GET request to the URL and get the content
response = requests.get(url)

print(response)