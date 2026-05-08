def bang_tong_ket_theo_thang(data):

    print("===== BẢNG TỔNG KẾT =====")

    tong_cong_don = 0

    for thang, danh_muc in data.items():

        tong_chi = sum(danh_muc.values())

        # Giả sử thu nhập cố định mỗi tháng
        tong_thu = 10000000

        tiet_kiem = tong_thu - tong_chi

        tong_cong_don += tiet_kiem

        print("\nTháng:", thang)
        print("Tổng thu:", tong_thu)
        print("Tổng chi:", tong_chi)
        print("Tiết kiệm tháng:", tiet_kiem)
        print("Tiết kiệm cộng dồn:", tong_cong_don)


# DATA
data = {
    "2026-03": {
        "Ăn uống": 3000000,
        "Học tập": 1500000,
        "Giải trí": 1000000,
        "Đi lại": 800000,
        "Mua sắm": 2000000,
        "Hóa đơn": 1500000,
        "Y tế": 500000
    },

    "2026-04": {
        "Ăn uống": 3000000,
        "Học tập": 1500000,
        "Giải trí": 1000000,
        "Đi lại": 800000,
        "Mua sắm": 2000000,
        "Hóa đơn": 1500000,
        "Y tế": 500000
    },

    "2026-05": {
        "Ăn uống": 3000000,
        "Học tập": 1500000,
        "Giải trí": 1000000,
        "Đi lại": 800000,
        "Mua sắm": 2000000,
        "Hóa đơn": 1500000,
        "Y tế": 500000
    }
}

bang_tong_ket_theo_thang(data)
