pages = int(input("Enter number of pages in the book: "))
flash_gb = int(input("Enter flash capacity in GB: "))

page_size = 33 * 76 

book_size = pages * page_size 

flash_size = flash_gb * (10 ** 9)

number_of_books = flash_size // book_size

# Print the result
print("Number of books that can fit in the flash:", number_of_books)