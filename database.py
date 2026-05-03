import sqlite3

def ket_noi():
    conn = sqlite3.connect("quan_ly_sach.db")
    cursor = conn.cursor()
    # Tạo bảng sách nếu chưa có
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS sach (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ten_sach TEXT NOT NULL UNIQUE,
            the_loai TEXT,
            trang_thai TEXT -- Đã đọc, Đang đọc, Chưa đọc
        )
    ''')
    conn.commit()
    return conn
def cap_nhat_trang_thai(ten_sach, trang_thai_moi):
    conn = sqlite3.connect("quan_ly_sach.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE sach SET trang_thai = ? WHERE ten_sach = ?", 
                   (trang_thai_moi, ten_sach))
    conn.commit()
    conn.close()


def them_sach(ten, the_loai, trang_thai):
    conn = ket_noi()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO sach (ten_sach, the_loai, trang_thai) VALUES (?, ?, ?)", 
                       (ten, the_loai, trang_thai))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()

def lay_tat_ca_sach():
    conn = ket_noi()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM sach")
    rows = cursor.fetchall()
    conn.close()
    return rows

def xoa_sach(ten_sach):
    conn = sqlite3.connect("quan_ly_sach.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM sach WHERE ten_sach = ?", (ten_sach,))
    conn.commit()
    conn.close()
