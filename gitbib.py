#! /usr/bin/python

import sys
import os.path
import shutil
from config import Config
from bibtexentry import BibTexEntry

CONFIG_FILE = "gitbib.cf"

def config(argv):
	config = Config(CONFIG_FILE)
	config.fill()

def getBibEntries(bibfile):
	inArob = False
	MetBrace = False
	NumBraces = 0
	Entry = ''
	Entries = []

	with open(bibfile) as f:
		while True:
			c = f.read(1)
			if not c:
				break

			if not inArob:
				if c == '@':
					inArob = True
					Entry = Entry + c
			else:
				Entry = Entry + c
				if c == '{':
					MetBrace = True
					NumBraces = NumBraces + 1
				elif c == '}':
					NumBraces = NumBraces - 1

				if MetBrace == True and NumBraces == 0:
					MetBrace = False
					inArob = False
					Entries.append(BibTexEntry(Entry))
					Entry = ''

	return Entries


def add(argv):
	config = Config(CONFIG_FILE)
	filename = config.getBibLocation()
	try:
		f = open(filename, 'a')
		print "Bibtex entry (enter a blank line at the end of the input):"
		sentinel = ''
		bibtex = ''
		for line in iter(raw_input, sentinel):
			bibtex = bibtex + line + '\n'

		bibtexentry = BibTexEntry(bibtex)
		Entries = getBibEntries(filename)
		for entry in Entries:
			if entry.getReference() == bibtexentry.getReference():
				print bibtexentry.getReference() + " already exists in " + filename + "."
				print "Please remove or update existing entry"
				sys.exit(1)

		print "Category (blank for uncategorized):"
		category = raw_input()
		if category == '':
			category = "Uncategorized"

		bibtexentry.addCat(category)

		print "Related files:"
		tmpfiles = raw_input()

		if len(tmpfiles) > 0:
			files = ''
			count = 1
			tokens = tmpfiles.split(',')
			for i in tokens:
				thisfile = i.replace(' ', '')
				if os.path.isfile(thisfile):
					if os.path.isdir(config.getFilesLocation()):
						fileTokenized = thisfile.split('.')
						tmpfile = bibtexentry.getReference() + str(count) + '.' + fileTokenized[len(fileTokenized) - 1]
						DstName = config.getFilesLocation() + tmpfile
						if len(files) > 0:
							files = files + ", "
						files = files + tmpfile
						shutil.copy(thisfile, DstName)
						count = count + 1
					else:
						print "Did not copy ", thisfile, "because ", config.getFilesLocation(), "does not exist."
				else:
					print "Could not find file ", thisfile
			bibtexentry.addFiles(files)
		f.write(str(bibtexentry) + '\n')
		f.close()

		print "Entry added."
	except IOError:
		print "Error when appending to ", filename

def search(argv):
	config = Config(CONFIG_FILE)
	filename = config.getBibLocation()
	Entries = getBibEntries(filename)
	RankedEntries = []

	if len(argv) < 2:
		print "Search needs at least one keyword..."
		sys.exit(1)

	for entry in Entries:
		score = entry.search(argv[2:])
		if score > 0:
			RankedEntries.append((score, entry))

	RankedEntries.sort(key=lambda tup: tup[0])

	count = len(RankedEntries)
	for entry in RankedEntries:
		print "========== " + str(count) + " =========="
		print entry[1]
		count = count - 1

def edit(argv):
	print "TODO edit"

def show(argv):
	print "TODO show"

def commit(argv):
	print "TODO commit"

def push(argv):
	print "TODO push"


def help():
	print "python gitbib.py [config|add|search|edit|show|commit|push|help]"
	print "- config: will create (or modify) configuration file gitbib.cf."
	print "- add: will add a bib entry to the base."
	print "- search: search a bibtex entry in the base given one keyword."
	print "- edit: edit an entry given its name."
	print "- show: show the file attached to an entry given its name."
	print "- commit: commit modifications made to the base."
	print "- push: push commits."
	print "- help: show this message."

def main(argv):
	#Parse first argument and call the right function
	if len(argv) > 1:
		if argv[1] == "config":
			config(argv)
		elif argv[1] == "add":
			add(argv)
		elif argv[1] == "search":
			search(argv)
		elif argv[1] == "edit":
			edit(argv)
		elif argv[1] == "show":
			show(argv)
		elif argv[1] == "commit":
			commit(argv)
		elif argv[1] == "push":
			push(argv)
		elif argv[1] == "help":
			help()
		else:
			help()
			sys.exit(1)
	else:
		help()
		sys.exit(1)
	sys.exit(0)

if __name__ == "__main__":
	main(sys.argv)
