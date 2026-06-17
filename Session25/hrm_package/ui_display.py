
from tabulate import tabulate

def display_records(attendance_book):
    attendances = list()
    print("--- BẢNG CHẤM CÔNG ---")
    for attendance in attendance_book:
        clock_out = attendance['times'][1]
        clock_in = attendance['times'][0]
        if not clock_out:
            clock_out = "[Đang làm việc]"
        attendances.append([attendance['id'], attendance['name'], clock_in, clock_out])
    table = tabulate(
        attendances, 
        headers=["Mã NV", "Tên Nhân Viên", "Giờ Vào", "Giờ Ra"], 
        tablefmt="grid"
    )
    print(table)
