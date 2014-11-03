#! /usr/bin/python

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

	def getReference(self):
		return self._reference

	def addFiles(self, files):
		self._files = files

	def addCat(self, cat):
		self._cat = cat

	def addComments(self, comments):
		self._commments = comments

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

		SplittedEntry = ActualEntry.split(',\n')

		count = 0
		for field in SplittedEntry:
			field = field.strip(' \t\n')
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
				if fieldname == "gitbibfiles":
					self._files = fieldvalue
				if fieldname == "gitbibcat":
					self._cat = fieldvalue
				if fieldname == "gitbibcomments":
					self._comments = fieldvalue
			count = count + 1
		return 0

