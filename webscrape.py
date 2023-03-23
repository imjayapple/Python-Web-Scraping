import requests
from bs4 import BeautifulSoup

# define the URL of the blog
url = 'https://calnewport.com/blog/'

# send an HTTP GET request to the URL and get the content
response = requests.get(url)

# print(response)

# check if the request was successful (status code 200)
if response.status_code == 200:
    # parse the HTML content of the response
    soup = BeautifulSoup(response.text, 'html.parser')

    # find all the article elements on the page
    articles = soup.find_all('article')

    # iterate through the articles and extract the title and link
    for article in articles:
        title_element = article.find('h2')
        link_element = title_element.find('a')

        # get the text of the title and the URL of the link
        title = title_element.text
        link = link_element['href']

        # print the title and link
        print(f'Title: {title}')
        print(f'Link: {link}')
        print('-' * 80)
else:
    print(f"Failed to fetch the page. Status code: {response.status_code}")