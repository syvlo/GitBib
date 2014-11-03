#! /usr/bin/python

import sys
import os.path
import shutil
from config import Config

CONFIG_FILE = "gitbib.cf"

def config(argv):
	config = Config(CONFIG_FILE)
	config.fill()

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

		#TODO: Check for duplicated entry.

		print "Category (blank for uncategorized):"
		category = raw_input()
		if category == '':
			category = "Uncategorized"

		print "Related files:"
		tmpfiles = raw_input()

		f.write("Category = " + category + '\n')
		if len(tmpfiles) > 0:
			files = ''
			count = 1
			tokens = tmpfiles.split(',')
			for i in tokens:
				thisfile = i.replace(' ', '')
				if os.path.isfile(thisfile):
					if os.path.isdir(config.getFilesLocation()):
						#FIXME: Should change filename in the form entryname + count to avoid duplicates.
						tmpfile = "FIXME" + str(count)
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
			f.write("Files = " + files + '\n')
		f.write(bibtex + '\n')
		f.close()

		print "Entry added."
	except IOError:
		print "Error when appending to ", filename

def search(argv):
	print "TODO search"

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
