
class Menu:
    def __init__(self):   
        # self.employee_service = EmployeeService() 
        # self.menu_handler = MenuHandler(self.employee_service)
        self.choices = {
            "1": {"text": "Nhập thông tin nhân viên", "action": None },
            "2": {"text": "Xuất danh sách nhân viên", "action": None },
            "3": {"text": "Tìm nhân viên theo ID", "action": None },
            "4": {"text": "Xóa nhân viên theo ID", "action": None },
            "5": {"text": "Cập nhật thông tin nhân viên", "action": None },
            "6": {"text": "Tìm nhân viên theo khoảng thu nhập", "action": None },
            "7": {"text": "Sắp xếp nhân viên theo Tên", "action":None },
            "8": {"text": "Sắp xếp nhân viên theo Thu nhập", "action": None },
            "9": {"text": "Hiển thị 5 nhân viên có thu nhập cao nhất", "action": None },
            "0": {"text": "Thoát chương trình", "action": self._exit_program },
        }

    def _display_menu(self):
        print("\n--- HỆ THỐNG QUẢN LÝ NHÂN VIÊN ---")
        for key, value in self.choices.items():
            print(f"[{key}]: {value['text']}")
        print("-----------------------------------")

    def run(self):
        while True:
            self._display_menu()
            choice = input("Vui lòng nhập lựa chọn của bạn: ")
            
            selected_choice = self.choices.get(choice)
            
            if selected_choice:
                action_function = selected_choice["action"]
                try:
                    action_function()
                except Exception as e:
                    print(f"Đã xảy ra lỗi trong quá trình thực thi: {e}")
            else:
                print("Lựa chọn không hợp lệ. Vui lòng thử lại.")

    def _exit_program(self):
        print("Cảm ơn bạn đã sử dụng chương trình. Tạm biệt!")
        exit()

menu = Menu()
menu.run()