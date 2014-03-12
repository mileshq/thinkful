import os
import re
import argparse

SEARCH_FILE_EXT = '.txt'
DEFAULT_DIRECTORY = '.'

GB_META_SEARCHES = {
		#"title": re.compile(r'(title:\s*)(?P<title>.+\s.+)', re.IGNORECASE), \
		"title": re.compile(r'(?:title:\s*)(?P<title>((\S*( )?)+)' + \
			r'((\n(\ )+)(\S*(\ )?)*)*)', re.IGNORECASE), \
		"author": re.compile(r'(author:)(?P<author>.*)', re.IGNORECASE), \
		"translator": re.compile(r'(translator:)(?P<translator>.*)', re.IGNORECASE), \
		"illustrator": re.compile(r'(illustrator:)(?P<illustrator>.*)', re.IGNORECASE) \
		}

def list_by_file_ext(directory, extention=SEARCH_FILE_EXT):
	"""Return list of files from directory with matching extention."""
	return [os.path.join(directory, fn) for fn in os.listdir(directory) \
		if fn.endswith(extention)]

def read_file(filename):
	"""Open and return contents of file."""
	with open(filename, 'r') as fh:
		return fh.read()

def compile_regexs(keywords):
	"""Return dict of keyworks to compiled regex for that keyword."""
	return {kw: re.compile(r'\b' + kw + r'\b', re.IGNORECASE) for kw in keywords}

def count_keywords(text, regexs):
	"""Return dict of keywords and frequency in text."""
	return {word: len(re.findall(regexs[word], text)) for word in regexs}

def parse_for_metadata(text, regexs=GB_META_SEARCHES):
	#return {word: re.search(META_SEARCHES[word], text).group(word) \
	#	for word in META_SEARCHES if re.search(META_SEARCHES[word], text)}
	results = {}
	for md in regexs:
		match = re.search(regexs[md], text)
		if match:
			results[md] = match.group(md)
		#else:
		#	results[md] = ""
	return results

def pretty_print(results):
	pass

def main():
	parser = argparse.ArgumentParser( \
		description='Supply path to .txt files and parse for keywords')
	parser.add_argument("-d", "--dir", dest="directory", \
		default=DEFAULT_DIRECTORY, \
		help="directory containing .txt files to parse")
	
	# Removed: decided on position arguments, seems simpler
	#parser.add_argument("-w", "--words", required=True, \
	#	help="list of keywords to parse for", nargs="+")
	parser.add_argument("keywords", nargs="+", \
		help="list of keywords to parse for")
	
	args = parser.parse_args()
	#args = parser.parse_args('-d . -w this that then'.split())
	#args = parser.parse_args('-d . this that then'.split())
	#args = parser.parse_args('-d .'.split())

	print "-d {0}".format(args.directory)
	print "-w {0}".format(args.keywords)

	regexs = compile_regexs(args.keywords)

	for fn in list_by_file_ext(args.directory, SEARCH_FILE_EXT):
		text = read_file(fn)
		print fn, count_keywords(text, regexs)
		print fn, parse_for_metadata(text)

if __name__ == '__main__':
	main()