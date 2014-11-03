#! /usr/bin/python

import sys
from config import Config

def config(argv):
	config = Config("gitbib.cf")
	config.fill()

def add(argv):
	print "TODO add"

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
