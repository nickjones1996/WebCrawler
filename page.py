class Page:
  def __init__(self, title, links, words, paragraphs):
      self.title = title
      self.links = links
      self.words = words
      self.paragraphs = paragraphs
  def get_links(self):
      return self.links
  def get_title(self):
      return self.title
  def get_words(self):
      return self.words
  def get_paragraphs(self):
      return self.paragraphs
  def print_title(self):
      print('Title:\n',self.title)
  def print_paragraphs(self):
      numP = 1
      for paragraph in self.paragraphs:
          print('Paragraph: ', numP)
          print(paragraph)
          numP += 1
  def print_links(self):
      print('Links:')
      for link in self.links:
          print(link)
  def print_all(self):
      self.print_title()
      self.print_paragraphs()
      self.print_links()
