import tkinter as tk
from datetime import datetime
from tkinter import messagebox

def xu_ly_du_lieu():
  # 1. Lấy dữ liệu từ ô nhập bằng phương thức .get()
    thoi_gian_bam = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    mssv = o_nhap_ma_sv.get()
    ho_ten = o_nhap_ho_ten.get()
    
    # 2. In ra Terminal để lập trình viên kiểm tra
    print(f"[{thoi_gian_bam}] Dữ liệu nhận được: MSSV: {mssv} - Họ tên: {ho_ten}")
    
    # 3. Cập nhật trực tiếp lên giao diện (Label kết quả)
    if ho_ten != "":
        try:
            mssv_int = int(mssv)  # Cố gắng chuyển MSSV sang số nguyên
            nhan_ket_qua.config(text=f"Chào sinh viên: {ho_ten} ({mssv})", fg="blue")
        except ValueError:
            messagebox.showerror("Lỗi", "Mã sinh viên phải là một số nguyên.")
    else:
        messagebox.showwarning("Cảnh báo", "Vui lòng nhập họ tên sinh viên.")
    o_nhap_ma_sv.delete(0, tk.END)
    o_nhap_ho_ten.delete(0, tk.END)
    o_nhap_ma_sv.focus()

root = tk.Tk()
root.title("Quản lý Sinh viên - UHL")
root.geometry("400x350")
root.columnconfigure(1, weight=1)

# --- PHẦN GIAO DIỆN (Giữ nguyên từ Lộ trình 3) ---
tk.Label(root, text="Mã sinh viên:").grid(row=0, column=0, padx=10, pady=10, sticky="w")
o_nhap_ma_sv = tk.Entry(root)
o_nhap_ma_sv.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

tk.Label(root, text="Họ và tên:").grid(row=1, column=0, padx=10, pady=10, sticky="w")
o_nhap_ho_ten = tk.Entry(root)
o_nhap_ho_ten.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

# --- PHẦN MỚI: NÚT BẤM VÀ KẾT QUẢ ---

# Nút bấm có tham số 'command' kết nối tới hàm xử lý
nut_xac_nhan = tk.Button(root, text="Xác nhận điểm danh", command=xu_ly_du_lieu)
nut_xac_nhan.grid(row=2, column=0, columnspan=2, pady=10)

# Nhãn hiển thị kết quả ngay trên giao diện
nhan_ket_qua = tk.Label(root, text="Chưa có dữ liệu", font=("Arial", 10, "italic"))
nhan_ket_qua.grid(row=3, column=0, columnspan=2, pady=20)

root.mainloop()
