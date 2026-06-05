# KHỞI TẠO CÁC BIẾN TÍCH LŨY BAN ĐẦU (Xử lý thời gian thực)
tong_doanh_thu = 0          # Cộng dồn tiền của tất cả hóa đơn
tong_so_hoa_don = 0         # Đếm tổng số lượng hóa đơn đã nhập
so_hoa_don_lon = 0          # Đếm riêng các hóa đơn từ 1,000,000 VND trở lên

# Biến đếm số thứ tự khách hàng hiển thị ra màn hình
thu_tu_khach = 1

print("=========================================================")
print("    HỆ THỐNG QUẢN LÝ DOANH THU THỜI GIAN THỰC STORE      ")
print("=========================================================\n")

# QUY TẮC 1: Vòng lặp vô hạn cho phép nhập liên tục cho đến khi chủ động dừng
while True:
    
    # Hỏi thu ngân xem có muốn nhập hóa đơn hay dừng lại luôn để xuất báo cáo
    lua_chon = input(f"Khách hàng {thu_tu_khach} - Bạn muốn nhập hóa đơn hay Dừng xuất báo cáo? (C để Tiếp tục / K để Dừng): ")
    
    # Kiểm tra xem thu ngân có chọn DỪNG (gõ k hoặc K) ngay từ đầu hoặc sau đó không
    if lua_chon == "k" or lua_chon == "K":
        break # Thoát ngay khỏi vòng lặp để xuống phần xuất báo cáo
        
    # Nếu chọn tiếp tục (hoặc gõ ký tự khác), tiến hành nhập giá trị hóa đơn
    gia_tri_input = input(f"-> Nhập giá trị hóa đơn Khách hàng {thu_tu_khach}: ")
    gia_tri_hien_tai = int(gia_tri_input)
    
    # QUY TẮC 2: Xử lý dữ liệu thời gian thực ngay khi vừa nhập xong một đơn
    tong_doanh_thu = tong_doanh_thu + gia_tri_hien_tai # Cộng dồn doanh thu
    tong_so_hoa_don = tong_so_hoa_don + 1              # Tăng tổng số hóa đơn lên 1
    
    # Kiểm tra xem có phải "hóa đơn lớn" hay không để ghi nhận riêng
    if gia_tri_hien_tai >= 1000000:
        so_hoa_don_lon = so_hoa_don_lon + 1
        
    # Tăng số thứ tự khách hàng để chuẩn bị cho lượt tiếp theo
    thu_tu_khach = thu_tu_khach + 1
    print() # In dòng trống cho dễ nhìn


# --- QUY TẮC 3 & 4: TÍNH TOÁN AN TOÀN & IN BÁO CÁO TỔNG KẾT ---
print("\n-- BÁO CÁO DOANH THU CUỐI NGÀY RIKKEI STORE")

# QUY TẮC 4: Phòng chống lỗi sập hệ thống do chia cho số 0 (ZeroDivisionError)
if tong_so_hoa_don == 0:
    ty_le_hoa_don_lon = 0.0 # Nếu chưa bán được đơn nào, tỷ lệ mặc định là 0%
else:
    # Nếu có hóa đơn, tính tỷ lệ: (Số đơn lớn / Tổng số đơn) * 100
    ty_le_hoa_don_lon = (so_hoa_don_lon / tong_so_hoa_don) * 100

# In toàn bộ kết quả tổng kết ra màn hình
print(f"Tổng số hóa đơn đã xử lý: {tong_so_hoa_don} hóa đơn.")
print(f"Tổng doanh thu ngày hôm nay: {tong_doanh_thu:,} VND.") # Dấu :, giúp tự động thêm dấu phẩy ngăn cách hàng nghìn
print(f"Số hóa đơn lớn (>= 1,000,000 VND): {so_hoa_don_lon} hóa đơn.")
print(f"Tỷ lệ hóa đơn lớn đạt: {ty_le_hoa_don_lon:.1f}% trên tổng số đơn hàng.")
print("=========================================================")