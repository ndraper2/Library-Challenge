class Library(object):
	'A simple library that holds a list of shelves.'

	def __init__(self, name):
		self.name = name
		self.shelves = []

	def addShelf(self, newShelf):
		self.shelves.append(newShelf)
		print "New shelf built in Library.\n"

	def display(self):
		print "Contents of library:\n"
		for x in self.shelves:
			x.display()
		print "Complete. \n"


class Shelf(object):
	'Shelves hold a list of books.'

	def __init__(self, number):
		self.number = number
		self.books = []

	def add(self, newBook):
		self.books.append(newBook)

	def display(self):
		print "Contents of shelf", self.number + ":\n"
		for x in self.books:
			x.display()

	def remove(self, rBook):
		if rBook in self.books:
			self.books.remove(rBook)
		else:
			print "Book not found on shelf.\n"


class Book(object):
	'Books have a title, an author, and a shelf.'

	def __init__(self, title, author):
		self.title = title
		self.author = author
		self.shelf = None

	def enshelf(self, newShelf):
		if newShelf in myLibrary.shelves:
			newShelf.add(self)
			self.shelf = newShelf
			print "Book placed on shelf", self.shelf.number + ".\n"

		else:
			print "One must build a shelf before books can be placed on it.\n"

	def unshelf(self):
		self.shelf.remove(self)
		print "Book removed from shelf", self.shelf.number + ".\n"
		self.shelf = None



	def display(self):
		print "Title: ", self.title
		print "Author: ", self.author
		if self.shelf:
			print "On Shelf: ", self.shelf.number
		else:
			print "Not on a shelf."
		print ""



myLibrary = Library("Draper Public Library")
shelf1 = Shelf("1")
myLibrary.addShelf(shelf1)
book1 = Book("Survey of Theoretical Magic", "Nicholas Draper")
book1.enshelf(shelf1)
book1.display()

shelf2 = Shelf("2")
book1.enshelf(shelf2)
myLibrary.addShelf(shelf2)
book2 = Book("Magical Engineering", "Ryan Baker")
book2.enshelf(shelf2)

book1.unshelf()
book1.display()
book1.enshelf(shelf1)

shelf2.display()

myLibrary.display()