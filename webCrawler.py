import sys
from webRequests import *
from page import Page
from webSpider import Spider
try:
  webURL = str(sys.argv[1])
except IndexError:
  print("No URL provided, please provide a URL")

spoder = Spider()
spoder.crawl(str(sys.argv[1]))

search = input("Enter a search string: ")
print('')
spoder.searchForWord(search)
