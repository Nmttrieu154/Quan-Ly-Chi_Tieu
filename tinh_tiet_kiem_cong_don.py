def tinh_tiet_kiem_cong_don(data):

    tong_cong_don = 0

    print("===== TIẾT KIỆM CỘNG DỒN =====")

    for thang, danh_muc in data.items():

        tong_chi = sum(danh_muc.values())

        # Giả sử thu nhập mỗi tháng là 10 triệu
        tong_thu = 10000000

        tiet_kiem = tong_thu - tong_chi

        tong_cong_don += tiet_kiem

        print("\nTháng:", thang)
        print("Tổng chi:", tong_chi)
        print("Tiết kiệm tháng:", tiet_kiem)
        print("Tiết kiệm cộng dồn:", tong_cong_don)


tinh_tiet_kiem_cong_don(data)
