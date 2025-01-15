# Kelas Book untuk merepresentasikan buku di perpustakaan
class Book:
    def __init__(self, title, author, copies):
        # Inisialisasi atribut buku
        self.title = title
        self.author = author
        self.copies = copies

    # Metode untuk meminjam buku
    def borrow(self):
        if self.copies > 0:
            self.copies -= 1  # Mengurangi jumlah salinan jika tersedia
            print(f"You have borrowed '{self.title}'.")
        else:
            print("Book unavailable.")  # Pesan jika buku tidak tersedia

    # Metode untuk mengembalikan buku
    def return_book(self):
        self.copies += 1  # Menambah jumlah salinan saat buku dikembalikan
        print(f"You have returned '{self.title}'.")

# Kelas Library untuk mengelola daftar buku dan operasinya
class Library:
    def __init__(self):
        self.books = []  # Daftar buku di perpustakaan

    # Metode untuk menambahkan buku ke perpustakaan
    def add_book(self, book):
        self.books.append(book)

    # Metode untuk mencari buku berdasarkan judul
    def find_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book  # Mengembalikan objek buku jika ditemukan
        return None  # Mengembalikan None jika buku tidak ditemukan

    # Metode untuk meminjam buku berdasarkan judul
    def borrow_book(self, title):
        book = self.find_book(title)
        if book:
            book.borrow()  # Memanggil metode borrow() pada objek buku
        else:
            print("Book not found.")  # Pesan jika buku tidak ditemukan

    # Metode untuk mengembalikan buku berdasarkan judul
    def return_book(self, title):
        book = self.find_book(title)
        if book:
            book.return_book()  # Memanggil metode return_book() pada objek buku
        else:
            print("Book not found.")

    # Metode untuk menghasilkan laporan inventaris perpustakaan
    def generate_report(self, output_file):
        with open(output_file, 'w') as file:
            file.write("Library Inventory Report:\n")
            for i, book in enumerate(self.books, 1):
                file.write(f"{i}. {book.title} by {book.author} - Copies Available: {book.copies}\n")

# Contoh Penggunaan
library = Library()
library.add_book(Book("The Great Gatsby", "F. Scott Fitzgerald", 2))  # Menambahkan buku
library.add_book(Book("1984", "George Orwell", 5))
library.borrow_book("1984")  # Meminjam buku
library.return_book("1984")  # Mengembalikan buku
library.generate_report("library_report.txt")  # Menghasilkan laporan