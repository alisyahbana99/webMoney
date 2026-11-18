import sqlite3

def init_db():
    conn = sqlite3.connect('moneystocking.db')
    cursor = conn.cursor()
    
    # Tabel User
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    
    # Tabel Transaksi
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS transaksi (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            tanggal TEXT NOT NULL,
            keterangan TEXT NOT NULL,
            tipe TEXT NOT NULL,
            nominal INTEGER NOT NULL
        )
    ''')
    
    # Akun admin default
    cursor.execute("INSERT OR IGNORE INTO users (username, password) VALUES ('admin', 'admin111')")
    
    conn.commit()
    conn.close()
    print("Database Money-Stocking berhasil dibuat!")

if __name__ == '__main__':
    init_db()