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

# webscraping practice

url = "https://books.toscrape.com/catalogue/category/books/programming_5/index.html"

# send an HTTP GET request to the URL and get the content
response = requests.get(url)

# check if the request was successful (status code 200)
if response.status_code == 200:
    # parse the HTML content of the response
    soup = BeautifulSoup(response.text, "html.parser")

    # find the book elements on the page
    books = soup.find_all("article", class_="product_pod")

    # limit to the top 10 books
    top_books = books[:10]

    # iterate through the top books and extract the title and author
    for book in top_books:
        title_element = book.find("h3").find("a")
        title = title_element["title"]

        # get the book detail page link
        detail_link = "https://books.toscrape.com/catalogue" + title_element["href"][8:]

        # fetch the book detail page
        detail_response = requests.get(detail_link)
        detail_soup = BeautifulSoup(detail_response.text, "html.parser")

        # get the author name from the detail page
        author_element = detail_soup.find("table", class_="table table-striped").find_all("tr")[1].find("td")
        author = author_element.text.strip()

        # print the title and author
        print(f"Title: {title}")
        print(f"Author: {author}")
        print("-" * 80)
else:
    print(f"Failed to fetch the page. Status code: {response.status_code}")