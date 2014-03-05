import sys
import os
import re

directory = None
keywords = []
searches = {}

title_search = re.compile(r'(title:\s*)(?P<title>.+\s.+)', re.IGNORECASE)
author_search = re.compile(r'(author:)(?P<author>.*)', re.IGNORECASE)
translator_search = re.compile(r'(translator:)(?P<translator>.*)', re.IGNORECASE)
illustrator_search = re.compile(r'(illustrator:)(?P<illustrator>.*)', re.IGNORECASE)

def search_keywords(directory, keywords):
	print "Directory: {0}".format(directory)
	print "Key words: {0}".format(keywords)

	for kw in keywords:
		searches[kw] = re.compile(r'\b' + kw + r'\b', re.IGNORECASE)

	for fl in os.listdir(directory):	
		if fl.endswith(".txt"):
			print "*" * 80
			print "Processing {0}".format(fl)
			fl_path = os.path.join(directory, fl)

			with open(fl_path, 'r') as fh:
				doc = fh.read()
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
  				print "Title: {}".format(title)
  				print "Author(s): {}".format(author)
  				print "Translator(s): {}".format(translator)
  				print "Illustrator(s): {}".format(illustrator)

  				for search in searches:
  					print "Keyword: \'{0}\' {1}".format(search, len(re.findall(searches[search], doc)))

if len(sys.argv) == 1:
	print "No args supplied, ending."
elif len(sys.argv) == 2:
	print "Only one arg supplied, assuming it is a keyword, searching local dir"
	directory = "."
	keywords = sys.argv[1]
	search_keywords(directory, keywords)
else:
	directory = sys.argv[1]
	keywords = sys.argv[2:]
	search_keywords(directory, keywords)