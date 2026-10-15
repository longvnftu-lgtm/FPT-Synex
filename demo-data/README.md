# Dữ liệu demo Synnex FPT trên Base Sales (sales.base.com.vn)

Bộ dữ liệu demo cho 3 Use Case trong `synnex_fpt_value_chain_agentic_sales_os.md`: Account Care & Bán chéo, Pipeline Dự án B2G, Chăm sóc SME.
Toàn bộ tên công ty, người liên hệ, domain, số điện thoại, mã số thuế là **hư cấu** cho mục đích demo. Tên Hãng (Dell, HP, Cisco…) là thật.

## 1. Có gì trong thư mục

| File | Dùng để | Trạng thái |
|---|---|---|
| `Dữ liệu setup/CRM Sale/Account/Import - CRM Account Đại lý & Khách hàng Synnex FPT.xlsx` | Import **22 custom field** vào Account directory | ✅ Import được ngay |
| `Dữ liệu setup/CRM Sale/Pipeline/Import - CRM Pipeline Dự án B2G & Enterprise - Field.xlsx` | Import **16 custom field** vào pipeline Dự án | ✅ Import được sau khi tạo đúng tên stage |
| `Dữ liệu setup/CRM Sale/Pipeline/Import - CRM Pipeline Phát triển Đại lý & Bán chéo - Field.xlsx` | Import **12 custom field** vào pipeline Bán chéo | ✅ Import được sau khi tạo đúng tên stage |
| `Dữ liệu setup/CRM Sale/Bộ dữ liệu demo Synnex FPT (dữ liệu gốc).xlsx` | Xem và duyệt toàn bộ dữ liệu: 52 Account, 100 Contact, 18 Deal B2G, 12 Deal bán chéo, ma trận ngành hàng | 📖 Chỉ để đọc, **không import file này** |
| `personas.json` | Điền username Base thật cho 4 vai demo | ✍️ Bạn điền |
| `scripts/fill_template.py` | Đổ dữ liệu gốc vào **file mẫu record thật** xuất từ tenant | ⏳ Chạy sau khi có file mẫu |

## 2. Quy mô và câu chuyện cài sẵn

| Đối tượng | Số lượng | Ghi chú |
|---|---|---|
| Account Kênh Đại lý | 40 | 6 Key Account · 12 Gold · 22 SME (SME không có owner, để Agent chăm sóc) |
| Account Kênh Dự án | 12 | 4 cơ quan nhà nước · 5 Enterprise · 2 SI · 1 Telco |
| Contact | 100 | 1 (SME) – 3 (Key Account, Dự án) người / Account |
| Deal Dự án B2G | 18 · ~193,9 tỷ | 3 / 4 / 3 / 5 / 3 theo 5 stage |
| Deal Bán chéo | 12 · ~70,8 tỷ | 3 / 4 / 3 / 2 theo 4 stage, giá trị = cam kết 6 tháng |

Câu chuyện để mở trong buổi demo:
1. **Chuỗi Điện máy Sao Việt** (Key Account): mua Máy tính đều nhưng chưa mua Thiết bị mạng → deal "AI gợi ý từ dữ liệu PO".
2. **Ban QLDA Chuyển đổi số tỉnh Đông Hải – Trung tâm IOC 42 tỷ**: deal chủ lực, giá đặc biệt Dell "Đang chờ duyệt", để nằm quá ngưỡng rotting.
3. **Tin học Đức Trí** (SME): hỏi qua Zalo OA rồi thành cơ hội bán thêm Dell.
4. Phụ: **Tin học Minh Khang** công nợ 96% hạn mức; 3 SME có cảnh báo "Rủi ro sụt doanh số"; **Ngân hàng Sao Bắc Á** đang đàm phán HĐ 3 bên.

## 3. Trình tự dựng trên Base (không đảo thứ tự)

1. **Account directory**: `Settings → Accounts → + Create service`, tên `Đại lý & Khách hàng Synnex FPT`. Tạo Operation stages tối thiểu (ACTIVE: `Đang chăm sóc`).
2. **Import field Account**: `Setting → Custom fields → Import` → chọn file field Account.
3. **Tạo 2 pipeline**, đặt **đúng tên stage** (cột *Stages* trong file field tham chiếu theo tên):

   | Pipeline | Stage · Probability · Rotting (ngày) |
   |---|---|
   | `Dự án B2G & Enterprise` | Lead dự án 10%·5 → Khảo sát & Tư vấn 25%·10 → Đăng ký Deal Hãng 40%·7 → Báo giá & Hồ sơ thầu 60%·14 → Đàm phán HĐ 3 bên 85%·10 |
   | `Phát triển Đại lý & Bán chéo` | Phát hiện cơ hội 15%·5 → Tư vấn ngành hàng 35%·7 → Đại lý đặt thử 65%·10 → Đặt hàng định kỳ 90%·14 |

   Cả hai: tiền tệ mặc định **VND**, bật `Enforce same currency`. Nếu muốn deal IOC hiện cảnh báo trễ hạn trong buổi demo, import trước ít nhất 1 ngày hơn ngưỡng rotting, hoặc tạm hạ rotting của stage Báo giá xuống 1 ngày.
4. **Import field cho từng pipeline**: `Setting → Data fields → Import`.
5. **Reference data**: Lost reasons `Thua giá trong thầu` · `Hãng không bảo vệ dự án` · `Chủ đầu tư hoãn ngân sách` · `Đối tác SI chuyển nhà phân phối khác`; Won reasons `Được Hãng bảo vệ giá` · `Đáp ứng tiến độ giao hàng`.
6. **Xuất file mẫu record**: ở từng màn Accounts, Contacts, Deals (mỗi pipeline) → `Import → Download template`. Gửi các file này lại (4 file).
7. **Sinh file import record** (chạy lại script, ví dụ cho Account):
   ```
   python demo-data/scripts/fill_template.py --object accounts \
     --template "<file mẫu Account>.xlsx" --personas demo-data/personas.json \
     --output "demo-data/Dữ liệu setup/CRM Sale/Account/Import - CRM Account record.xlsx"
   ```
   `--object` lần lượt: `accounts` → `contacts` → `deals_b2g` → `deals_xsell`.
8. **Import record theo thứ tự Account → Contact → Deal**, rồi xuất lại để đối chiếu vài bản ghi (đặc biệt Deal value có thể bị về 0, custom field bị lệch cột).

## 4. Lưu ý đã biết

- Các skill import đi kèm ghi là dành cho **CRM Base 2.0**. Nếu tenant `sales.base.com.vn` là bản Sales mới (Base 3.0), cấu trúc 12 cột của file field có thể không khớp. Hãy thử import file field Account trước, nếu lỗi thì gửi ảnh màn hình hoặc file `Data fields → Export` để chỉnh lại.
- Field nhiều lựa chọn (`select-m`) đang ghép bằng dấu `;`. Nếu Base đọc sai, chạy lại với `--list-sep ","`.
- Import không đóng được deal Won/Lost. Muốn có số liệu thắng/thua trên báo cáo thì đóng tay 2–3 deal sau khi import.
- Không có field công thức (ví dụ % sử dụng hạn mức) vì công thức cần field key mà Base tự sinh. Tạo tay sau khi import nếu cần.
