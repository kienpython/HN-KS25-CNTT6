from hrm_package.feature import check_exits

def clock_in(attendance_book):
    employee_id = input("Nhập mã nhân viên: ").strip().upper()
    if check_exits(attendance_book, employee_id) :
        print("Nhân viên đã tồn tại!")
        return
    name = input("Nhập tên nhân viên: ")
    clock_in = input("Nhập giờ vào (HH:MM): ")
    attendance_book.append({
        "id": employee_id, 
        "name": name, 
        "times": (clock_in, None)
    })
    print(f"Thành công: Đã ghi nhận {employee_id} chấm công vào lúc 09:00!")

