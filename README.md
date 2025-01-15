# Library Management System

## Deskripsi
**Library Management System** adalah program sederhana berbasis Python untuk mengelola koleksi buku di perpustakaan. Program ini memiliki fungsi untuk:
- Menambahkan buku ke perpustakaan.
- Meminjam dan mengembalikan buku.
- Menghasilkan laporan inventaris perpustakaan dalam file teks.

## Fitur
### 1. Kelas `Book`
Merepresentasikan sebuah buku dengan atribut:
- **`title`**: Judul buku.
- **`author`**: Penulis buku.
- **`copies`**: Jumlah salinan buku yang tersedia.

#### Metode:
- **`borrow()`**: Mengurangi jumlah salinan saat buku dipinjam.
- **`return_book()`**: Menambah jumlah salinan saat buku dikembalikan.

### 2. Kelas `Library`
Mengelola koleksi buku dan berbagai operasi terkait.

#### Metode:
- **`add_book(book)`**: Menambahkan buku ke koleksi perpustakaan.
- **`find_book(title)`**: Mencari buku berdasarkan judul.
- **`borrow_book(title)`**: Meminjam buku berdasarkan judul.
- **`return_book(title)`**: Mengembalikan buku berdasarkan judul.
- **`generate_report(output_file)`**: Menghasilkan laporan inventaris ke file teks.

## Cara Menggunakan
### 1. Inisialisasi Perpustakaan
```python
library = Library()
```
### 2. Menambahkan Buku
```python
library.add_book(Book("The Great Gatsby", "F. Scott Fitzgerald", 2))
library.add_book(Book("1984", "George Orwell", 5))
```
### 3. Meminjam Buku
```python
library.borrow_book("1984")
```
### 4. Mengembalikan Buku
```python
library.return_book("1984")
```
### 5. Menghasilkan Laporan
```python
library.generate_report("library_report.txt")
```
### Contoh Laporan
```yaml
Library Inventory Report:
1. The Great Gatsby by F. Scott Fitzgerald - Copies Available: 2
2. 1984 by George Orwell - Copies Available: 5
