
# Cấu trúc dự án Quản lý nhân viên

Dưới đây là sơ đồ cấu trúc thư mục của dự án cùng với giải thích chi tiết bằng tiếng Việt.

```
staff-management/
├── .gitignore                      # Các file và thư mục được Git bỏ qua
├── .idea/                          # Thư mục cài đặt của IDE (ví dụ: PyCharm)
└── src/                            # Thư mục chứa mã nguồn chính
    ├── __init__.py                 # Đánh dấu thư mục `src` là một Python package
    ├── main.py                     # Điểm khởi đầu của ứng dụng
    ├── employee/                   # Gói (package) chứa mọi thứ liên quan đến nhân viên
    │   ├── employee.py             # Định nghĩa lớp `Employee` cơ bản
    │   └── role/                   # Gói con chứa các vai trò (chức vụ) khác nhau
    │       ├── adminstrative.py    # Định nghĩa vai trò nhân viên hành chính
    │       ├── HOD.py              # Định nghĩa vai trò Trưởng phòng (Head of Department)
    │       └── sales.py            # Định nghĩa vai trò nhân viên kinh doanh
    └── menu/                       # Gói chứa các module liên quan đến giao diện người dùng
        ├── menu_logic.py           # Chứa logic xử lý các lựa chọn từ menu
        └── menu_ui.py              # Chứa code để hiển thị menu cho người dùng
```

## Ghi chú chi tiết

*   **`.gitignore`**: Rất quan trọng để không đưa các file không cần thiết (như file của IDE, file cache của Python) vào repository.
*   **`src/`**: Tách biệt mã nguồn khỏi các file cấu hình ở gốc dự án giúp cấu trúc rõ ràng hơn.
*   **`main.py`**: Là file bạn sẽ chạy để khởi động chương trình. Nó sẽ gọi các module khác.
*   **Gói `employee`**:
    *   Việc chia các vai trò (`role`) thành các file riêng biệt giúp dễ dàng quản lý và mở rộng. Nếu sau này có thêm chức vụ mới (ví dụ: `Technical.py`), bạn chỉ cần tạo file mới trong thư mục `role`.
*   **Gói `menu`**:
    *   Tách biệt `menu_ui.py` (giao diện) và `menu_logic.py` (xử lý) là một thực hành tốt. Nó giúp bạn có thể thay đổi giao diện mà không ảnh hưởng đến logic nghiệp vụ và ngược lại.
