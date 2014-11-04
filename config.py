#! /usr/bin/python

class Config:
	def __init__(self, filename):
		self._filename = filename
		self._BibLocation = ""
		self._FilesLocation = ""
		self._pdfViewer = ''
		try:
			f = open(self._filename, 'r')
			for line in f:
				tokens = line.split(' ')

				if tokens[0] == "BibLocation":
					self._BibLocation = tokens[2].replace('\n', '').replace('"', '')
				elif tokens[0] == "FilesLocation":
					self._FilesLocation = tokens[2].replace('\n', '').replace('"', '')
				elif tokens[0] == "PDFViewer":
					self._pdfViewer = tokens[2].replace('\n', '').replace('"', '')
			f.close()
		except IOError:
			print "Non existing file"

	def fill(self):
		try:
			f = open(self._filename, 'w')

			print "Location of bib file: ",
			if len(self._BibLocation) > 0:
				print "(was", self._BibLocation, ")",
			self._BibLocation = raw_input('')
			f.write("BibLocation = " +  self._BibLocation + "\n")

			print "Location of files (pdfs, ...): ",
			if len(self._FilesLocation) > 0:
				print "(was", self._FilesLocation, ")",
			self._FilesLocation = raw_input('')
			f.write("FilesLocation = " + self._FilesLocation + "\n")

			print "PDF Viewer: ",
			if len(self._pdfViewer) > 0:
				print "(was", self._pdfViewer, ")",
			self._pdfViewer = raw_input('')
			f.write("PDFViewer = " + self._pdfViewer + "\n")


			f.close()
		except IOError:
			"Something went wrong when opening ", self._filename, " for wirting."

	def getBibLocation(self):
		return self._BibLocation

	def getFilesLocation(self):
		return self._FilesLocation

	def getPDFViewer(self):
		return self._pdfViewer
