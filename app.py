from flask import Flask, render_template, request, redirect, url_for, session, Response
import sqlite3
import csv
import io

app = Flask(__name__)
app.secret_key = 'kunci_rahasia_money_stocking'

def get_db_connection():
    conn = sqlite3.connect('moneystocking.db')
    conn.row_factory = sqlite3.Row
    return conn

# --- HALAMAN LOGIN ---
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        conn = get_db_connection()
        user = conn.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password)).fetchone()
        conn.close()
        
        if user:
            session['logged_in'] = True
            return redirect(url_for('dashboard'))
        else:
            return "Login Gagal! <a href='/'>Coba lagi</a>"
    return render_template('login.html')

# --- HALAMAN DASHBOARD ---
@app.route('/dashboard')
def dashboard():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
        
    conn = get_db_connection()
    transaksi = conn.execute('SELECT * FROM transaksi ORDER BY tanggal DESC').fetchall()
    
    total_masuk = conn.execute("SELECT SUM(nominal) FROM transaksi WHERE tipe='Pemasukan'").fetchone()[0] or 0
    total_keluar = conn.execute("SELECT SUM(nominal) FROM transaksi WHERE tipe='Pengeluaran'").fetchone()[0] or 0
    conn.close()
    
    return render_template('dashboard.html', transaksi=transaksi, masuk=total_masuk, keluar=total_keluar)

# --- TAMBAH TRANSAKSI ---
@app.route('/tambah', methods=['POST'])
def tambah():
    if not session.get('logged_in'): return redirect(url_for('login'))
    tanggal = request.form['tanggal']
    keterangan = request.form['keterangan']
    tipe = request.form['tipe']
    nominal = request.form['nominal']
    
    conn = get_db_connection()
    conn.execute('INSERT INTO transaksi (tanggal, keterangan, tipe, nominal) VALUES (?, ?, ?, ?)',
                 (tanggal, keterangan, tipe, nominal))
    conn.commit()
    conn.close()
    return redirect(url_for('dashboard'))

# --- EXPORT CSV ---
@app.route('/export')
def export():
    if not session.get('logged_in'): return redirect(url_for('login'))
    conn = get_db_connection()
    transaksi = conn.execute('SELECT * FROM transaksi').fetchall()
    conn.close()

    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(['ID', 'Tanggal', 'Keterangan', 'Tipe', 'Nominal'])
    for row in transaksi:
        writer.writerow([row['id'], row['tanggal'], row['keterangan'], row['tipe'], row['nominal']])
    
    return Response(output.getvalue(), mimetype="text/csv", headers={"Content-Disposition": "attachment;filename=laporan_money_stocking.csv"})

# --- LOGOUT ---
@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)