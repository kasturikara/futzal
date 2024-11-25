# Futzal

Futzal adalah sebuah aplikasi yang dibuat untuk memudahkan masyarakat dalam memesan lapangan futsal.

## Instalasi

1. Install env dengan menggunakan perintah `python -m venv env` dan `./env/bin/activate`
2. Clone repository ini ke komputer Anda dengan menggunakan perintah `git clone https://github.com/kasturikara/futzal.git`
3. Buka folder proyek yang telah di clone dan jalankan perintah `pip install -r requirements.txt` untuk menginstalasi semua dependensi yang dibutuhkan
4. Buatlah database dengan menggunakan perintah `python manage.py makemigrations` dan `python manage.py migrate`
5. Jalankan server dengan menggunakan perintah `python manage.py runserver`

## Penggunaan

1. Buka browser Anda dan akses ke alamat `http://localhost:8000/`
2. Anda akan diarahkan ke halaman login, silakan login dengan menggunakan akun yang telah Anda buat
3. Setelah login, Anda akan diarahkan ke halaman dashboard, di mana Anda dapat memesan lapangan futsal yang tersedia

