class BankAccount:
    # Class attributes
    bank_name = "Vietcombank"
    transaction_fee = 2000

    def __init__(self, account_number, account_name):
        self.account_number = account_number

        # Private attribute (Name Mangling)
        self.__balance = 0

        self._account_name = ""
        self.account_name = account_name

    # Property chỉ cho phép đọc số dư
    @property
    def balance(self):
        return self.__balance

    # Property cho tên tài khoản
    @property
    def account_name(self):
        return self._account_name

    # Setter xử lý chuẩn hóa tên
    @account_name.setter
    def account_name(self, new_name):
        new_name = new_name.strip()

        if not new_name:
            print("Tên tài khoản không được để trống")
            return

        self._account_name = " ".join(new_name.split()).upper()

    # Static method kiểm tra số tài khoản
    @staticmethod
    def validate_account_number(account_number):
        return (
            account_number.isdigit()
            and len(account_number) == 10
        )

    # Class method cập nhật phí giao dịch
    @classmethod
    def update_transaction_fee(cls, new_fee):
        cls.transaction_fee = new_fee

    # Nạp tiền
    def deposit(self, amount):
        if amount <= 0:
            print("Số tiền giao dịch phải lớn hơn 0")
            return False

        self.__balance += amount
        return True

    # Rút tiền
    def withdraw(self, amount):
        if amount <= 0:
            print("Số tiền giao dịch phải lớn hơn 0")
            return False

        total_required = amount + BankAccount.transaction_fee

        if self.__balance < total_required:
            print(
                "Giao dịch thất bại. Số dư không đủ để thanh toán số tiền và phí giao dịch"
            )
            return False

        self.__balance -= total_required
        return True

    # Hiển thị thông tin
    def display_info(self):
        print("\n--- THÔNG TIN TÀI KHOẢN ---")
        print(f"Ngân hàng: {BankAccount.bank_name}")
        print(f"Số tài khoản: {self.account_number}")
        print(f"Tên chủ tài khoản: {self.account_name}")
        print(f"Số dư hiện tại: {self.balance:,} VND")
        print(
            f"Phí giao dịch: {BankAccount.transaction_fee:,} VND"
        )


def main():
    current_account = None

    while True:
        print("\n===== VIETCOMBANK DIGIBANK SIMULATOR =====")
        print("1. Mở tài khoản mới")
        print("2. Xem thông tin tài khoản")
        print("3. Giao dịch Nạp / Rút tiền")
        print("4. Cập nhật Tên chủ tài khoản")
        print("5. Đổi phí giao dịch hệ thống")
        print("6. Thoát chương trình")
        print("==========================================")

        choice = input("Chọn chức năng (1-6): ").strip()

        # Chức năng 1
        if choice == "1":
            print("\n--- MỞ TÀI KHOẢN MỚI ---")

            while True:
                account_number = input(
                    "Nhập số tài khoản 10 chữ số: "
                ).strip()

                if BankAccount.validate_account_number(
                    account_number
                ):
                    break

                print("Số tài khoản không hợp lệ!")
                print("Số tài khoản phải gồm đúng 10 chữ số.")

            account_name = input(
                "Nhập tên chủ tài khoản: "
            )

            current_account = BankAccount(
                account_number,
                account_name
            )

            print("Mở tài khoản thành công!")
            print(
                f"Số tài khoản: {current_account.account_number}"
            )
            print(
                f"Tên chủ tài khoản: {current_account.account_name}"
            )

        # Chức năng 2
        elif choice == "2":
            if current_account is None:
                print("Hệ thống chưa có thông tin tài khoản")
                print(
                    "Vui lòng mở tài khoản ở Chức năng 1 trước."
                )
            else:
                current_account.display_info()

        # Chức năng 3
        elif choice == "3":
            if current_account is None:
                print("Hệ thống chưa có thông tin tài khoản")
                print(
                    "Vui lòng mở tài khoản ở Chức năng 1 trước."
                )
                continue

            print("\n--- GIAO DỊCH NẠP / RÚT TIỀN ---")
            print("1. Nạp tiền")
            print("2. Rút tiền")

            transaction_choice = input(
                "Chọn loại giao dịch (1-2): "
            ).strip()

            try:
                amount = int(
                    input("Nhập số tiền giao dịch: ")
                )

                if transaction_choice == "1":
                    if current_account.deposit(amount):
                        print(
                            f"Nạp tiền thành công: +{amount:,} VND"
                        )
                        print(
                            f"Số dư mới: {current_account.balance:,} VND"
                        )

                elif transaction_choice == "2":
                    if current_account.withdraw(amount):
                        print(
                            f"Rút tiền thành công: -{amount:,} VND"
                        )
                        print(
                            f"Phí giao dịch: {BankAccount.transaction_fee:,} VND"
                        )
                        print(
                            f"Số dư mới: {current_account.balance:,} VND"
                        )
                    else:
                        print(
                            f"Số dư mới: {current_account.balance:,} VND"
                        )

                else:
                    print(
                        "Loại giao dịch không hợp lệ."
                    )

            except ValueError:
                print(
                    "Số tiền phải là số nguyên hợp lệ."
                )

        # Chức năng 4
        elif choice == "4":
            if current_account is None:
                print("Hệ thống chưa có thông tin tài khoản")
                print(
                    "Vui lòng mở tài khoản ở Chức năng 1 trước."
                )
                continue

            print(
                "\n--- CẬP NHẬT TÊN CHỦ TÀI KHOẢN ---"
            )

            new_name = input("Nhập tên mới: ")

            old_name = current_account.account_name

            current_account.account_name = new_name

            if current_account.account_name != old_name:
                print(
                    f"Cập nhật thành công. Tên mới: {current_account.account_name}"
                )

        # Chức năng 5
        elif choice == "5":
            print(
                "\n--- ĐỔI PHÍ GIAO DỊCH HỆ THỐNG ---"
            )

            print(
                f"Phí giao dịch hiện tại: {BankAccount.transaction_fee:,} VND"
            )

            try:
                new_fee = int(
                    input(
                        "Nhập phí giao dịch mới: "
                    )
                )

                if new_fee < 0:
                    print(
                        "Phí giao dịch không được âm"
                    )
                    print(
                        f"Phí giao dịch hiện tại vẫn là {BankAccount.transaction_fee:,} VND"
                    )
                else:
                    BankAccount.update_transaction_fee(
                        new_fee
                    )

                    print(
                        f"Đã cập nhật phí giao dịch toàn hệ thống thành {BankAccount.transaction_fee:,} VND"
                    )

            except ValueError:
                print(
                    "Phí giao dịch phải là số nguyên hợp lệ."
                )

        # Chức năng 6
        elif choice == "6":
            print(
                "Cảm ơn bạn đã sử dụng Vietcombank Digibank!"
            )
            break

        else:
            print(
                "Lựa chọn không hợp lệ. Vui lòng chọn từ 1 đến 6."
            )


if __name__ == "__main__":
    main()