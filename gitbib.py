#! /usr/bin/python

import sys
import shutil
import os.path
import inspect
import subprocess
from config import Config
from bibtexentry import BibTexEntry

CONFIG_FILE = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))) + "/default.cf"

def config(argv):
	config = Config(CONFIG_FILE)
	config.fill()

def getCategories(Entries):
	Categories = []

	for entry in Entries:
		CatsFromEntry = entry.getCat().split(',')
		for cat in CatsFromEntry:
			cat = cat.strip()
			if not cat in Categories:
				Categories.append(cat)

	return Categories

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
		print "Category (select or enter a new one):"
		Categories = getCategories(Entries)
		if len(Categories) > 0:
			i = 0
			for cat in Categories:
				print str(i) + ": " + cat
				i = i + 1

		category = raw_input()
		if category.isdigit():
			category = Categories[int(category)]
		if category == '':
			category = "Uncategorized"

		bibtexentry.setCat(category)

		print "Related files:"
		files = raw_input()
		bibtexentry.setFiles(files, config.getFilesLocation())
		f.write(str(bibtexentry) + '\n')
		f.close()

		print "Entry added."
	except IOError:
		print "Error when appending to ", filename

def search(argv):
	if len(argv) < 2:
		print "Search needs at least one keyword..."
		sys.exit(1)

	config = Config(CONFIG_FILE)
	filename = config.getBibLocation()
	Entries = getBibEntries(filename)
	RankedEntries = []

	for entry in Entries:
		score = entry.search(argv[2:])
		if score > 0:
			RankedEntries.append((score, entry))

	RankedEntries.sort(key=lambda tup: tup[0])

	count = len(RankedEntries)
	if count == 0:
		print "No entry found matching search"
	for entry in RankedEntries:
		print "========== " + str(count) + " =========="
		print entry[1]
		count = count - 1

def editEntry(entry, Entries):
	config = Config(CONFIG_FILE)
	Fields = {
		'Address': (BibTexEntry.setAddress, BibTexEntry.getAddress),
		'Abstract': (BibTexEntry.setAbstract, BibTexEntry.getAbstract),
		'Annote': (BibTexEntry.setAnnote, BibTexEntry.getAnnote),
		'Author': (BibTexEntry.setAuthor, BibTexEntry.getAuthor),
		'Booktitle': (BibTexEntry.setBooktitle, BibTexEntry.getBooktitle),
		'Chapter': (BibTexEntry.setChapter, BibTexEntry.getChapter),
		'Crossref': (BibTexEntry.setCrossref, BibTexEntry.getCrossref),
		'Edition': (BibTexEntry.setEdition, BibTexEntry.getEdition),
		'Editor': (BibTexEntry.setEditor, BibTexEntry.getEditor),
		'Eprint': (BibTexEntry.setEprint, BibTexEntry.getEprint),
		'Howpublished': (BibTexEntry.setHowpublished, BibTexEntry.getHowpublished),
		'Institution': (BibTexEntry.setInstitution, BibTexEntry.getInstitution),
		'Journal': (BibTexEntry.setJournal, BibTexEntry.getJournal),
		'Key': (BibTexEntry.setKey, BibTexEntry.getKey),
		'Month': (BibTexEntry.setMonth, BibTexEntry.getMonth),
		'Note': (BibTexEntry.setNote, BibTexEntry.getNote),
		'Number': (BibTexEntry.setNumber, BibTexEntry.getNumber),
		'Organization': (BibTexEntry.setOrganization, BibTexEntry.getOrganization),
		'Pages': (BibTexEntry.setPages, BibTexEntry.getPages),
		'Publisher': (BibTexEntry.setPublisher, BibTexEntry.getPublisher),
		'School': (BibTexEntry.setSchool, BibTexEntry.getSchool),
		'Series': (BibTexEntry.setSeries, BibTexEntry.getSeries),
		'Title': (BibTexEntry.setTitle, BibTexEntry.getTitle),
		'Type': (BibTexEntry.setType, BibTexEntry.getType),
		'Url': (BibTexEntry.setUrl, BibTexEntry.getUrl),
		'Volume': (BibTexEntry.setVolume, BibTexEntry.getVolume),
		'Year': (BibTexEntry.setYear, BibTexEntry.getYear),
		'Files': (BibTexEntry.setFiles, BibTexEntry.getFiles),
		'Cat': (BibTexEntry.setCat, BibTexEntry.getCat),
		'Comments': (BibTexEntry.setComments, BibTexEntry.getComments),
		'Reference': (BibTexEntry.setReference, BibTexEntry.getReference)
	}
	print "====================="
	print "Editing " + entry.getReference()
	print "Select field to edit:"

	for key in Fields:
		print key

	key = raw_input('Choice:')

	if key == "Cat":
		Categories = getCategories(Entries)
		if len(Categories) > 0:
			i = 0
			for cat in Categories:
				print str(i) + ": " + cat
				i = i + 1

		print "Category (select or enter a new one):"
		category = raw_input()
		if category.isdigit():
			category = Categories[int(category)]
		if category == '':
			category = "Uncategorized"

		entry.setCat(category)

	else:
		print "New value for " + key,
		if len(Fields[key][1](entry)) > 0:
			print " (was " + Fields[key][1](entry) + "):"
		else:
			print ":"

		value = raw_input('')
		if key == "Files":
			Fields["Files"][0](entry, value, config.getFilesLocation())
		else:
			Fields[key][0](entry, value)

	print "Done. Edit another value for the same entry ? [y/N]"
	again = raw_input('')
	if (again.lower() == 'y'):
		editEntry(entry, Entries)
	print "====================="

def edit(argv):
	if len(argv) == 0:
		print "You need to provide at least one reference name to edit"
		sys.exit(1)

	config = Config(CONFIG_FILE)
	filename = config.getBibLocation()
	Entries = getBibEntries(filename)

	IndexToModify = []
	ReferencesToFind = argv

	#Check that references are in the base
	countEntry = 0
	for entry in Entries:
		for ref in ReferencesToFind:
			if entry.getReference() == ref:
				IndexToModify.append(countEntry)
				ReferencesToFind.remove(ref)
		countEntry = countEntry + 1

	if len(ReferencesToFind) > 0:
		print "Some references were not found:"
		print ReferencesToFind
		sys.exit(1)

	with open(".gitbibtmp.bib", 'w') as f:
		for iEntry in range(len(Entries)):
			for iIndexToModify in IndexToModify:
				if iEntry == iIndexToModify:
					editEntry(Entries[iEntry], Entries)
			f.write(str(Entries[iEntry]) + '\n')

	shutil.copy(".gitbibtmp.bib", filename)

def delete(argv):
	if len(argv) == 0:
		print "You need to provide at least one reference name to delete"
		sys.exit(1)

	config = Config(CONFIG_FILE)
	filename = config.getBibLocation()
	Entries = getBibEntries(filename)

	IndexToModify = []
	ReferencesToFind = argv

	#Check that references are in the base
	countEntry = 0
	for entry in Entries:
		for ref in ReferencesToFind:
			if entry.getReference() == ref:
				IndexToModify.append(countEntry)
				ReferencesToFind.remove(ref)
		countEntry = countEntry + 1

	if len(ReferencesToFind) > 0:
		print "Some references were not found:"
		print ReferencesToFind
		sys.exit(1)

	with open(".gitbibtmp.bib", 'w') as f:
		for iEntry in range(len(Entries)):
			for iIndexToModify in IndexToModify:
				if iEntry == iIndexToModify:
					Entries[iEntry].removeFiles(config.getFilesLocation())
				else:
					f.write(str(Entries[iEntry]) + '\n')

	shutil.copy(".gitbibtmp.bib", filename)


def show(argv):
	if len(argv) == 0:
		print "You need to provide at least one reference name to show"
		sys.exit(1)

	config = Config(CONFIG_FILE)
	filename = config.getBibLocation()
	filespath = config.getFilesLocation()
	pdfViewer = config.getPDFViewer()
	Entries = getBibEntries(filename)

	for i in argv:
		Found = False
		for entry in Entries:
			if i == entry.getReference():
				Found = True
				Files = entry.getFiles().split(',')
				for File in Files:
					File = File.strip(' ')
					Ext = os.path.splitext(File)[1]
					if Ext.lower() == ".pdf":
						subprocess.Popen([pdfViewer, filespath+File])
					else:
						print "Cannot read " + File

		if Found == False:
			print "Could not find an entry named " + i

def commit(argv):
	print "TODO commit"

def push(argv):
	print "TODO push"


def help():
	print "python gitbib.py [config|add|search|edit|delete|show|commit|push|help]"
	print "- config: will create (or modify) configuration file gitbib.cf."
	print "- add: will add a bib entry to the base."
	print "- search: search a bibtex entry in the base given one keyword."
	print "- edit: edit an entry given its name."
	print "- delete: delete an entry given its name."
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
			edit(argv[2:])
		elif argv[1] == "delete":
			delete(argv[2:])
		elif argv[1] == "show":
			show(argv[2:])
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
