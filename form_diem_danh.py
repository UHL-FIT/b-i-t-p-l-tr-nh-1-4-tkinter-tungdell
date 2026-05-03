import tkinter as tk

root = tk.Tk()
root.title("Quản lý Sinh viên - UHL")
root.geometry("400x250")
root.columnconfigure(1, weight=1)

# 1. Tạo các thành phần (nhưng chưa hiện lên)
nhap_ma_sv = tk.Label(root, text="Mã sinh viên:")
o_nhap_ma_sv = tk.Entry(root)

nhap_ho_ten = tk.Label(root, text="Họ và tên:")
o_nhap_ho_ten = tk.Entry(root)
# Hàng 0
nhap_ma_sv.grid(row=0, column=0, padx=10, pady=10, sticky="w")
o_nhap_ma_sv.grid(row=0, column=1, sticky="ew") 

# Hàng 1
nhap_ho_ten.grid(row=1, column=0, padx=10, pady=10, sticky="w")
o_nhap_ho_ten.grid(row=1, column=1)

root.mainloop()
