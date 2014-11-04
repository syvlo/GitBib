#! /usr/bin/python

import os.path
import shutil
#FIXME: Should handle in some way the string entry...

class BibTexEntry:
	SCORE_REF = 5
	SCORE_AUTHOR = 10
	SCORE_TITLE = 10

	def __init__(self, entry):
		self._address = ''
		self._abstract = ''
		self._annote = ''
		self._author = ''
		self._booktitle = ''
		self._chapter = ''
		self._crossref = ''
		self._edition = ''
		self._editor = ''
		self._eprint = ''
		self._howpublished = ''
		self._institution = ''
		self._journal = ''
		self._key = ''
		self._month = ''
		self._note = ''
		self._number = ''
		self._organization = ''
		self._pages = ''
		self._publisher = ''
		self._school = ''
		self._series = ''
		self._title = ''
		self._type = ''
		self._url = ''
		self._volume = ''
		self._year = ''
		#Defined by gitbib.
		self._files = ''
		self._cat = ''
		self._comments = ''
		self._reference = ''

		self.parse(entry.strip(' \n'))

	#Getters / Setters

	def getReference(self):
		return self._reference

	def setReference(self, value):
		self._reference = value

	def getAddress(self):
		return self._address

	def setAddress(self, value):
		self._address = value

	def getAbstract(self):
		return self._abstract

	def setAbstract(self, value):
		self._abstract = value

	def getAnnote(self):
		return self._annote

	def setAnnote(self, value):
		self._annote = value

	def getAuthor(self):
		return self._author

	def setAuthor(self, value):
		self._author = value

	def getBooktitle(self):
		return self._booktitle

	def setBooktitle(self, value):
		self._booktitle = value

	def getChapter(self):
		return self._chapter

	def setChapter(self, value):
		self._chapter = value

	def getCrossref(self):
		return self._crossref

	def setCrossref(self, value):
		self._crossref = value

	def getEdition(self):
		return self._edition

	def setEdition(self, value):
		self._edition = value

	def getEditor(self):
		return self._editor

	def setEditor(self, value):
		self._editor = value

	def getEprint(self):
		return self._eprint

	def setEprint(self, value):
		self._eprint = value

	def getHowpublished(self):
		return self._howpublished

	def setHowpublished(self, value):
		self._howpublished = value

	def getInstitution(self):
		return self._institution

	def setInstitution(self, value):
		self._institution = value

	def getJournal(self):
		return self._journal

	def setJournal(self, value):
		self._journal = value

	def getKey(self):
		return self._key

	def setKey(self, value):
		self._key = value

	def getMonth(self):
		return self._month

	def setMonth(self, value):
		self._month = value

	def getNote(self):
		return self._note

	def setNote(self, value):
		self._note = value

	def getNumber(self):
		return self._number

	def setNumber(self, value):
		self._number = value

	def getOrganization(self):
		return self._organization

	def setOrganization(self, value):
		self._organization = value

	def getPages(self):
		return self._pages

	def setPages(self, value):
		self._pages = value

	def getPublisher(self):
		return self._publisher

	def setPublisher(self, value):
		self._publisher = value

	def getSchool(self):
		return self._school

	def setSchool(self, value):
		self._school = value

	def getSeries(self):
		return self._series

	def setSeries(self, value):
		self._series = value

	def getTitle(self):
		return self._title

	def setTitle(self, value):
		self._title = value

	def getType(self):
		return self._type

	def setType(self, value):
		self._type = value

	def getUrl(self):
		return self._url

	def setUrl(self, value):
		self._url = value

	def getVolume(self):
		return self._volume

	def setVolume(self, value):
		self._volume = value

	def getYear(self):
		return self._year

	def setYear(self, value):
		self._year = value

	def getFiles(self):
		return self._files

	def setFiles(self, value, FilesLocation):
		if len(value) > 0:
			files = ''
			count = 1
			tokens = value.split(',')
			for i in tokens:
				thisfile = os.path.expanduser(i.replace(' ', ''))
				if os.path.isfile(thisfile):
					if os.path.isdir(FilesLocation):
						fileTokenized = thisfile.split('.')
						tmpfile = self.getReference() + str(count) + '.' + fileTokenized[len(fileTokenized) - 1]
						DstName = FilesLocation + tmpfile
						if len(files) > 0:
							files = files + ", "
						files = files + tmpfile
						shutil.copy(thisfile, DstName)
						count = count + 1
					else:
						print "Did not copy ", thisfile, "because ", FilesLocation(), "does not exist."
				else:
					print "Could not find file ", thisfile
		self._files = files


	def getCat(self):
		return self._cat

	def setCat(self, value):
		if len(value) == 0:
			value = "Uncategorized"
		self._cat = value

	def getComments(self):
		return self._comments

	def setComments(self, value):
		self._comments = value

	def getReference(self):
		return self._reference

	def setReference(self, value):
		self._reference = value


	def search(self, keywords):
		score = 0
		for keyword in keywords:
			keyword = keyword.lower()
			if self._reference.lower().find(keyword) >= 0:
				score = score + self.SCORE_REF
			if self._author.lower().find(keyword) >= 0:
				score = score + self.SCORE_AUTHOR
			if self._title.lower().find(keyword) >= 0:
				score = score + self.SCORE_TITLE

		return score

	def __str__(self):
		return self.__repr__()

	def __repr__(self):
		Result = '@'
		Result = Result + self._type + '{' + self._reference
		if len(self._title) > 0:
			Result = Result + ',\n\ttitle={' + self._title + '}'
		if len(self._author) > 0:
			Result = Result + ',\n\tauthor={' + self._author + '}'
		if len(self._address) > 0:
			Result = Result + ',\n\taddress={' + self._address + '}'
		if len(self._abstract) > 0:
			Result = Result + ',\n\tabstract={' + self._abstract + '}'
		if len(self._annote) > 0:
			Result = Result + ',\n\tannote={' + self._annote + '}'
		if len(self._booktitle) > 0:
			Result = Result + ',\n\tbooktitle={' + self._booktitle + '}'
		if len(self._chapter) > 0:
			Result = Result + ',\n\tchapter={' + self._chapter + '}'
		if len(self._crossref) > 0:
			Result = Result + ',\n\tcrossref={' + self._crossref + '}'
		if len(self._edition) > 0:
			Result = Result + ',\n\tedition={' + self._edition + '}'
		if len(self._editor) > 0:
			Result = Result + ',\n\teditor={' + self._editor + '}'
		if len(self._eprint) > 0:
			Result = Result + ',\n\teprint={' + self._eprint + '}'
		if len(self._howpublished) > 0:
			Result = Result + ',\n\thowpublished={' + self._howpublished + '}'
		if len(self._institution) > 0:
			Result = Result + ',\n\tinstitution={' + self._institution + '}'
		if len(self._journal) > 0:
			Result = Result + ',\n\tjournal={' + self._journal + '}'
		if len(self._key) > 0:
			Result = Result + ',\n\tkey={' + self._key + '}'
		if len(self._month) > 0:
			Result = Result + ',\n\tmonth={' + self._month + '}'
		if len(self._note) > 0:
			Result = Result + ',\n\tnote={' + self._note + '}'
		if len(self._number) > 0:
			Result = Result + ',\n\tnumber={' + self._number + '}'
		if len(self._organization) > 0:
			Result = Result + ',\n\torganization={' + self._organization + '}'
		if len(self._pages) > 0:
			Result = Result + ',\n\tpages={' + self._pages + '}'
		if len(self._publisher) > 0:
			Result = Result + ',\n\tpublisher={' + self._publisher + '}'
		if len(self._school) > 0:
			Result = Result + ',\n\tschool={' + self._school + '}'
		if len(self._series) > 0:
			Result = Result + ',\n\tseries={' + self._series + '}'
		if len(self._type) > 0:
			Result = Result + ',\n\ttype={' + self._type + '}'
		if len(self._url) > 0:
			Result = Result + ',\n\turl={' + self._url + '}'
		if len(self._volume) > 0:
			Result = Result + ',\n\tvolume={' + self._volume + '}'
		if len(self._year) > 0:
			Result = Result + ',\n\tyear={' + self._year + '}'
		if len(self._files) > 0:
			Result = Result + ',\n\tgitbibFiles={' + self._files + '}'
		if len(self._cat) > 0:
			Result = Result + ',\n\tgitbibCat={' + self._cat + '}'
		if len(self._comments) > 0:
			Result = Result + ',\n\tgitbibComments={' + self._comments + '}'
		Result = Result + '\n}'
		return Result



	def parse(self, entry):
		#entry should start with a @:
		if entry[0] != "@":
			print entry, "is not an entry!"
			return 1
		OpeningBracePos = entry.find('{')
		self._type = entry[1:OpeningBracePos].lower()
		#Last char should be a closing brace
		if entry[len(entry) - 1] != "}":
			print "Did not find expected closing brace."
			return 1

		#Entry without outter braces.
		ActualEntry = entry[OpeningBracePos + 1:len(entry) - 1]

		SplittedEntry = []
		CurrentWord = ''
		NumberBraces = 0
		InQuotes = False
		for i in ActualEntry:
			if NumberBraces == 0 and not InQuotes and i == ',':
				SplittedEntry.append(CurrentWord)
				CurrentWord = ''
			if i == '{':
				NumberBraces = NumberBraces + 1
			if i == '}':
				NumberBraces = NumberBraces - 1
			if i == '"':
				InQuotes = not InQuotes
			CurrentWord = CurrentWord + i
		if NumberBraces == 0 and not InQuotes:
			SplittedEntry.append(CurrentWord)

		count = 0
		for field in SplittedEntry:
			field = field.strip(' \t\n,')
			if (count == 0):
				self._reference = field
			else:
				tokens = field.split('=')
				fieldname = tokens[0].strip(' ').lower()
				fieldvalue = tokens[1].strip(' ')
				fieldvalue = fieldvalue[1:len(fieldvalue) - 1]
				#FIXME: Handle concatenation form "One" # "Two" -> "OneTwo"...
				#FIXME: Use dict instead...
				if fieldname == "address":
					self._address = fieldvalue
				if fieldname == "abstract":
					self._abstract = fieldvalue
				if fieldname == "annote":
					self._annote = fieldvalue
				if fieldname == "author":
					self._author = fieldvalue
				if fieldname == "booktitle":
					self._booktitle = fieldvalue
				if fieldname == "chapter":
					self._chapter = fieldvalue
				if fieldname == "crossref":
					self._crossref = fieldvalue
				if fieldname == "edition":
					self._edition = fieldvalue
				if fieldname == "editor":
					self._editor = fieldvalue
				if fieldname == "eprint":
					self._eprint = fieldvalue
				if fieldname == "howpublished":
					self._howpublished = fieldvalue
				if fieldname == "institution":
					self._institution = fieldvalue
				if fieldname == "journal":
					self._journal = fieldvalue
				if fieldname == "key":
					self._key = fieldvalue
				if fieldname == "month":
					self._month = fieldvalue
				if fieldname == "note":
					self._note = fieldvalue
				if fieldname == "number":
					self._number = fieldvalue
				if fieldname == "organization":
					self._organization = fieldvalue
				if fieldname == "pages":
					self._pages = fieldvalue
				if fieldname == "publisher":
					self._publisher = fieldvalue
				if fieldname == "school":
					self._school = fieldvalue
				if fieldname == "series":
					self._series = fieldvalue
				if fieldname == "title":
					self._title = fieldvalue
				if fieldname == "url":
					self._url = fieldvalue
				if fieldname == "volume":
					self._volume = fieldvalue
				if fieldname == "year":
					self._year = fieldvalue
				if fieldname == "gitbibfiles":
					self._files = fieldvalue
				if fieldname == "gitbibcat":
					self._cat = fieldvalue
				if fieldname == "gitbibcomments":
					self._comments = fieldvalue
			count = count + 1
		return 0

