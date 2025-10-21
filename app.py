from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

# Inisialisasi aplikasi Flask
app = Flask(__name__, template_folder='.')
app.secret_key = 'ganti_dengan_kunci_rahasia_yang_sangat_acak'

# Konfigurasi database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inisialisasi database
db = SQLAlchemy(app)

# Membuat rute untuk halaman utama
@app.route('/')
def home():
    # Flask akan mencari dan merender file 'index.html'
    return render_template('index.html')

# Menjalankan aplikasi jika file ini dieksekusi
if __name__ == '__main__':
    app.run(debug=False)