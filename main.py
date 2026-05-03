import tkinter as tk
from tkinter import ttk, messagebox
import database 

# --- 1. ĐỊNH NGHĨA CÁC HÀM XỬ LÝ ---
def hien_thi_danh_sach():
    for item in tree.get_children():
        tree.delete(item)
    danh_sach = database.lay_tat_ca_sach()
    for sach in danh_sach:
        tree.insert("", tk.END, values=(sach[1], sach[2], sach[3]))

def nut_them_sach():
    ten = entry_ten.get()
    the_loai = entry_the_loai.get()
    trang_thai = combo_trang_thai.get()

    if ten:
        ket_qua = database.them_sach(ten, the_loai, trang_thai)
        
        if ket_qua:
            messagebox.showinfo("Thành công", f"Đã thêm: {ten}")
            entry_ten.delete(0, tk.END)
            entry_the_loai.delete(0, tk.END)
            hien_thi_danh_sach()
        else:
            messagebox.showerror("Lỗi", f"Sách '{ten}' đã tồn tại trong tủ sách!")
    else:
        messagebox.showwarning("Lỗi", "Vui lòng nhập tên sách!")

    

def nut_cap_nhat_sach():
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showwarning("Lỗi", "Vui lòng chọn một cuốn sách từ bảng!")
        return
    item_values = tree.item(selected_item, "values")
    ten_sach = item_values[0]
    trang_thai_moi = combo_trang_thai.get()
    database.cap_nhat_trang_thai(ten_sach, trang_thai_moi)
    messagebox.showinfo("Thành công", f"Đã cập nhật trạng thái mới!")
    hien_thi_danh_sach()
    entry_ten.delete(0, tk.END)
    entry_the_loai.delete(0, tk.END)
    combo_trang_thai.current(0)

def khi_chon_dong(event):
    selected_item = tree.selection()
    if selected_item:
        item_values = tree.item(selected_item, "values")
        entry_ten.delete(0, tk.END)
        entry_ten.insert(0, item_values[0])
        entry_the_loai.delete(0, tk.END)
        entry_the_loai.insert(0, item_values[1])
        combo_trang_thai.set(item_values[2])

def nut_xoa_sach():
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showwarning("Lỗi", "Vui lòng chọn cuốn sách cần xóa!")
        return
    
    item_values = tree.item(selected_item, "values")
    ten_sach = item_values[0]
    
    # Hiển thị hộp thoại xác nhận
    tra_loi = messagebox.askyesno("Xác nhận", f"Bạn có chắc chắn muốn xóa cuốn: {ten_sach}?")
    if tra_loi:
        database.xoa_sach(ten_sach)
        messagebox.showinfo("Thành công", "Đã xóa sách khỏi danh sách!")
        hien_thi_danh_sach() 
        entry_ten.delete(0, tk.END)
        entry_the_loai.delete(0, tk.END)
        combo_trang_thai.current(0)

# --- 2. THIẾT LẬP GIAO DIỆN ---
root = tk.Tk()
root.title("Quản lý Tủ sách Cá nhân")
root.geometry("500x600")

# Nhập liệu
tk.Label(root, text="Tên sách:").pack(pady=5)
entry_ten = tk.Entry(root, justify="center")
entry_ten.pack(padx=10, fill="x")

tk.Label(root, text="Thể loại:").pack(pady=5)
entry_the_loai = tk.Entry(root, justify="center")
entry_the_loai.pack(padx=10, fill="x")

tk.Label(root, text="Trạng thái:").pack(pady=5)
combo_trang_thai = ttk.Combobox(root, values=["Chưa đọc", "Đang đọc", "Đã đọc"], width=37)
combo_trang_thai.current(0)
combo_trang_thai.pack()

# Nút bấm
btn_them = tk.Button(root, text="Thêm mới", command=nut_them_sach, bg="green", fg="white", width=20)
btn_them.pack(pady=10)

btn_cap_nhat = tk.Button(root, text="Cập nhật trạng thái", command=nut_cap_nhat_sach, bg="orange", width=20)
btn_cap_nhat.pack(pady=5)

btn_xoa = tk.Button(root, text="Xóa sách đang chọn", command=nut_xoa_sach, bg="red", fg="white", width=20)
btn_xoa.pack(pady=5)

# Bảng hiển thị 
columns = ("ten", "loai", "trang_thai")
tree = ttk.Treeview(root, columns=columns, show="headings", height=10)
tree.heading("ten", text="Tên Sách")
tree.heading("loai", text="Thể loại")
tree.heading("trang_thai", text="Trạng thái")
tree.pack(padx=10, pady=10, fill="x")
# Cấu hình các cột
tree.column("ten", width=200, anchor="center") 
tree.column("loai", width=150, anchor="center")
tree.column("trang_thai", width=100, anchor="center")

# Cấu hình tiêu đề
tree.heading("ten", text="Tên Sách", anchor="center") 
tree.heading("loai", text="Thể loại", anchor="center")
tree.heading("trang_thai", text="Trạng thái", anchor="center")


# --- 3. KẾT NỐI SỰ KIỆN VÀ CHẠY ---
tree.bind("<<TreeviewSelect>>", khi_chon_dong) 
hien_thi_danh_sach()

root.mainloop()
