from flask import Flask, render_template, request, redirect, url_for, flash, session
from werkzeug.security import generate_password_hash, check_password_hash
import pymysql
import pymysql.cursors

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Fungsi untuk membuat koneksi ke database
def get_db_connection():
    return pymysql.connect(
        host="localhost",
        user="root",
        password="",
        database="instyle_furniture",
        cursorclass=pymysql.cursors.DictCursor
    )

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = get_db_connection()
        cursor = conn.cursor()
        
        cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
        user = cursor.fetchone()

        cursor.close()
        conn.close()

        if user and check_password_hash(user['password_hash'], password):
            session['username'] = user['username']
            flash('Login berhasil!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Username atau password salah', 'danger')

    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        password_hash = generate_password_hash(password)

        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            
            cursor.execute("INSERT INTO users (username, password_hash) VALUES (%s, %s)", 
                           (username, password_hash))
            conn.commit()

            cursor.close()
            conn.close()

            flash('Registrasi berhasil! Silakan login.', 'success')
            return redirect(url_for('login'))
        except Exception as e:
            flash(f'Gagal mendaftar: {str(e)}', 'danger')

    return render_template('register.html')

import pymysql.cursors

@app.route('/dashboard')
def dashboard():
    conn = get_db_connection()
    cursor = conn.cursor(pymysql.cursors.DictCursor)  # Ubah ke DictCursor
    
    cursor.execute("SELECT name, stock FROM furniture")
    data = cursor.fetchall()
    
    cursor.close()
    conn.close()

    item_names = [row["name"] for row in data]
    item_stocks = [int(row["stock"]) for row in data]

    return render_template('dashboard.html', item_names=item_names, item_stocks=item_stocks)



@app.route('/kelola_barang')
def kelola_barang():
    page = request.args.get('page', 1, type=int)
    per_page = 10  # Jumlah item per halaman
    offset = (page - 1) * per_page

    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Hitung total data
    cursor.execute("SELECT COUNT(*) as total FROM furniture")
    total_items = cursor.fetchone()['total']
    total_pages = (total_items + per_page - 1) // per_page  # Hitung total halaman

    # Ambil data sesuai halaman
    cursor.execute("SELECT * FROM furniture LIMIT %s OFFSET %s", (per_page, offset))
    furniture = cursor.fetchall()

    cursor.close()
    conn.close()

    # ✅ Kirim semua variabel ke template
    return render_template("kelola_barang.html", furniture=furniture, page=page, total_pages=total_pages)

@app.route('/add_furniture', methods=['GET', 'POST'])
def add_furniture():
    if 'username' in session:
        conn = get_db_connection()
        cursor = conn.cursor()

        if request.method == 'POST':
            name = request.form['name']
            kategori = request.form['kategori']
            bahan = request.form.getlist('bahan[]')  # Mengambil multiple pilihan bahan
            bahan_str = ", ".join(bahan)  # Ubah menjadi string "Kayu Jati, Baja"
            price = request.form['price']
            stock = request.form['stock']

            cursor.execute("INSERT INTO furniture (name, kategori, bahan, price, stock) VALUES (%s, %s, %s, %s, %s)",
                           (name, kategori, bahan_str, price, stock))
            conn.commit()
            cursor.close()
            conn.close()

            flash('Barang berhasil ditambahkan!', 'success')
            return redirect(url_for('kelola_barang'))

        return render_template('add_furniture.html')

    return redirect(url_for('login'))

@app.route('/edit_furniture/<int:id>', methods=['GET', 'POST'])
def edit_furniture(id):
    if 'username' in session:
        conn = get_db_connection()
        cursor = conn.cursor()

        if request.method == 'POST':
            name = request.form['name']
            kategori = request.form['kategori']
            bahan = request.form.getlist('bahan[]')  # Ambil data dari checkbox
            bahan_str = ", ".join(bahan)  # Ubah menjadi string "Kayu Jati, Baja"
            price = request.form['price']
            stock = request.form['stock']

            cursor.execute("UPDATE furniture SET name = %s, kategori = %s, bahan = %s, price = %s, stock = %s WHERE id = %s",
                           (name, kategori, bahan_str, price, stock, id))
            conn.commit()
            cursor.close()
            conn.close()

            flash('Barang berhasil diperbarui!', 'success')
            return redirect(url_for('kelola_barang'))
        else:
            cursor.execute("SELECT * FROM furniture WHERE id = %s", (id,))
            furniture = cursor.fetchone()
            cursor.close()
            conn.close()

            # Memisahkan string bahan kembali menjadi daftar
            furniture = dict(furniture)
            furniture['bahan'] = furniture['bahan'].split(",")  # Mengubah "Kayu Jati,Baja" → ['Kayu Jati', 'Baja']

            return render_template('edit_furniture.html', furniture=furniture)

    return redirect(url_for('login'))

@app.route('/delete_furniture/<int:id>')
def delete_furniture(id):
    if 'username' in session:
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute("DELETE FROM furniture WHERE id = %s", (id,))
        conn.commit()

        cursor.close()
        conn.close()

        flash('Barang berhasil dihapus!', 'success')
        return redirect(url_for('kelola_barang'))

    return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop('username', None)
    flash('Anda telah logout.', 'info')
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
