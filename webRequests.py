import requests
from page import Page
from bs4 import BeautifulSoup

def web_requests(webURL):
#try to request the page
  try:
    page = requests.get(webURL)
  except requests.ConnectionError as e:
    print(e)
    sys.exit(1)
  except requests.Timeout:
    print('request timed out\nExiting..')
    sys.exit(1)
#if successful, parse the page
  soup = BeautifulSoup(page.content, 'html.parser')
# get page attributes to create a new page object
  title = soup.find_all('title')[0].get_text()
  linksFull = soup.find_all('a')
  links = list()
  for link in linksFull:
      links.append(link.get('href'))
  paragraphListFull = soup.find_all('p')
  paragraphList = list()
  words = dict()
# fill words dictionary
  for p in paragraphListFull:
      paragraph = p.get_text()
      paragraphList.append(paragraph)
      wordsList = paragraph.split()
      for word in wordsList:
          if word in words:
              words[word] += 1
          else:
              words[word] = 1

# create page object
  p = Page(title, links, words, paragraphList)
  return p
