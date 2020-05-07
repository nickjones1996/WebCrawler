import requests
from page import Page
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from urllib.parse import urljoin

def internal_website(base, link):
    parsedBase = urlparse(base)
    parsedLink = urlparse(link)
    return parsedBase.netloc == parsedLink.netloc
def relative_to_absolute(base, relative):
    ret = urljoin(base, relative)
    return ret
def scrub_string(dirty):
    temp = dirty
    badChars = [':', '?', '.', '!', ':', '#', ',', '\"', '\'', '(', ')']
    for i in badChars :
        temp = temp.replace(i, '')
    return temp

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
      linkSrc = link.get('href')
      if internal_website(webURL, linkSrc):
         absoluteURL = relative_to_absolute(webURL, linkSrc)
         links.append(absoluteURL)
  paragraphListFull = soup.find_all('p')
  paragraphList = list()
  words = dict()
  titleSplit = title.split()
  for titleWord in titleSplit:
      scrubbed = scrub_string(titleWord)
      if scrubbed in words:
          words[scrubbed] += 1
      else:
          words[scrubbed] = 1
# fill words dictionary
  for p in paragraphListFull:
      paragraph = p.get_text()
      paragraphList.append(paragraph)
      wordsList = paragraph.split()
      for word in wordsList:
          scrubbed = scrub_string(word)
          if scrubbed in words:
              words[scrubbed] += 1
          else:
              words[scrubbed] = 1

# create page object
  p = Page(title, links, words, paragraphList)
  return p
