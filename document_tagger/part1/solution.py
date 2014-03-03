import re, sys
from pg_sample_texts import DIV_COMM, MAG_CART

# documents to search
documents = [DIV_COMM, MAG_CART]

# metadata matching compiles
title_search = re.compile(r'(title:\s*)(?P<title>.+\s.+)', re.IGNORECASE)
author_search = re.compile(r'(author:)(?P<author>.*)', re.IGNORECASE)
translator_search = re.compile(r'(translator:)(?P<translator>.*)', re.IGNORECASE)
illustrator_search = re.compile(r'(illustrator:)(?P<illustrator>.*)', re.IGNORECASE)

# keyword matching compiles
searches = {}
for kw in sys.argv[1:]:
  searches[kw] = re.compile(r'\b' + kw + r'\b', re.IGNORECASE)

# perform searches, print output
for i, doc in enumerate(documents):
  title = re.search(title_search, doc).group('title')
  author = re.search(author_search, doc)
  translator = re.search(translator_search, doc)
  illustrator = re.search(illustrator_search, doc)
  if author: 
    author = author.group('author')
  if translator:
    translator = translator.group('translator')
  if illustrator:
    illustrator = illustrator.group('illustrator')
  print "*" * 80
  print "Title: {}".format(title)
  print "Author(s): {}".format(author)
  print "Translator(s): {}".format(translator)
  print "Illustrator(s): {}".format(illustrator)
  #print "\n"
  for search in searches:
    print "\"{0}\": {1}".format(search, len(re.findall(searches[search], doc)))
