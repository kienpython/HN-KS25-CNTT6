from tabulate import tabulate
class Drink:
    def __init__(self, code, name, price):
        self.code = code 
        self.name = name
        self.__price = price
        self.is_vailable = True
    
    @property
    def price(self):
        return self.__price
    
    @property
    def status(self):
        if self.is_vailable:
            return "Đang bán"
        return "Ngừng bán"

def display_menu(menu):
    print("--- DANH SÁCH ĐỒ UỐNG ---")
    drinks = list()
    for drink in menu:
        drinks.append([drink.code, drink.name, drink.price, drink.status])
    table = tabulate(drinks, headers=['Mã món','Tên món','Giá bán','Trạng thái'])
    print(table)

def main():
    menu = [
        Drink("CF01", "Cà phê sữa", 35000),
        Drink("TS01", "Trà sữa matcha", 45000),
        Drink("TD01", "Trà đào cam sả", 40000)
    ]
    while True:
        choice = input("""=== HỆ THỐNG QUẢN LÝ THỰC ĐƠN RIKKEI COFFEE ===

        1. Xem danh sách đồ uống
        2. Thêm đồ uống mới
        3. Cập nhật trạng thái kinh doanh
        4. Thoát chương trình

        ==============================================
        Chọn chức năng (1-4): """)
        match choice:
            case "1":
                display_menu(menu)

if __name__ == "__main__":
    main()