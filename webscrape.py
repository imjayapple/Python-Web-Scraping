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

# title, paragraph, and link scraper

html_string = '''
<!DOCTYPE html>
<html>
<head>
    <title>My Web Page</title>
</head>
<body>
    <h1>Welcome to my web page</h1>
    <p>This is an example paragraph.</p>
    <ul>
        <li><a href="https://www.example1.com">Example 1</a></li>
        <li><a href="https://www.example2.com">Example 2</a></li>
    </ul>
</body>
</html>
'''

# parse the HTML string using Beautiful Soup
soup = BeautifulSoup(html_string, 'html.parser')

# extract the title of the webpage
title = soup.title.text
print(f'Title: {title}')

# extract the text of the first paragraph
paragraph = soup.p.text
print(f'Paragraph: {paragraph}')

# extract the links and their text 
links = soup.find_all('a')
for link in links:
    link_text = link.text
    link_url = link['href']
    print(f'Link text: {link_text}, Link URL: {link_url}')
