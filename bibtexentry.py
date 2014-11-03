#! /usr/bin/python

class BibTexEntry:
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

		self._reference = ''

		self.parse(entry.strip(' \n'))

	def getReference(self):
		return self._reference

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

		SplittedEntry = ActualEntry.split(',\n')

		count = 0
		for field in SplittedEntry:
			field = field.strip(' \n')
			if (count == 0):
				self._reference = field
			else:
				tokens = field.split('=')
				fieldname = tokens[0].strip(' ').lower()
				fieldvalue = tokens[1].strip(' ')
				fieldvalue = fieldvalue[1:len(fieldvalue) - 1]
				#FIXME: Handle concatenation form "One" # "Two" -> "OneTwo"...

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
			count = count + 1
		return 0
