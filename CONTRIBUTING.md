# Hướng dẫn Đóng góp (Contribution Guidelines)

Chào mừng bạn đến với dự án! Để đảm bảo mã nguồn được nhất quán, dễ đọc và dễ bảo trì, vui lòng tuân thủ các quy tắc dưới đây khi đóng góp.

---

## 1. Quy tắc về Ngôn ngữ

Đây là quy tắc quan trọng nhất của dự án.

#### **Mã nguồn (Code) → Tiếng Anh**
- **TOÀN BỘ** mã nguồn phải được viết bằng **Tiếng Anh**.
- Điều này bao gồm:
    - Tên biến, tên hàm, tên lớp (class).
    - Comment (bình luận) trong code.
    - Tên file.
    - Commit message.

#### **Giao diện Người dùng (UI) → Tiếng Việt**
- **TOÀN BỘ** các chuỗi (string) văn bản hiển thị cho người dùng cuối phải là **Tiếng Việt** có dấu.
- Điều này bao gồm:
    - Các mục trong menu.
    - Các câu thông báo (ví dụ: "Thêm nhân viên thành công.").
    - Các câu hỏi nhập liệu (ví dụ: "Vui lòng nhập tên nhân viên:").

#### **Ví dụ Minh họa**

```python
# ✅ TỐT
def get_employee_by_id(employee_id: int):
    """This function retrieves an employee from the database."""
    # Find the employee...
    if not employee:
        print("Không tìm thấy nhân viên.")
        return None
    return employee

# ❌ KHÔNG TỐT
def tim_nhan_vien_theo_id(id_nhan_vien: int):
    """Hàm này lấy nhân viên từ CSDL."""
    # ...
    if not employee:
        print("Employee not found.") # Sai ngôn ngữ UI
        return None
    return employee
```

## 2. Định dạng Mã nguồn (Code Style)

- **PEP 8**: Toàn bộ code Python phải tuân thủ theo tiêu chuẩn [PEP 8](https://peps.python.org/pep-0008/).
- **Linter**: Chúng tôi khuyến khích sử dụng các công cụ kiểm tra code (linter) như `Ruff` hoặc `Flake8` để tự động phát hiện và sửa lỗi định dạng trước khi commit.

## 3. Quy tắc Đặt tên (Naming Conventions)

- **Biến và Hàm (Variables, Functions)**: Dùng `snake_case` (ví dụ: `employee_list`, `calculate_total_salary`).
- **Lớp (Classes)**: Dùng `PascalCase` (ví dụ: `Employee`, `SalesManager`).
- **Hằng số (Constants)**: Dùng `UPPER_SNAKE_CASE` (ví dụ: `DEFAULT_TAX_RATE`).

## 4. Commit Message

- Viết commit message bằng **Tiếng Anh**.
- Nên sử dụng các tiền tố (prefix) để thể hiện rõ mục đích của commit. Ví dụ:
    - `feat:`: Thêm một tính năng mới (feature).
    - `fix:`: Sửa một lỗi (bug fix).
    - `docs:`: Cập nhật tài liệu (documentation).
    - `style:`: Sửa lỗi định dạng, không ảnh hưởng đến logic code.
    - `refactor:`: Tái cấu trúc code mà không thay đổi hành vi.
    - `test:`: Thêm hoặc sửa test.

**Ví dụ commit message:**
```
feat: Add function to calculate employee bonuses
```

## 5. Quy trình làm việc (Workflow)

1.  **Fork** repository.
2.  Tạo một **branch** mới cho tính năng hoặc bản sửa lỗi của bạn (`git checkout -b ten-feature-cua-ban`).
3.  Thực hiện các thay đổi và **commit**.
4.  Đẩy (push) branch của bạn lên fork.
5.  Tạo một **Pull Request** để nhóm review và sáp nhập.
