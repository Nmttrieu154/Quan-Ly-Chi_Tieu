# ============================================================
# giao_dien.py  —  Giao diện + xử lý khi bấm nút
# Bạn cần điền code vào các hàm có chữ TODO ở phía dưới
# ============================================================

import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
import ham_xu_ly as h

# Danh sách danh mục cố định
DANH_MUC_THU = ["Lương", "Thưởng", "Đầu tư", "Khác"]
DANH_MUC_CHI = [
    "Ăn uống",
    "Học tập",
    "Giải trí",
    "Đi lại",
    "Mua sắm",
    "Hóa đơn",
    "Y tế",
    "Khác",
]


# ============================================================
# CÁC HÀM XỬ LÝ SỰ KIỆN  (gọi khi bấm nút)
# ============================================================


def doi_danh_muc(*args):
    loai = var_loai.get()
    if loai == "thu":
        cb_danh_muc.config(values=DANH_MUC_THU)
        cb_danh_muc.set(DANH_MUC_THU[0])
    else:
        cb_danh_muc.config(values=DANH_MUC_CHI)
        cb_danh_muc.set(DANH_MUC_CHI[0])


def them_giao_dich():
    loai = var_loai.get()
    danh_muc = cb_danh_muc.get().strip()
    so_tien_str = e_so_tien.get().strip()
    ngay = e_ngay.get().strip()
    ghi_chu = e_ghi_chu.get().strip()
    if not danh_muc or not so_tien_str or not ngay:
        messagebox.showwarning(
            "Lỗi nhập liệu", "Vui lòng nhập đầy đủ Danh mục, Số tiền và Ngày!"
        )
        return
    try:
        so_tien = int(so_tien_str)
        if so_tien <= 0:
            messagebox.showwarning("Lỗi nhập liệu", "Số tiền phải lớn hơn 0!")
            return
    except ValueError:
        messagebox.showwarning(
            "Lỗi nhập liệu",
            "Số tiền phải là số nguyên (không chứa chữ hoặc ký tự đặc biệt)!",
        )
        return
    try:
        datetime.strptime(ngay, "%Y-%m-%d")
    except ValueError:
        messagebox.showwarning(
            "Lỗi nhập liệu", "Ngày phải nhập đúng định dạng YYYY-MM-DD!"
        )
        return
    ds = h.doc_giao_dich()

    id_moi = max([gd["id"] for gd in ds], default=0) + 1

    gd_moi = {
        "id": id_moi,
        "loai": loai,
        "danh_muc": danh_muc,
        "so_tien": so_tien,
        "ngay": ngay,
        "ghi_chu": ghi_chu,
    }

    ds.append(gd_moi)
    h.luu_giao_dich(ds)

    messagebox.showinfo(
        "Thành công", f"Đã lưu giao dịch:\n[{loai.upper()}] {danh_muc} - {so_tien:,} đ"
    )

    e_so_tien.delete(0, tk.END)
    e_ghi_chu.delete(0, tk.END)

    hien_thi_danh_sach()

    if loai == "chi":
        thang = ngay[:7]  # Lấy chuỗi YYYY-MM từ ngày
        canh_bao_ngan_sach(danh_muc, thang)


def luu_ngan_sach_ui():
    thang = e_ns_thang.get().strip()
    danh_muc = cb_ns_dm.get().strip()
    han_muc_str = e_ns_hanmuc.get().strip()

    if not thang or not danh_muc or not han_muc_str:
        messagebox.showwarning(
            "Thiếu thông tin", "Vui lòng nhập đầy đủ tháng, danh mục và hạn mức."
        )
        return

    try:
        han_muc = int(han_muc_str)
        if han_muc <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Lỗi", "Hạn mức phải là số nguyên dương.")
        return

    ns = h.doc_ngan_sach()

    if thang not in ns:
        ns[thang] = {}
    ns[thang][danh_muc] = han_muc

    h.luu_ngan_sach(ns)
    messagebox.showinfo(
        "Thành công", f"Đã lưu ngân sách:\n{danh_muc} | Tháng {thang}: {han_muc:,} đ"
    )

    canh_bao_ngan_sach(danh_muc, thang)


def canh_bao_ngan_sach(danh_muc, thang):
    ns = h.doc_ngan_sach()
    ds = h.doc_giao_dich()

    if thang not in ns or danh_muc not in ns[thang]:
        return

    han_muc = ns[thang][danh_muc]
    tong_chi = h.tinh_tong_theo_danh_muc(ds, danh_muc, thang)

    if tong_chi > han_muc:
        messagebox.showwarning(
            "⚠️ Vượt ngân sách!",
            f"Danh mục: {danh_muc}\n"
            f"Tháng: {thang}\n"
            f"Hạn mức: {han_muc:,} đ\n"
            f"Đã chi: {tong_chi:,} đ\n"
            f"Vượt: {tong_chi - han_muc:,} đ",
        )


# xong Nhân
def hien_thi_danh_sach():
    thang = e_loc_thang.get().strip()
    loai_loc = var_loai_loc.get()
    if loai_loc == "tat_ca":
        loai_loc = ""

    dm_loc = var_dm_loc.get()
    if dm_loc == "tat_ca":
        dm_loc = ""

    ds = h.doc_giao_dich()
    ket_qua = h.loc_giao_dich(ds, thang, loai_loc, dm_loc)

    for i in range(len(ket_qua) - 1):
        for j in range(i + 1, len(ket_qua)):
            if ket_qua[i]["ngay"] < ket_qua[j]["ngay"]:
                ket_qua[i], ket_qua[j] = ket_qua[j], ket_qua[i]

    for row in tree.get_children():
        tree.delete(row)

    for gd in ket_qua:
        ten_loai = "Thu" if gd["loai"] == "thu" else "Chi"
        tree.insert(
            "",
            "end",
            values=(
                gd["ngay"],
                ten_loai,
                gd["danh_muc"],
                f"{gd['so_tien']:,} đ",
                gd.get("ghi_chu", ""),
            ),
        )

    thang_tk = thang if thang != "" else datetime.now().strftime("%Y-%m")

    tong_thu = h.tinh_tong(ds, "thu", thang_tk)
    tong_chi = h.tinh_tong(ds, "chi", thang_tk)
    tiet_kiem_t = tong_thu - tong_chi  # tháng này
    tiet_kiem_cd = h.tinh_tiet_kiem_cong_don(ds, thang_tk)  # cộng dồn

    lbl_tk.config(
        text=(
            f"Tháng {thang_tk}:   "
            f"Thu {tong_thu:,} đ   |   "
            f"Chi {tong_chi:,} đ   |   "
            f"Tiết kiệm tháng: {tiet_kiem_t:,} đ   |   "
            f"Cộng dồn: {tiet_kiem_cd:,} đ"
        )
    )


# xong Nhân
def hien_tat_ca():
    e_loc_thang.delete(0, tk.END)  # clear month filter field
    var_loai_loc.set("tat_ca")  # đặt lại combobox loại về "tất cả"
    var_dm_loc.set("tat_ca")  # đặt lại combobox danh mục về "tất cả"
    hien_thi_danh_sach()  # hiện lại bảng


# ============================================================
# TẠO CỬA SỔ VÀ WIDGET
# (phần này không cần sửa gì nhé)
# ============================================================

root = tk.Tk()
root.title("Quản Lý Chi Tiêu Cá Nhân")
root.geometry("900x650")

tk.Label(
    root,
    text="QUẢN LÝ CHI TIÊU CÁ NHÂN",
    font=("Arial", 15, "bold"),
    fg="navy",
).pack(pady=8)

frm_top = tk.Frame(root)
frm_top.pack(padx=10, fill="x")

# --- Khung thêm giao dịch ---
frm_nhap = tk.LabelFrame(frm_top, text="Thêm giao dịch", padx=10, pady=8)
frm_nhap.grid(row=0, column=0, padx=5, pady=5, sticky="n")

var_loai = tk.StringVar(value="chi")
var_loai.trace_add("write", doi_danh_muc)
tk.Radiobutton(frm_nhap, text="Thu", variable=var_loai, value="thu", fg="green").grid(
    row=0, column=0
)
tk.Radiobutton(frm_nhap, text="Chi", variable=var_loai, value="chi", fg="red").grid(
    row=0, column=1
)

tk.Label(frm_nhap, text="Danh mục:").grid(row=1, column=0, sticky="w", pady=4)
cb_danh_muc = ttk.Combobox(frm_nhap, values=DANH_MUC_CHI, state="readonly", width=18)
cb_danh_muc.set(DANH_MUC_CHI[0])
cb_danh_muc.grid(row=1, column=1, pady=4)

tk.Label(frm_nhap, text="Số tiền (đ):").grid(row=2, column=0, sticky="w", pady=4)
e_so_tien = tk.Entry(frm_nhap, width=20)
e_so_tien.grid(row=2, column=1, pady=4)

tk.Label(frm_nhap, text="Ngày (yyyy-mm-dd):").grid(row=3, column=0, sticky="w", pady=4)
e_ngay = tk.Entry(frm_nhap, width=20)
e_ngay.insert(0, datetime.now().strftime("%Y-%m-%d"))
e_ngay.grid(row=3, column=1, pady=4)

tk.Label(frm_nhap, text="Ghi chú:").grid(row=4, column=0, sticky="w", pady=4)
e_ghi_chu = tk.Entry(frm_nhap, width=20)
e_ghi_chu.grid(row=4, column=1, pady=4)

tk.Button(
    frm_nhap,
    text="LƯU GIAO DỊCH",
    bg="navy",
    fg="white",
    width=20,
    command=them_giao_dich,
).grid(row=5, column=0, columnspan=2, pady=10)

# --- Khung ngân sách ---
frm_ns = tk.LabelFrame(frm_top, text="Đặt ngân sách tháng", padx=10, pady=8)
frm_ns.grid(row=0, column=1, padx=5, pady=5, sticky="n")

tk.Label(frm_ns, text="Tháng (yyyy-mm):").grid(row=0, column=0, sticky="w", pady=4)
e_ns_thang = tk.Entry(frm_ns, width=14)
e_ns_thang.insert(0, datetime.now().strftime("%Y-%m"))
e_ns_thang.grid(row=0, column=1, pady=4)

tk.Label(frm_ns, text="Danh mục:").grid(row=1, column=0, sticky="w", pady=4)
cb_ns_dm = ttk.Combobox(frm_ns, values=DANH_MUC_CHI, state="readonly", width=14)
cb_ns_dm.set(DANH_MUC_CHI[0])
cb_ns_dm.grid(row=1, column=1, pady=4)

tk.Label(frm_ns, text="Hạn mức (đ):").grid(row=2, column=0, sticky="w", pady=4)
e_ns_hanmuc = tk.Entry(frm_ns, width=14)
e_ns_hanmuc.grid(row=2, column=1, pady=4)

tk.Button(
    frm_ns,
    text="LƯU NGÂN SÁCH",
    bg="green",
    fg="white",
    width=18,
    command=luu_ngan_sach_ui,
).grid(row=3, column=0, columnspan=2, pady=10)

# --- Khung lọc ---
frm_loc = tk.Frame(root)
frm_loc.pack(padx=10, pady=3, fill="x")

tk.Label(frm_loc, text="Lọc tháng (yyyy-mm):").pack(side="left", padx=4)
e_loc_thang = tk.Entry(frm_loc, width=10)
e_loc_thang.pack(side="left", padx=4)

tk.Label(frm_loc, text="Loại:").pack(side="left", padx=4)
var_loai_loc = tk.StringVar(value="tat_ca")
ttk.Combobox(
    frm_loc,
    textvariable=var_loai_loc,
    values=["tat_ca", "thu", "chi"],
    width=8,
    state="readonly",
).pack(side="left", padx=4)

tk.Label(frm_loc, text="Danh mục:").pack(side="left", padx=4)
var_dm_loc = tk.StringVar(value="tat_ca")
ttk.Combobox(
    frm_loc,
    textvariable=var_dm_loc,
    values=["tat_ca"] + DANH_MUC_THU + DANH_MUC_CHI,
    width=14,
    state="readonly",
).pack(side="left", padx=4)

tk.Button(frm_loc, text="Lọc", width=6, command=hien_thi_danh_sach).pack(
    side="left", padx=4
)
tk.Button(frm_loc, text="Hiện tất cả", width=10, command=hien_tat_ca).pack(
    side="left", padx=4
)

# --- Bảng danh sách ---
tree = ttk.Treeview(
    root,
    columns=("ngay", "loai", "danh_muc", "so_tien", "ghi_chu"),
    show="headings",
    height=12,
)
tree.heading("ngay", text="Ngày")
tree.heading("loai", text="Loại")
tree.heading("danh_muc", text="Danh mục")
tree.heading("so_tien", text="Số tiền")
tree.heading("ghi_chu", text="Ghi chú")
tree.column("ngay", width=100)
tree.column("loai", width=55)
tree.column("danh_muc", width=130)
tree.column("so_tien", width=120)
tree.column("ghi_chu", width=280)
tree.pack(padx=10, pady=5, fill="x")

# --- Nhãn thống kê ---
lbl_tk = tk.Label(
    root,
    text="(Chưa có dữ liệu)",
    font=("Arial", 10, "bold"),
    fg="navy",
    bg="#e8f4fd",
)
lbl_tk.pack(pady=5, fill="x", padx=10)


# ============================================================
# HÀM CHẠY (gọi từ main.py)
# ============================================================


def chay():
    #hien_thi_danh_sach()
    root.mainloop()
