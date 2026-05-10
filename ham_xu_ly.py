# ============================================================
# ham_xu_ly.py  —  Hàm xử lý dữ liệu (đọc/ghi file, tính toán)
# Bạn cần điền code vào các hàm có chữ TODO
# ============================================================

import json
import os

# Tên 2 file dữ liệu (đặt trong cùng folder với main.py)
FILE_GD = "transactions.json"  # file chứa danh sách giao dịch
FILE_NS = "budgets.json"  # file chứa ngân sách theo tháng


# ============================================================
# ĐỌC / GHI FILE
# ============================================================


# Xong Nhân
def doc_giao_dich():
    if not os.path.exists(FILE_GD):
        return []
    with open(FILE_GD, "r", encoding="utf-8") as f:
        return json.load(f)


# Xong Nhân
def luu_giao_dich(ds):
    with open(FILE_GD, "w", encoding="utf-8") as f:
        json.dump(ds, f, ensure_ascii=False, indent=2)


# Xong Nhân
def doc_ngan_sach():
    if not os.path.exists(FILE_NS):
        return {}
    with open(FILE_NS, "r", encoding="utf-8") as f:
        return json.load(f)


# Xong Nhân
def luu_ngan_sach(ns):
    with open(FILE_NS, "w", encoding="utf-8") as f:
        json.dump(ns, f, ensure_ascii=False, indent=2)


# ============================================================
# TÍNH TOÁN
# ============================================================


def tinh_tong(ds, loai, thang):
    tong = 0
    for gd in ds:
        if gd["loai"] == loai and gd["ngay"][:7] == thang:
            tong += gd["so_tien"]
    return tong


def tinh_tong_theo_danh_muc(ds, danh_muc, thang):
    tong = 0
    for gd in ds:
        if (
            gd["ngay"][:7] == thang
            and gd["loai"] == "chi"
            and gd["danh_muc"].lower() == danh_muc.lower()
        ):
            tong += gd["so_tien"]
    return tong


# Thời xong
def loc_giao_dich(ds, thang="", loai="", danh_muc=""):
    ket_qua = []
    for gd in ds:
        thang_gd = gd["ngay"][:7]
        dieu_kien_thang = thang == "" or thang_gd == thang
        dieu_kien_loai = loai == "" or gd["loai"].lower() == loai.lower()
        dieu_kien_danh_muc = (
            danh_muc == "" or gd["danh_muc"].lower() == danh_muc.lower()
        )

        if dieu_kien_thang and dieu_kien_loai and dieu_kien_danh_muc:
            ket_qua.append(gd)
    return ket_qua


def tinh_tiet_kiem_cong_don(ds, thang):
    tiet_kiem_cd = 0
    for gd in ds:
        if gd["ngay"][:7] <= thang:
            if gd["loai"] == "thu":
                tiet_kiem_cd += gd["so_tien"]
            else:
                tiet_kiem_cd -= gd["so_tien"]
    return tiet_kiem_cd
