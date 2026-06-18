# Publich : Su dung o ngoai class va trong
# Protected: _ : chi su dung trong class va trong class ke thua
# private: __: chi su dung trong class ma mk khai bao 

from abc import ABC, abstractmethod
class BaseAccount(ABC):
    bank_name = "Vietcombank"
    def __init__(self, account_number, account_name, balance=0):
        self.__balance = balance
        self.account_number = account_number
        self.account_name = account_name.strip().upper()

    @property
    def balance(self):
        return self.__balance

    @abstractmethod 
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

    @staticmethod
    def validate_account_number(account_number):
        if account_number.isdigit() and len(account_number) == 10:
            return True
        return False
    
    @classmethod
    def update_bank_name(cls, new_name):
        cls.bank_name = new_name

    def __add__(self, other):
        return self.balance + other.balance
    
    def __lt__(self, other):
        return self.balance < other.balance
    
    def __eq__(self, other):
        return self.balance == other.balance
    
    def _increase_amount(self, amount):
        self.__balance += amount
    
    def _decrease_amount(self, amount):
        self.__balance -= amount
    
class SavingsAccount(BaseAccount):
    def __init__(self, account_number, account_name, interest_rate, balance = 0):
        super().__init__(account_number, account_name, balance)
        self.interest_rate = interest_rate 

    def deposit(self, amount):
        self._increase_amount(amount)

    def withdraw(self, amount):
        penalty = amount * 0.02
        total_amount = amount + penalty
        if self.balance - total_amount < 0 :
            print("Số tiền không đủ để rút!")
        self._decrease_amount(total_amount)

    def apply_interest(self):
        interest_money = self.balance*self.interest_rate
        self._increase_amount(self.balance*self.interest_rate)
        return interest_money

class CreditAccount(BaseAccount):
    def __init__(self, account_number, account_name, credit_limit, balance = 0 ):
        super().__init__(account_number, account_name, balance)
        self.credit_limit = credit_limit

    def deposit(self, amount):
        pass

    def withdraw(self, amount):
        if not (self.balance - amount >= -self.credit_limit):
            print("Vượt hạn mức!")
            return 
        self._decrease_amount(amount)

class DigitalPremiumMixin:
    def cashback_reward(self, amount):
        if amount > 5000000:
            return amount * 0.01
        return 0

class HybridAccount(SavingsAccount, DigitalPremiumMixin):
    pass
    
def open_account(current_account, accounts):
    choice_type_account = input("""1. Savings Account (Tài khoản Tiết kiệm)
2. Credit Account (Tài khoản Tín dụng)
3. Hybrid Account (Tài khoản Đa năng)
Chọn loại tài khoản (1-3): """)
    if choice_type_account not in ["1","2","3"]:
        print("Lựa chọn không hợp lệ!")
        return
    
    account_number = input("Nhập số tài khoản 10 chữ số: ")
    if not (BaseAccount.validate_account_number(account_number)):
        print("Số tài khoản không hợp lệ! Phải gồm đúng 10 chữ số.")
        return
    
    account_name = input("Nhập tên chủ tài khoản: ")
    if choice_type_account == "1":
        interest_rate = float(input("Nhập lãi suất năm (ví dụ 0.05): "))
        current_account = SavingsAccount(account_number, account_name, interest_rate)
    if choice_type_account == "2":
        credit_limit = float(input("Nhập hạn mức: "))
        current_account = CreditAccount(account_number, account_name, credit_limit)
    if choice_type_account == "3":
        interest_rate = float(input("Nhập lãi suất năm (ví dụ 0.05): "))
        current_account = HybridAccount(account_number, account_name, interest_rate)
    print("Mở tài khoản Tiết kiệm thành công!")
    print(f"Chủ tài khoản: {account_name}")
    accounts.append(current_account)
    return current_account

def display_info(current_account):
    if not current_account:
        print("Hệ thống chưa có thông tin tài khoản. Vui lòng mở tài khoản ở Chức năng 1 trước.")
        return
    print("--- THÔNG TIN TÀI KHOẢN HIỆN TẠI ---")
    print(f"Loại tài khoản: {current_account.__class__.__name__}")
    print(f"Ngân hàng: {current_account.bank_name}")
    print(f"Số tài khoản: {current_account.account_number}")
    print(f"Chủ tài khoản: {current_account.account_name}")
    print(f"Số dư: {current_account.balance} VNĐ")
    if current_account.__class__.__name__ in ["SavingsAccount", "HybridAccount"]:
        print(f"Lãi suất: {float(current_account.interest_rate)*100}% / năm")
    else:
        print(f"Hạn mức: {current_account.credit_limit} VNĐ")

def transaction(current_account):
    print("--- GIAO DỊCH NẠP / RÚT TIỀN ---")
    choice = input("""1. Nạp tiền
2. Rút tiền
Chọn giao dịch (1-2): """)
    if choice == "1":
        amount = float(input("Nhập số tiền nạp: "))
        print("Nạp tiền thành công!")
        print(f"[Ưu đãi Premium]: Bạn được hoàn tiền 1% ({amount*0.01:,.0f} VND) vào tài khoản!")
        current_account.deposit(amount)
        if current_account.__class__.__name__ == "HybridAccount":
            reward = current_account.cashback_reward(amount)
            current_account.deposit(reward)
        print(f"Số dư mới: {current_account.balance:,.0f} VND")

    if choice == "2":
        amount = float(input("Nhập số tiền cần rút: "))
        current_account.withdraw(amount)
        if current_account.__class__.__name__ in ["SavingsAccount", "HybridAccount"]:
            print("Rút tiền thành công!")
            print(f"Số tiền rút: {amount}")
            print(f"Phí phạt rút trước hạn (2%): {amount*0.02}")
        else:
            print("Rút tiền thành công! (Sử dụng hạn mức thấu chi)")
            print(f"Số tiền rút: {amount}")
        print(f"Số dư còn lại: {current_account.balance}")

def accumulate_balance(current_account):
    if current_account.__class__.__name__ not in ["SavingsAccount", "HybridAccount"]:
        print("Tính năng không hỗ trợ")
        return
    print("--- TÍNH LÃI ĐỊNH KỲ ---")
    print(f"Số dư trước tính lãi:{current_account.balance}")
    print(f"Lãi suất năm: {current_account.interest_rate*100}%")
    print(f"Tiền lãi nhận được: +{current_account.apply_interest():,.0f} VND")
    print(f"Số dư mới sau khi cộng lãi: {current_account.balance} VND")

def choose_account_b(accounts, current_account):
    position = 0
    for index, account in enumerate(accounts, 1):
        if account.account_number == current_account.account_number:
            print(f"{index}. {account.account_name} - {account.account_number} [Tài khoản hiện tại]")
            position = index
            continue
        print(f"{index}. {account.account_name} - {account.account_number}")
    choice = input("Chọn 1 trong các account trên (trừ account hiện tại)!")
    if int(choice) == position:
        print("Vui lòng chọn account khác hiện tại để so sánh!")
        return False
    return accounts[int(choice)-1]

def compare_account(accounts, current_account):
    print("--- ĐỒNG BỘ & SO SÁNH TÀI KHOẢN (OPERATOR OVERLOADING) ---") 
    print(f"Tài khoản hiện tại (A): {current_account.account_name} (Số dư: {current_account.balance:,.0f} VND)")
    other_account = choose_account_b(accounts, current_account)
    if not other_account:
        return
    print(f"Chọn tài khoản đối ứng (B) từ danh sách hệ thống: {other_account.account_number} ({other_account.account_name} - Số dư: {other_account.balance:,.0f} VND)") 
    if current_account < other_account:
        print(f"[Kết quả So sánh (__lt__)]: Số dư tài khoản A NHỎ HƠN số dư tài khoản B.")
    elif current_account == other_account:
        print(f"[Kết quả So sánh (__eq__)]: Số dư tài khoản A BẰNG số dư tài khoản B.")
    else:
        print(f"[Kết quả So sánh (__lt__)]: Số dư tài khoản A LỚN HƠN số dư tài khoản B.")
    total_balance = current_account + other_account
    print(f"[Kết quả Tổng hợp (__add__)]: Tổng số tiền sở hữu của cả 2 tài khoản là: {total_balance:,.0f} VND.")

def main():
    accounts = [SavingsAccount("0987462843","Kien",0.04),
                HybridAccount("0987462844","Kien1",0.04),
                CreditAccount("0987462845","Kien2",200000),
                SavingsAccount("0987462846","Kien3",0.04)]
    current_account = None 
    while True:
        choice = input("""===== VIETCOMBANK DIGIBANK PRO SIMULATOR =====
1. Mở tài khoản mới (Chọn loại tài khoản)
2. Xem thông tin & Kiểm tra thứ tự kế thừa (MRO)
3. Giao dịch Nạp / Rút tiền & Tính điểm thưởng (Đa hình)
4. Tích lũy / Áp dụng lãi suất định kỳ
5. Kiểm tra tính năng gộp tài khoản & So sánh (Overloading)
6. Thanh toán hóa đơn qua Cổng trung gian (Duck Typing)
7. Thoát chương trình
==============================================
Chọn chức năng (1-7): """)
        match choice:
            case "1":
                current_account = open_account(current_account,accounts)
            case "2":
                display_info(current_account)
            case "3":
                transaction(current_account)
            case "4":
                accumulate_balance(current_account)
            case "5":
                compare_account(accounts, current_account)
            case "6":
                pass
            case "7":
                print("Cảm ơn bạn đã sử dụng chương trình!")
                break
            case _:
                print("Lựa chọn không hợp lệ!")

if __name__ == "__main__":
    main()