import logging

def check_ticket_exits(tickets,ticket_id):
    for ticket in tickets:
        if ticket['ticket_id'] == ticket_id:
            return ticket
    return False

def input_format_float(message):
    while True:
        try:
            value = float(input(message))
            if value <= 0 :
                print("Giá vé phải lớn hơn 0. Vui lòng nhập lại.")   
            return value      
        except:
            print("Giá vé phải là số. Vui lòng nhập lại.")
            logging.warning("2026-06-04 10:14:30,333 - WARNING - Invalid price input while booking ticket")

def input_format_int(message):
    while True:
        try:
            value = int(input(message))
            if value <= 0 :
                print("Số ghế phải lớn hơn 0. Vui lòng nhập lại.")   
            return value
        except:
            print("Số ghế phải là số. Vui lòng nhập lại.")
            logging.warning("2026-06-04 10:14:30,333 - WARNING - Invalid seat input while booking ticket")


def book_ticket(tickets):
    print("--- ĐẶT VÉ MỚI ---")
    ticket_id = input("Nhập mã vé: ").strip().upper()

    if check_ticket_exits(tickets,ticket_id):
        print(f"Lỗi: Mã vé {ticket_id} đã tồn tại.")
        logging.warning("2026-06-04 10:13:05,222 - WARNING - Duplicate ticket ID entered: T01")
        return
    
    buyer_name = input("Nhập tên khách hàng:")
    price = input_format_float("Nhập giá vé: ")
    ticket_zone = input("Nhập khu vực ghế: ")
    seat_quantity = input_format_int("Nhập số ghế: ")
    seat = (ticket_zone,seat_quantity)
    new_ticket = {
        "ticket_id": ticket_id, 
        "buyer_name": buyer_name, 
        "price": price, 
        "status": "Booked", 
        "seat": seat
        }
    tickets.append(new_ticket)
    print(f"Thành công: Đã đặt vé {ticket_id} cho khách hàng {buyer_name}.")
    logging.info(f"Booked new ticket {ticket_id} for {buyer_name}")


def display_tickets(tickets):
    if not tickets:
        print("Hiện chưa có vé nào trong hệ thống.")
        return 
    print("""--- DANH SÁCH VÉ ---
Mã Vé | Tên Khách Hàng  | Giá Vé  | Chỗ Ngồi | Trạng Thái
-----------------------------------------------------------""")
    check_viewed = False
    for index,ticket in enumerate(tickets):
        # print("{} | {ticket_id:<6} | {buyer_name:<20} | {price:<10} | {status:<10} | {seat}".format(index+1,**ticket))
        try:
            ticket_id = ticket['ticket_id']
            buyer_name = ticket['buyer_name']
            price = ticket['price']
            status = ticket['status']
            seat = ticket['seat']
            if status == "Cancelled":
                status += " [ĐÃ HỦY]"
            print(f"{ticket_id}   | {buyer_name}    | {price}   | {seat[0]}-{seat[1]}      | {status}")
            check_viewed = True
        except KeyError as error:
            print("Lỗi: Một vé đang bị thiếu dữ liệu, vui lòng kiểm tra lại.")
    if check_viewed:
        logging.info("User viewed ticket list.")
    else:
        logging.error("Missing key while displaying ticket: 'seat'")
    print("-----------------------------------------------------------")


def change_seat(tickets):
    print("--- ĐỔI CHỖ NGỒI ---")
    ticket_id = input("Nhập mã vé cần đổi chỗ: ").strip().upper()
    ticket = check_ticket_exits(tickets,ticket_id)
    if not ticket:
        print(f"Không tìm thấy vé mang mã {ticket_id}.")
        logging.warning(f"Change seat failed - Ticket {ticket_id} not found")
        return
    
    seat_zone = input("Nhập khu vực ghế mới: ")
    seat_quantity = input_format_int("Nhập số ghế mới: ")
    seat = (seat_zone,seat_quantity)
    ticket['seat'] = seat
    logging.info(f"Seat changed for ticket {ticket_id} to {seat_zone}-{seat_quantity}")

def cancel_ticket(tickets):
    print("--- HỦY VÉ ---")
    ticket_id = input("Nhập mã vé cần đổi chỗ: ").strip().upper()
    ticket = check_ticket_exits(tickets,ticket_id)
    if not ticket:
        print(f"Không tìm thấy vé mang mã {ticket_id}.")
        logging.warning(f"Cancel ticket failed - Ticket {ticket_id} not found")
        return
    if ticket['status'] == "Cancelled":
        print(f"Vé {ticket_id} đã ở trạng thái Cancelled trước đó.")
        return
    ticket['status'] = "Cancelled"
    print(f"Thành công: Vé {ticket_id} đã được hủy.")
    logging.warning(f"Ticket {ticket_id} has been cancelled.")

def calculate_revenue(tickets):
    total_revenue = 0
    total_ticket_booked = 0
    total_ticket_cancelled = 0
    for ticket in tickets:
        if ticket['status'] != "Cancelled":
            total_revenue += ticket['price']
            total_ticket_booked +=1
        else:
            total_ticket_cancelled +=1
    return total_revenue


def main():
    logging.basicConfig(
        filename="C:/Users/kienp/Downloads/Used/Teach/HN-KS25-CNTT6/Sesssion21/arena_tickets.log",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        encoding="utf-8"
    )
    ticket_db = [
        {"ticket_id": "T01", "buyer_name": "Nguyen Van A", "price": 500.0, "status": "Booked", "seat": ("A", 1)},
        {"ticket_id": "T02", "buyer_name": "Tran Thi B", "price": 300.0, "status": "Cancelled", "seat": ("B", 5)},
        {"ticket_id": "T03", "buyer_name": "Le Van C", "price": 500.0, "status": "Booked", "seat": ("A", 2)}
    ]
    while True:
        choice = input("""=== HỆ THỐNG QUẢN LÝ VÉ RIKKEI ESPORTS ===
            1. Xem danh sách vé đã bán
            2. Đặt vé mới
            3. Đổi chỗ ngồi (Cập nhật vé)
            4. Hủy vé
            5. Báo cáo doanh thu
            6. Thoát chương trình
            ======================================== 
            Chọn chức năng (1-6): """)
        match choice:
            case "1":
                display_tickets(ticket_db)
            case "2":
                book_ticket(ticket_db)
            case "3":
                change_seat(ticket_db)
            case "4":
                cancel_ticket(ticket_db)
            case "5":
                pass

if __name__ == "__main__":
    main()