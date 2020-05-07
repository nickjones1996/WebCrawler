from webRequests import *
from page import Page

class Spider:
  pageList = dict()
  wordDict = dict()
  numPages = 1
  maxPages = 50
  def crawl(self, url):
      if url in self.pageList:
         return
      if self.maxPages < self.numPages:
         return
      print('crawling page: ', url)
      print('number of pages crawled: ', self.numPages)
      page = web_requests(url)
      self.pageList[url] = page
      pageWords = page.get_words()
      for word in pageWords:
          #tuple of (count, url, page)
          wordTuple = (pageWords[word], url, page)
          if word in self.wordDict:
              self.wordDict[word].append(wordTuple)
          else:
              self.wordDict[word] = [wordTuple]
      self.pageList[url] = page
      self.numPages += 1
      if self.numPages < self.maxPages:
         for link in page.get_links():
             self.crawl(link)
  def getKey(tuple):
      return tuple[0]
  def searchForWord(self, word):
      if  word in self.wordDict:
          tupleList = self.wordDict[word]
          tupleList.sort(reverse=True)
          for tuple in tupleList:
              print(tuple[0], ' occurrences of word:', word, 'on page titled:')
              print(tuple[2].get_title())
              print(tuple[1], '\n')
      else:
         print('word:', word, 'not found in any of the pages crawled')
