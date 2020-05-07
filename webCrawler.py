import sys
from webRequests import *
from page import Page
print("hello world!")
print(str(sys.argv))
try:
  webURL = str(sys.argv[1])
except IndexError:
  print("No URL provided, please provide a URL")
page = web_requests(str(sys.argv[1]))
page.print_all()
