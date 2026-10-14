# HƯỚNG DẪN CHO AGENT TRÌNH DUYỆT — Dựng dữ liệu demo Synnex FPT trên Base Sales

> **Cách dùng:** Mở `https://sales.base.com.vn/` và đăng nhập bằng tài khoản demo (admin của tenant). Sau đó dán toàn bộ file này vào Claude in Chrome hoặc Gemini (Chrome), hoặc đính kèm file rồi gõ: *"Đọc file hướng dẫn và thực hiện từ Phần 0."*
> Phiên bản dữ liệu: 14/10/2026. Toàn bộ tên công ty, người, domain, số điện thoại là **hư cấu** cho mục đích demo. Tên Hãng (Dell, HP, Cisco…) là thật.

---

## PHẦN 0 — Vai trò và quy tắc bắt buộc (agent đọc trước)

Bạn là trợ lý dựng môi trường demo CRM cho buổi trình bày với **Synnex FPT**, nhà phân phối ICT có ~300 Sales: 70% doanh thu từ kênh Đại lý (~1.000 Account), 30% từ kênh Dự án B2G/Enterprise. Nhiệm vụ của bạn là cấu hình và nhập dữ liệu trên `sales.base.com.vn` theo đúng thứ tự trong file này.

**Quy tắc an toàn:**
1. **Không xoá, không sửa, không gộp** bất kỳ pipeline, directory, field hay bản ghi nào **đã có sẵn** trong tenant. Chỉ tạo mới. Nếu thấy một mục trùng tên đã tồn tại → dừng lại và hỏi người dùng.
2. **Không bấm Won/Lost, không gửi email, không gọi điện, không mời người dùng mới.** Không đổi cài đặt ngoài phạm vi các mục được liệt kê.
3. Tên menu, nút, trường trong app là **tiếng Anh**. Gõ dữ liệu **tiếng Việt có dấu**, đúng chính tả như bảng.
4. Ô tiền: **chỉ gõ chữ số**, không dấu chấm/phẩy, không ký hiệu. Tiền tệ luôn là **VND** (form Account mặc định USD — phải đổi).
5. Ngày nhập theo định dạng app yêu cầu; dữ liệu trong file viết `DD/MM/YYYY`.
6. **Tên stage phải gõ chính xác** như bảng (kể cả dấu `&`). Field và deal tham chiếu stage theo tên.
7. Gặp màn hình khác mô tả, nút không tồn tại, lỗi lưu, hoặc hộp thoại hỏi xác nhận nhạy cảm → **dừng, chụp/mô tả màn hình, hỏi người dùng**. Không đoán, không thử bừa.
8. Sau mỗi PHẦN, báo cáo ngắn: đã tạo gì, số lượng, mục nào lỗi/bỏ qua.

**Owner (người phụ trách):** dữ liệu dùng mã vai sau. Trước khi bắt đầu Phần 4, **hỏi người dùng** username Base tương ứng. Nếu người dùng trả lời "dùng tài khoản của tôi" → gán mọi owner là tài khoản đang đăng nhập.

| Mã vai | Vai trò | Username Base |
|---|---|---|
| SALES_BAC | Sales kênh Miền Bắc & Miền Trung | *(hỏi người dùng)* |
| SALES_NAM | Sales kênh Miền Nam | *(hỏi người dùng)* |
| SALES_DUAN | Sales dự án B2G & Enterprise | *(hỏi người dùng)* |
| TRUONG_KENH | Trưởng kênh Đại lý (quản lý) | *(hỏi người dùng)* |

Ô owner để trống trong bảng (đại lý SME) = **không gán owner** — đây là chủ ý: tệp SME chưa có Sales phụ trách, sẽ do AI Agent chăm sóc.

**Hai cách nhập dữ liệu — hỏi người dùng chọn trước Phần 4:**
- **Cách A — Import Excel (nhanh, đủ 52 Account / 100 Contact):** người dùng có file `Bộ dữ liệu demo Synnex FPT (dữ liệu gốc).xlsx` và các file import field. Agent chỉ hướng dẫn và kiểm tra; người dùng tự chọn file khi hộp thoại upload mở (agent không tự truy cập ổ đĩa).
- **Cách B — Nhập tay qua form (bộ lõi):** agent tự nhập 25 Account, 25 Contact và 30 Deal theo bảng ở Phần 4–6. Đủ để chạy cả 3 câu chuyện demo.

---

## PHẦN 1 — Account directory và Contact directory

1. Vào `Settings → Accounts → + Create service`.
   - `Account directory name`: **Đại lý & Khách hàng Synnex FPT**
   - `Description`: *Danh bạ đại lý kênh phân phối (Key Account, Gold, SME) và khách hàng dự án B2G/Enterprise của Synnex FPT.*
2. Mở `Setting` của directory vừa tạo → `Operation stages` → `Create stage`:
   - Bucket `ACTIVE / OPERATIONAL`: **Tiềm năng**, **Đang chăm sóc**, **Khách hàng chiến lược**
   - Bucket `CLOSED / LOST / FAILED`: **Ngừng hợp tác**
   - Bucket `DISCARDED / IGNORED / TRASHED`: **Không phù hợp**
3. Vào `Settings → Contacts → + Create service`.
   - `Contact directory name`: **Người liên hệ Synnex FPT**
   - `Description`: *Đầu mối mua hàng, kế toán công nợ, CNTT của đại lý và chủ đầu tư dự án.*
4. Trong `Setting → Segmentations` (System-wide) tạo segmentation **Phân hạng đại lý** với option: `Key Account`, `Gold`, `Silver`, `SME`.
5. `Labels & taggings`: tạo nhãn **Chiến lược** (`#dc2626`), **Bán chéo** (`#2563eb`), **Cần theo dõi công nợ** (`#f59e0b`).

## PHẦN 2 — Custom field cho Account

Mở `Setting` của directory **Đại lý & Khách hàng Synnex FPT** → `Custom fields`.
- **Cách A:** bấm `Import`, để người dùng chọn file `Import - CRM Account Đại lý & Khách hàng Synnex FPT.xlsx`.
- **Cách B:** bấm `New Field` → chọn `Internal Field`, tạo lần lượt (bật `ON FORMS` và `IN VIEWS`):

| # | Label | Type | Option (nếu là Dropdown/Multi-Select) |
|---|---|---|---|
| 1 | Mã đại lý | Text | |
| 2 | Loại tài khoản | Dropdown | Chuỗi bán lẻ; Đại lý bán lẻ; Nhà phân phối cấp 2; System Integrator; Telco · Service Provider; Cơ quan nhà nước; Doanh nghiệp Enterprise |
| 3 | Mảng kinh doanh | Dropdown | Kênh Đại lý; Kênh Dự án |
| 4 | Hạng đại lý | Dropdown | Key Account; Gold; Silver; SME |
| 5 | Khu vực | Dropdown | Miền Bắc; Miền Trung; Miền Nam |
| 6 | Ngành hàng đang mua | Multi-Select | Máy tính; Linh kiện & Ngoại vi; Thiết bị mạng; Smart Device; Phần mềm & Cloud; Giải pháp CNTT |
| 7 | Ngành hàng chưa khai thác | Multi-Select | (như trên) |
| 8 | Hạn mức tín dụng (VND) | Decimal | |
| 9 | Công nợ hiện tại (VND) | Decimal | |
| 10 | Doanh số 12 tháng (VND) | Decimal | |
| 11 | Tăng trưởng so cùng kỳ (%) | Decimal | |
| 12 | Sức khoẻ Account | Dropdown | Ổn định; Cần theo dõi; Rủi ro sụt doanh số |

*(File import của Cách A có thêm 10 field phụ: Tỉnh/Thành phố, Mã số thuế, Hãng đang phân phối, Doanh số tháng gần nhất, Tình trạng HĐ nguyên tắc, Ngày hết hạn HĐ nguyên tắc, Kỳ hạn thanh toán, Ngày thăm gần nhất, Tần suất thăm, Nhật ký thị sát gần nhất. Cách B có thể bỏ qua.)*

`AI Copilot` của directory → `+ Add rule`:
- Tiêu đề: **Sức khoẻ Account và cơ hội bán chéo đại lý**
- Nội dung: *Dựa trên hạng đại lý, doanh số 12 tháng, tăng trưởng so cùng kỳ, công nợ so với hạn mức, ngành hàng đang mua và chưa khai thác, ngày thăm gần nhất. Đánh giá mức gắn kết và rủi ro sụt doanh số. Chỉ ra tối đa 2 ngành hàng nên bán chéo kèm lý do. Cảnh báo nếu công nợ vượt 90% hạn mức hoặc quá 30 ngày chưa có tương tác. Không tự hứa chiết khấu, không bịa số liệu. Đề xuất tối đa 3 hành động kèm người phụ trách và hạn.*

## PHẦN 3 — Hai pipeline

### 3.1 Pipeline "Dự án B2G & Enterprise"
`Settings → Pipelines → + Create pipeline`, tên **Dự án B2G & Enterprise**, sửa bộ stage ngay trên màn tạo:

| Stage | Probability | Rotting in (days) |
|---|---|---|
| Lead dự án | 10 | 5 |
| Khảo sát & Tư vấn | 25 | 10 |
| Đăng ký Deal Hãng | 40 | 7 |
| Báo giá & Hồ sơ thầu | 60 | 1 *(cố ý để 1 ngày để deal chủ lực hiện cảnh báo trễ trong buổi demo; sau demo đổi lại 14)* |
| Đàm phán HĐ 3 bên | 85 | 10 |

`Setting → General info`:
- `Description`: *Quản lý cơ hội dự án hạ tầng CNTT cho cơ quan nhà nước và doanh nghiệp lớn: từ khảo sát, đăng ký bảo vệ dự án với Hãng, báo giá – hồ sơ thầu đến ký hợp đồng 3 bên cùng đơn vị SI.*
- `Set pipeline default currency` = **VND — Vietnamese Dong**, bật `Enforce same currency`.

`Setting → Data fields` → Cách A: `Import` file `Import - CRM Pipeline Dự án B2G & Enterprise - Field.xlsx`. Cách B: tạo `Internal Field`:

| # | Label | Type | Option |
|---|---|---|---|
| 1 | Hãng chính | Dropdown | Dell; HP; Lenovo; Cisco; Microsoft; Intel; Apple |
| 2 | Đơn vị SI / đối tác triển khai | Text | |
| 3 | Nguồn vốn | Dropdown | Ngân sách nhà nước; Vốn doanh nghiệp; ODA · Vốn vay; Xã hội hoá |
| 4 | Tình trạng bảo vệ dự án | Dropdown | Chưa đăng ký; Đang chờ Hãng duyệt; Đã được bảo vệ; Bị từ chối |
| 5 | Giá đặc biệt | Dropdown | Chưa xin; Đang chờ duyệt; Đã duyệt; Bị trả lại |
| 6 | Bước tiếp theo | Text | |
| 7 | Người quyết định và quy trình phê duyệt | Long Text | |

`System fields`: `Primary Account` → `REQUIRED AFTER STAGE` = **Lead dự án**.

`Won reasons`: **Được Hãng bảo vệ giá** · **Đáp ứng tiến độ giao hàng**.
`Lost reasons`: **Thua giá trong thầu** · **Hãng không bảo vệ dự án** · **Chủ đầu tư hoãn ngân sách** · **Đối tác SI chuyển nhà phân phối khác**.

`AI Copilot → + Add rule`:
- Tiêu đề: **Kiểm soát deal dự án B2G và HĐ 3 bên**
- Nội dung: *Dựa trên dữ liệu deal, xác định chủ đầu tư, đơn vị SI, Hãng đã bảo vệ dự án hay chưa, hình thức lựa chọn nhà thầu, ngày mở thầu, giá trị và biên lợi nhuận. Ở giai đoạn Báo giá & Hồ sơ thầu phải có giá đặc biệt đã duyệt; ở Đàm phán HĐ 3 bên phải có đủ 3 bên và điều khoản thanh toán. Nêu rõ thông tin đã có và còn thiếu, không tự bịa giá, chiết khấu hay cam kết của Hãng. Đề xuất tối đa 3 hành động kèm người phụ trách và hạn. Cảnh báo deal quá ngưỡng rotting, thiếu người quyết định, hoặc ngày mở thầu đã qua mà chưa cập nhật kết quả.*

### 3.2 Pipeline "Phát triển Đại lý & Bán chéo"

| Stage | Probability | Rotting in (days) |
|---|---|---|
| Phát hiện cơ hội | 15 | 5 |
| Tư vấn ngành hàng | 35 | 7 |
| Đại lý đặt thử | 65 | 10 |
| Đặt hàng định kỳ | 90 | 14 |

- `Description`: *Cơ hội tăng doanh số trên tệp đại lý hiện hữu: bán chéo ngành hàng chưa mua, bán thêm sản lượng, kích hoạt lại đại lý. Nguồn cơ hội từ AI phân tích dữ liệu PO, Sales đi thị sát và hội thoại Zalo OA.*
- Tiền tệ **VND**, bật `Enforce same currency`.
- Data fields: Cách A import file `Import - CRM Pipeline Phát triển Đại lý & Bán chéo - Field.xlsx`. Cách B tạo:

| # | Label | Type | Option |
|---|---|---|---|
| 1 | Nguồn cơ hội | Dropdown | AI gợi ý từ dữ liệu PO; Sales phát hiện khi thăm; Đại lý hỏi qua Zalo OA; Chương trình của Hãng |
| 2 | Ngành hàng mục tiêu | Dropdown | Máy tính; Linh kiện & Ngoại vi; Thiết bị mạng; Smart Device; Phần mềm & Cloud; Giải pháp CNTT |
| 3 | Hãng mục tiêu | Dropdown | Dell; HP; Lenovo; Cisco; Intel; Microsoft; Apple; Xiaomi |
| 4 | Sản lượng dự kiến/tháng (VND) | Decimal | |
| 5 | Bước tiếp theo | Text | |

- Won reasons: **Đại lý đạt sản lượng cam kết** · **Chính sách Hãng hấp dẫn**. Lost reasons: **Đại lý thiếu vốn nhập hàng** · **Không có nhân sự bán ngành hàng mới** · **Đối thủ chiết khấu cao hơn**.

**Kiểm tra trước khi sang Phần 4:** kanban 2 pipeline hiển thị đúng 5 và 4 stage, tên khớp 100%.

---

## PHẦN 4 — Account (25 bản ghi lõi)

`Accounts → + Add account`. Với mỗi dòng: `Account name`, `Domain`, `Account service` = **Đại lý & Khách hàng Synnex FPT** + stage **Đang chăm sóc** (khách dự án: **Tiềm năng**), `Estimated lifetime value` = Doanh số 12 tháng (đổi tiền tệ sang **VND**; khách dự án để trống), `Account owner`, `Address` (gõ tỉnh/thành, chọn gợi ý đầu tiên). Sau khi tạo, mở account và điền custom field.

Gắn nhãn: Key Account → **Chiến lược**; "Tin học Minh Khang" → **Cần theo dõi công nợ**.

| # | Account name | Domain | Account owner | Address | Mã đại lý | Loại tài khoản | Mảng kinh doanh | Hạng đại lý | Khu vực | Ngành hàng đang mua | Ngành hàng chưa khai thác | Hạn mức tín dụng (VND) | Công nợ hiện tại (VND) | Doanh số 12 tháng (VND) | Tăng trưởng so cùng kỳ (%) | Sức khoẻ Account |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Chuỗi Điện máy Sao Việt | saovietmart.vn | SALES_NAM | TP. Hồ Chí Minh | SFD-N0001 | Chuỗi bán lẻ | Kênh Đại lý | Key Account | Miền Nam | Máy tính; Smart Device; Linh kiện & Ngoại vi | Thiết bị mạng; Phần mềm & Cloud; Giải pháp CNTT | 27000000000 | 18783000000 | 276427000000 | 13.8 | Ổn định |
| 2 | Hệ thống Bán lẻ Công nghệ Nhật Minh | nhatminhtech.vn | SALES_BAC | Hà Nội | SFD-B0002 | Chuỗi bán lẻ | Kênh Đại lý | Key Account | Miền Bắc | Máy tính; Smart Device; Linh kiện & Ngoại vi; Thiết bị mạng | Phần mềm & Cloud; Giải pháp CNTT | 53500000000 | 35700000000 | 96184000000 | 17.5 | Ổn định |
| 3 | Chuỗi Laptop An Phát Digital | anphatdigital.vn | SALES_BAC | Hà Nội | SFD-B0003 | Chuỗi bán lẻ | Kênh Đại lý | Key Account | Miền Bắc | Máy tính; Linh kiện & Ngoại vi | Thiết bị mạng; Smart Device; Phần mềm & Cloud; Giải pháp CNTT | 54000000000 | 20068000000 | 106390000000 | 2.1 | Ổn định |
| 4 | Siêu thị Điện tử Hoàng Long | hoanglongdientu.vn | SALES_BAC | Đà Nẵng | SFD-T0004 | Chuỗi bán lẻ | Kênh Đại lý | Key Account | Miền Trung | Máy tính; Smart Device | Linh kiện & Ngoại vi; Thiết bị mạng; Phần mềm & Cloud; Giải pháp CNTT | 20000000000 | 15941000000 | 220131000000 | 1.9 | Ổn định |
| 5 | Chuỗi Di động Thế Hệ Mới | thehemoi.vn | SALES_NAM | TP. Hồ Chí Minh | SFD-N0005 | Chuỗi bán lẻ | Kênh Đại lý | Key Account | Miền Nam | Smart Device; Linh kiện & Ngoại vi | Máy tính; Thiết bị mạng; Phần mềm & Cloud; Giải pháp CNTT | 53500000000 | 22743000000 | 137686000000 | 8.2 | Ổn định |
| 6 | Tin học Minh Khang | minhkhangcomputer.vn | SALES_NAM | Cần Thơ | SFD-N0007 | Đại lý bán lẻ | Kênh Đại lý | Gold | Miền Nam | Máy tính; Linh kiện & Ngoại vi | Thiết bị mạng; Smart Device; Phần mềm & Cloud; Giải pháp CNTT | 8500000000 | 8160000000 | 19305000000 | 13.6 | Cần theo dõi |
| 7 | Công ty TNHH Tin học Thành Đạt | thanhdatvinh.vn | SALES_BAC | Nghệ An | SFD-T0009 | Đại lý bán lẻ | Kênh Đại lý | Gold | Miền Trung | Máy tính; Smart Device | Linh kiện & Ngoại vi; Thiết bị mạng; Phần mềm & Cloud; Giải pháp CNTT | 6000000000 | 2298000000 | 19776000000 | 8.2 | Ổn định |
| 8 | Tin học Ngọc Thịnh | ngocthinhpc.vn | SALES_NAM | Đồng Nai | SFD-N0010 | Đại lý bán lẻ | Kênh Đại lý | Gold | Miền Nam | Máy tính; Linh kiện & Ngoại vi | Thiết bị mạng; Smart Device; Phần mềm & Cloud; Giải pháp CNTT | 5500000000 | 2106000000 | 43393000000 | 9.8 | Ổn định |
| 9 | Máy tính Trường Sơn | truongsonhue.vn | SALES_BAC | Thừa Thiên Huế | SFD-T0012 | Đại lý bán lẻ | Kênh Đại lý | Gold | Miền Trung | Máy tính; Linh kiện & Ngoại vi | Thiết bị mạng; Smart Device; Phần mềm & Cloud; Giải pháp CNTT | 3500000000 | 1919000000 | 30325000000 | 7.3 | Ổn định |
| 10 | Tin học Hải Âu | haiaunhatrang.vn | SALES_BAC | Khánh Hòa | SFD-T0013 | Đại lý bán lẻ | Kênh Đại lý | Gold | Miền Trung | Máy tính; Smart Device | Linh kiện & Ngoại vi; Thiết bị mạng; Phần mềm & Cloud; Giải pháp CNTT | 4000000000 | 1813000000 | 41551000000 | -2.8 | Ổn định |
| 11 | Laptop Tâm An | laptoptaman.vn | SALES_BAC | Hà Nội | SFD-B0015 | Đại lý bán lẻ | Kênh Đại lý | Gold | Miền Bắc | Máy tính; Linh kiện & Ngoại vi | Thiết bị mạng; Smart Device; Phần mềm & Cloud; Giải pháp CNTT | 6000000000 | 2483000000 | 33893000000 | 7.4 | Ổn định |
| 12 | Vi tính Bảo An |  |  | Vĩnh Long | SFD-N0022 | Đại lý bán lẻ | Kênh Đại lý | SME | Miền Nam | Máy tính | Linh kiện & Ngoại vi; Thiết bị mạng; Smart Device; Phần mềm & Cloud; Giải pháp CNTT | 1000000000 | 472000000 | 1842000000 | -25.7 | Rủi ro sụt doanh số |
| 13 | Tin học Đức Trí |  |  | Đắk Lắk | SFD-T0023 | Đại lý bán lẻ | Kênh Đại lý | SME | Miền Trung | Máy tính; Smart Device | Linh kiện & Ngoại vi; Thiết bị mạng; Phần mềm & Cloud; Giải pháp CNTT | 1000000000 | 404000000 | 3615000000 | 12.5 | Ổn định |
| 14 | Tin học Ánh Dương |  |  | Quảng Ngãi | SFD-T0025 | Đại lý bán lẻ | Kênh Đại lý | SME | Miền Trung | Máy tính | Linh kiện & Ngoại vi; Thiết bị mạng; Smart Device; Phần mềm & Cloud; Giải pháp CNTT | 1000000000 | 700000000 | 3138000000 | -22.5 | Rủi ro sụt doanh số |
| 15 | Máy tính Hồng Phát |  |  | Bắc Giang | SFD-B0036 | Đại lý bán lẻ | Kênh Đại lý | SME | Miền Bắc | Máy tính; Smart Device | Linh kiện & Ngoại vi; Thiết bị mạng; Phần mềm & Cloud; Giải pháp CNTT | 1000000000 | 531000000 | 5927000000 | -35.8 | Rủi ro sụt doanh số |
| 16 | Ban QLDA Chuyển đổi số tỉnh Đông Hải | cds.donghai.gov.vn | SALES_DUAN | Tỉnh Đông Hải | SFP-0041 | Cơ quan nhà nước | Kênh Dự án |  | Miền Trung |  |  |  |  |  |  | Ổn định |
| 17 | Sở Y tế tỉnh Đông Hải | syt.donghai.gov.vn | SALES_DUAN | Tỉnh Đông Hải | SFP-0042 | Cơ quan nhà nước | Kênh Dự án |  | Miền Trung |  |  |  |  |  |  | Ổn định |
| 18 | Cục Thống kê tỉnh Bắc Sơn | thongke.bacson.gov.vn | SALES_DUAN | Tỉnh Bắc Sơn | SFP-0043 | Cơ quan nhà nước | Kênh Dự án |  | Miền Bắc |  |  |  |  |  |  | Ổn định |
| 19 | Đại học Kỹ thuật Hồng Lam | hlut.edu.vn | SALES_DUAN | Hà Nội | SFP-0044 | Cơ quan nhà nước | Kênh Dự án |  | Miền Bắc |  |  |  |  |  |  | Ổn định |
| 20 | Tổng Công ty Cảng biển Đông Hải | donghaiport.vn | SALES_DUAN | Tỉnh Đông Hải | SFP-0045 | Doanh nghiệp Enterprise | Kênh Dự án |  | Miền Trung |  |  |  |  |  |  | Ổn định |
| 21 | Bệnh viện Đa khoa Quốc tế Tâm Đức | tamduchospital.vn | SALES_DUAN | TP. Hồ Chí Minh | SFP-0046 | Doanh nghiệp Enterprise | Kênh Dự án |  | Miền Nam |  |  |  |  |  |  | Ổn định |
| 22 | Ngân hàng TMCP Sao Bắc Á | saobaca.bank.vn | SALES_DUAN | Hà Nội | SFP-0047 | Doanh nghiệp Enterprise | Kênh Dự án |  | Miền Bắc |  |  |  |  |  |  | Ổn định |
| 23 | Tập đoàn Bảo hiểm An Bình Thịnh | abtinsurance.vn | SALES_DUAN | TP. Hồ Chí Minh | SFP-0048 | Doanh nghiệp Enterprise | Kênh Dự án |  | Miền Nam |  |  |  |  |  |  | Ổn định |
| 24 | Công ty CP Logistics Đông Dương | dongduonglogistics.vn | SALES_DUAN | TP. Hồ Chí Minh | SFP-0049 | Doanh nghiệp Enterprise | Kênh Dự án |  | Miền Nam |  |  |  |  |  |  | Ổn định |
| 25 | Sao Mai Telecom | saomaitelecom.vn | SALES_DUAN | Hà Nội | SFP-0052 | Telco · Service Provider | Kênh Dự án |  | Miền Bắc |  |  |  |  |  |  | Ổn định |

## PHẦN 5 — Contact (1 đầu mối chính / Account)

`Contacts → + Add contact`: Name, Title, Account (chọn account đã tạo), Email, Phone, Owner = owner của account.

| # | Contact name | Title | Account | Email | Phone |
|---|---|---|---|---|---|
| 1 | Ngô Quốc Quân | Giám đốc ngành hàng | Chuỗi Điện máy Sao Việt | quan.nq@saovietmart.vn | 0837112104 |
| 2 | Đặng Đức Phong | Giám đốc ngành hàng | Hệ thống Bán lẻ Công nghệ Nhật Minh | phong.đđ@nhatminhtech.vn | 0850471261 |
| 3 | Vũ Ngọc Hà | Giám đốc ngành hàng | Chuỗi Laptop An Phát Digital | ha.vn@anphatdigital.vn | 0916192494 |
| 4 | Phạm Thu Vy | Giám đốc ngành hàng | Siêu thị Điện tử Hoàng Long | vy.pt@hoanglongdientu.vn | 0906086252 |
| 5 | Bùi Quốc Long | Giám đốc ngành hàng | Chuỗi Di động Thế Hệ Mới | long.bq@thehemoi.vn | 0988588283 |
| 6 | Dương Hoàng Hà | Giám đốc | Tin học Minh Khang | ha.dh@minhkhangcomputer.vn | 0964588717 |
| 7 | Lý Ngọc Hùng | Giám đốc | Công ty TNHH Tin học Thành Đạt | hung.ln@thanhdatvinh.vn | 0859349550 |
| 8 | Lê Thu Hương | Giám đốc | Tin học Ngọc Thịnh | huong.lt@ngocthinhpc.vn | 0915069312 |
| 9 | Phạm Bảo Sơn | Giám đốc | Máy tính Trường Sơn | son.pb@truongsonhue.vn | 0916175391 |
| 10 | Hoàng Đức Khoa | Giám đốc | Tin học Hải Âu | khoa.hđ@haiaunhatrang.vn | 0900709148 |
| 11 | Trần Thị Đạt | Giám đốc | Laptop Tâm An | đat.tt@laptoptaman.vn | 0932825184 |
| 12 | Đặng Hải Thảo | Giám đốc | Vi tính Bảo An | thao.đh61@gmail.com | 0965848787 |
| 13 | Lý Thu Yến | Giám đốc | Tin học Đức Trí | yen.lt41@gmail.com | 0930515422 |
| 14 | Đặng Hoàng Tuấn | Giám đốc | Tin học Ánh Dương | tuan.đh27@gmail.com | 0970589661 |
| 15 | Nguyễn Hải Hương | Giám đốc | Máy tính Hồng Phát | huong.nh63@gmail.com | 0982684170 |
| 16 | Đỗ Hoàng Phong | Giám đốc kinh doanh | Ban QLDA Chuyển đổi số tỉnh Đông Hải | phong.đh@cds.donghai.gov.vn | 0984840452 |
| 17 | Đỗ Minh Lan | Trưởng ban QLDA | Sở Y tế tỉnh Đông Hải | lan.đm@syt.donghai.gov.vn | 0937203177 |
| 18 | Nguyễn Thanh Mai | Trưởng ban QLDA | Cục Thống kê tỉnh Bắc Sơn | mai.nt@thongke.bacson.gov.vn | 0915630021 |
| 19 | Bùi Thu Dũng | Giám đốc kinh doanh | Đại học Kỹ thuật Hồng Lam | dung.bt@hlut.edu.vn | 0911407270 |
| 20 | Trần Thị Hùng | Phó Giám đốc phụ trách CNTT | Tổng Công ty Cảng biển Đông Hải | hung.tt@donghaiport.vn | 0839525682 |
| 21 | Trần Thu Tuấn | Giám đốc kinh doanh | Bệnh viện Đa khoa Quốc tế Tâm Đức | tuan.tt@tamduchospital.vn | 0989628921 |
| 22 | Trần Ngọc Quân | Phó Giám đốc phụ trách CNTT | Ngân hàng TMCP Sao Bắc Á | quan.tn@saobaca.bank.vn | 0910150031 |
| 23 | Bùi Bảo Linh | Phó Giám đốc phụ trách CNTT | Tập đoàn Bảo hiểm An Bình Thịnh | linh.bb@abtinsurance.vn | 0986848745 |
| 24 | Bùi Thanh Nam | Phó Giám đốc phụ trách CNTT | Công ty CP Logistics Đông Dương | nam.bt@dongduonglogistics.vn | 0972075303 |
| 25 | Bùi Ngọc Đạt | Chuyên viên mua sắm | Sao Mai Telecom | đat.bn@saomaitelecom.vn | 0933463629 |

## PHẦN 6 — Deal

**Chỉ tạo khi Phần 4 và 5 đã xong** (deal tham chiếu account/contact đã tồn tại). Mở đúng pipeline → `+ Add deal` (hoặc kéo deal sang đúng stage sau khi tạo). Điền `Name`, `Value` (VND), `Primary account`, `Primary contact`, `Deal owner`, `Stage`, `Expected close date`, rồi các custom field. Nội dung cột *Overview* → ghi vào phần mô tả/Overview của deal.

### 6.1 Pipeline "Dự án B2G & Enterprise" — Deal owner: SALES_DUAN

| # | Deal name | Stage | Deal value | Account | Contact | Expected close date | Hãng chính | Đơn vị SI / đối tác triển khai | Nguồn vốn | Tình trạng bảo vệ dự án | Giá đặc biệt | Bước tiếp theo | Overview |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Cục Thống kê tỉnh Bắc Sơn – Máy trạm điều tra viên 120 bộ | Lead dự án | 2400000000 | Cục Thống kê tỉnh Bắc Sơn | Nguyễn Thanh Mai | 13/03/2027 | HP |  | Ngân sách nhà nước |  |  | Hẹn buổi khảo sát hiện trạng với phòng CNTT | Cục cần thay máy trạm cho đợt tổng điều tra 2027, đang lập dự toán. |
| 2 | Sao Mai Telecom – Switch truy nhập 300 trạm | Lead dự án | 6800000000 | Sao Mai Telecom | Bùi Ngọc Đạt | 02/04/2027 | Cisco |  | Vốn doanh nghiệp |  |  | Hẹn buổi khảo sát hiện trạng với phòng CNTT | Nhà mạng mở rộng hạ tầng FTTH khu vực phía Bắc, mới gửi RFI. |
| 3 | Tập đoàn Bảo hiểm An Bình Thịnh – Bản quyền Microsoft 365 1.500 user | Lead dự án | 9500000000 | Tập đoàn Bảo hiểm An Bình Thịnh | Bùi Bảo Linh | 11/02/2027 | Microsoft |  | Vốn doanh nghiệp |  |  | Hẹn buổi khảo sát hiện trạng với phòng CNTT | Gia hạn và mở rộng bản quyền, khách đang so sánh EA và CSP. |
| 4 | Đại học Kỹ thuật Hồng Lam – Phòng lab AI 60 máy trạm GPU | Khảo sát & Tư vấn | 11200000000 | Đại học Kỹ thuật Hồng Lam | Bùi Thu Dũng | 23/03/2027 | Dell | Công ty CP Giải pháp Tích hợp Thăng Long Tech | Ngân sách nhà nước |  |  | Gửi đề xuất cấu hình và dự toán sơ bộ | Đã khảo sát hiện trạng phòng lab, chờ khoa CNTT chốt cấu hình GPU. |
| 5 | Bệnh viện Đa khoa Quốc tế Tâm Đức – Hạ tầng máy chủ HIS/PACS | Khảo sát & Tư vấn | 14600000000 | Bệnh viện Đa khoa Quốc tế Tâm Đức | Trần Thu Tuấn | 01/02/2027 | HP | Công ty TNHH Hệ thống Số Hưng Việt | Vốn doanh nghiệp |  |  | Gửi đề xuất cấu hình và dự toán sơ bộ | Bệnh viện nâng cấp hệ thống PACS, cần lưu trữ 400TB, SI Hưng Việt dẫn dắt. |
| 6 | Công ty CP Logistics Đông Dương – Wifi kho bãi 5 trung tâm | Khảo sát & Tư vấn | 3900000000 | Công ty CP Logistics Đông Dương | Bùi Thanh Nam | 12/01/2027 | Cisco |  | Vốn doanh nghiệp |  |  | Gửi đề xuất cấu hình và dự toán sơ bộ | Khảo sát 2/5 kho, cần phủ sóng cho máy quét mã vạch cầm tay. |
| 7 | Sở Y tế tỉnh Đông Hải – Máy tính trạm y tế xã 220 bộ | Khảo sát & Tư vấn | 4400000000 | Sở Y tế tỉnh Đông Hải | Đỗ Minh Lan | 02/05/2027 | Lenovo | Công ty CP Giải pháp Tích hợp Thăng Long Tech | Ngân sách nhà nước |  |  | Gửi đề xuất cấu hình và dự toán sơ bộ | Thuộc đề án y tế số cơ sở, đang chờ phê duyệt chủ trương đầu tư. |
| 8 | Ngân hàng TMCP Sao Bắc Á – Máy chủ & SAN cho DR site | Đăng ký Deal Hãng | 28500000000 | Ngân hàng TMCP Sao Bắc Á | Trần Ngọc Quân | 17/01/2027 | Dell | Công ty CP Giải pháp Tích hợp Thăng Long Tech | Vốn doanh nghiệp | Đã được bảo vệ |  | Theo dõi phản hồi bảo vệ giá từ Hãng | Dự án trung tâm dữ liệu dự phòng, đã nộp đăng ký deal với Dell, chờ phản hồi bảo vệ giá. |
| 9 | Tổng Công ty Cảng biển Đông Hải – Firewall & SOC cảng | Đăng ký Deal Hãng | 7200000000 | Tổng Công ty Cảng biển Đông Hải | Trần Thị Hùng | 02/01/2027 | Cisco | Công ty TNHH Hệ thống Số Hưng Việt | Vốn doanh nghiệp | Đang chờ Hãng duyệt |  | Theo dõi phản hồi bảo vệ giá từ Hãng | Cisco đã bảo vệ dự án cho Synnex FPT qua SI Hưng Việt. |
| 10 | Tập đoàn Bảo hiểm An Bình Thịnh – Laptop cho đại lý bảo hiểm 800 máy | Đăng ký Deal Hãng | 15600000000 | Tập đoàn Bảo hiểm An Bình Thịnh | Bùi Bảo Linh | 23/12/2026 | Lenovo |  | Vốn doanh nghiệp | Đang chờ Hãng duyệt |  | Theo dõi phản hồi bảo vệ giá từ Hãng | Đối thủ cũng đăng ký deal, Lenovo đang xét theo thứ tự nộp. |
| 11 | Ban QLDA Chuyển đổi số tỉnh Đông Hải – Trung tâm IOC tỉnh giai đoạn 2 | Báo giá & Hồ sơ thầu | 42000000000 | Ban QLDA Chuyển đổi số tỉnh Đông Hải | Đỗ Hoàng Phong | 13/12/2026 | Dell | Công ty CP Giải pháp Tích hợp Thăng Long Tech | Ngân sách nhà nước | Đã được bảo vệ | Đang chờ duyệt | Hoàn thiện hồ sơ năng lực và bảo lãnh dự thầu | DEAL CHỦ LỰC: hồ sơ thầu đã phát hành, giá đặc biệt Dell chưa duyệt xong — đang nằm quá SLA. |
| 12 | Đại học Kỹ thuật Hồng Lam – Hạ tầng mạng ký túc xá | Báo giá & Hồ sơ thầu | 5300000000 | Đại học Kỹ thuật Hồng Lam | Bùi Thu Dũng | 28/11/2026 | Cisco |  | Ngân sách nhà nước | Đã được bảo vệ | Đã duyệt | Hoàn thiện hồ sơ năng lực và bảo lãnh dự thầu | Đã nộp báo giá, chờ hội đồng chấm. |
| 13 | Sở Y tế tỉnh Đông Hải – Máy chủ bệnh án điện tử tuyến tỉnh | Báo giá & Hồ sơ thầu | 9800000000 | Sở Y tế tỉnh Đông Hải | Đỗ Minh Lan | 08/12/2026 | HP | Công ty TNHH Hệ thống Số Hưng Việt | Ngân sách nhà nước | Đã được bảo vệ | Đã duyệt | Hoàn thiện hồ sơ năng lực và bảo lãnh dự thầu | Hồ sơ mời thầu yêu cầu bảo hành 5 năm tại chỗ, cần xác nhận với HP. |
| 14 | Công ty CP Logistics Đông Dương – Thiết bị cầm tay & máy in nhãn | Báo giá & Hồ sơ thầu | 2100000000 | Công ty CP Logistics Đông Dương | Bùi Thanh Nam | 18/11/2026 | HP |  | Vốn doanh nghiệp | Đã được bảo vệ | Đã duyệt | Hoàn thiện hồ sơ năng lực và bảo lãnh dự thầu | Khách yêu cầu giao theo 3 đợt, thanh toán Net 45. |
| 15 | Bệnh viện Đa khoa Quốc tế Tâm Đức – Máy tính phòng khám 150 bộ | Báo giá & Hồ sơ thầu | 3600000000 | Bệnh viện Đa khoa Quốc tế Tâm Đức | Trần Thu Tuấn | 23/11/2026 | Dell |  | Vốn doanh nghiệp | Đã được bảo vệ | Đã duyệt | Hoàn thiện hồ sơ năng lực và bảo lãnh dự thầu | Đã gửi báo giá lần 2 sau khi khách xin giảm 3%. |
| 16 | Ngân hàng TMCP Sao Bắc Á – Máy tính giao dịch viên 600 bộ | Đàm phán HĐ 3 bên | 13400000000 | Ngân hàng TMCP Sao Bắc Á | Trần Ngọc Quân | 03/11/2026 | HP | Công ty CP Giải pháp Tích hợp Thăng Long Tech | Vốn doanh nghiệp | Đã được bảo vệ | Đã duyệt | Chốt điều khoản thanh toán với SI và chủ đầu tư | DEAL CHỦ LỰC: đang chốt điều khoản HĐ 3 bên Ngân hàng – Thăng Long Tech – Synnex FPT. |
| 17 | Tổng Công ty Cảng biển Đông Hải – Máy chủ hệ thống điều hành cảng | Đàm phán HĐ 3 bên | 8700000000 | Tổng Công ty Cảng biển Đông Hải | Trần Thị Hùng | 08/11/2026 | Dell | Công ty TNHH Hệ thống Số Hưng Việt | Vốn doanh nghiệp | Đã được bảo vệ | Đã duyệt | Chốt điều khoản thanh toán với SI và chủ đầu tư | Đã trúng chào hàng, đang thương thảo tiến độ thanh toán. |
| 18 | Sao Mai Telecom – Bản quyền ảo hoá trung tâm dữ liệu | Đàm phán HĐ 3 bên | 4900000000 | Sao Mai Telecom | Bùi Ngọc Đạt | 29/10/2026 | Microsoft |  | Vốn doanh nghiệp | Đã được bảo vệ | Đã duyệt | Chốt điều khoản thanh toán với SI và chủ đầu tư | Thống nhất giá, chờ pháp chế nhà mạng duyệt hợp đồng. |

### 6.2 Pipeline "Phát triển Đại lý & Bán chéo"

| # | Deal name | Stage | Deal value | Account | Contact | Deal owner | Expected close date | Nguồn cơ hội | Ngành hàng mục tiêu | Hãng mục tiêu | Sản lượng dự kiến/tháng (VND) | Bước tiếp theo |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Chuỗi Điện máy Sao Việt – Mở ngành Thiết bị mạng Cisco | Phát hiện cơ hội | 10800000000 | Chuỗi Điện máy Sao Việt | Ngô Quốc Quân | SALES_NAM | 28/12/2026 | AI gợi ý từ dữ liệu PO | Thiết bị mạng | Cisco | 1800000000 | Gọi chủ đại lý giới thiệu chương trình |
| 2 | Tin học Đức Trí – Mở ngành Máy tính Dell | Phát hiện cơ hội | 3900000000 | Tin học Đức Trí | Lý Thu Yến | SALES_BAC | 23/11/2026 | Đại lý hỏi qua Zalo OA | Máy tính | Dell | 650000000 | Gọi chủ đại lý giới thiệu chương trình |
| 3 | Máy tính Hồng Phát – Mở ngành Máy tính HP | Phát hiện cơ hội | 1800000000 | Máy tính Hồng Phát | Nguyễn Hải Hương | SALES_BAC | 13/12/2026 | AI gợi ý từ dữ liệu PO | Máy tính | HP | 300000000 | Gọi chủ đại lý giới thiệu chương trình |
| 4 | Chuỗi Laptop An Phát Digital – Mở ngành Smart Device Xiaomi | Tư vấn ngành hàng | 7200000000 | Chuỗi Laptop An Phát Digital | Vũ Ngọc Hà | SALES_BAC | 08/12/2026 | Chương trình của Hãng | Smart Device | Xiaomi | 1200000000 | Mang hàng demo xuống cửa hàng |
| 5 | Siêu thị Điện tử Hoàng Long – Mở ngành Linh kiện & Ngoại vi Intel | Tư vấn ngành hàng | 5400000000 | Siêu thị Điện tử Hoàng Long | Phạm Thu Vy | SALES_BAC | 03/12/2026 | AI gợi ý từ dữ liệu PO | Linh kiện & Ngoại vi | Intel | 900000000 | Mang hàng demo xuống cửa hàng |
| 6 | Công ty TNHH Tin học Thành Đạt – Mở ngành Phần mềm & Cloud Microsoft | Tư vấn ngành hàng | 1500000000 | Công ty TNHH Tin học Thành Đạt | Lý Ngọc Hùng | SALES_BAC | 28/11/2026 | Sales phát hiện khi thăm | Phần mềm & Cloud | Microsoft | 250000000 | Mang hàng demo xuống cửa hàng |
| 7 | Tin học Hải Âu – Mở ngành Thiết bị mạng Cisco | Tư vấn ngành hàng | 2400000000 | Tin học Hải Âu | Hoàng Đức Khoa | SALES_BAC | 13/12/2026 | Sales phát hiện khi thăm | Thiết bị mạng | Cisco | 400000000 | Mang hàng demo xuống cửa hàng |
| 8 | Chuỗi Di động Thế Hệ Mới – Mở ngành Máy tính Apple | Đại lý đặt thử | 19200000000 | Chuỗi Di động Thế Hệ Mới | Bùi Quốc Long | SALES_NAM | 13/11/2026 | Chương trình của Hãng | Máy tính | Apple | 3200000000 | Kiểm tra sell-out lô thử sau 2 tuần |
| 9 | Tin học Ngọc Thịnh – Mở ngành Thiết bị mạng Cisco | Đại lý đặt thử | 3120000000 | Tin học Ngọc Thịnh | Lê Thu Hương | SALES_NAM | 08/11/2026 | AI gợi ý từ dữ liệu PO | Thiết bị mạng | Cisco | 520000000 | Kiểm tra sell-out lô thử sau 2 tuần |
| 10 | Máy tính Trường Sơn – Mở ngành Smart Device Xiaomi | Đại lý đặt thử | 2280000000 | Máy tính Trường Sơn | Phạm Bảo Sơn | SALES_BAC | 13/11/2026 | Sales phát hiện khi thăm | Smart Device | Xiaomi | 380000000 | Kiểm tra sell-out lô thử sau 2 tuần |
| 11 | Hệ thống Bán lẻ Công nghệ Nhật Minh – Mở ngành Phần mềm & Cloud Microsoft | Đặt hàng định kỳ | 9000000000 | Hệ thống Bán lẻ Công nghệ Nhật Minh | Đặng Đức Phong | SALES_BAC | 24/10/2026 | Chương trình của Hãng | Phần mềm & Cloud | Microsoft | 1500000000 | Đề xuất mức sản lượng cam kết quý sau |
| 12 | Laptop Tâm An – Mở ngành Linh kiện & Ngoại vi Intel | Đặt hàng định kỳ | 4200000000 | Laptop Tâm An | Trần Thị Đạt | SALES_BAC | 21/10/2026 | AI gợi ý từ dữ liệu PO | Linh kiện & Ngoại vi | Intel | 700000000 | Đề xuất mức sản lượng cam kết quý sau |

---

## PHẦN 7 — Làm dày 3 deal chủ lực (để mở trong buổi demo)

| Deal | Việc cần làm |
|---|---|
| Ban QLDA Chuyển đổi số tỉnh Đông Hải – Trung tâm IOC tỉnh giai đoạn 2 | Thêm 2 **Note** vào Work stream: (1) *"Họp với Trưởng ban QLDA: hồ sơ mời thầu phát hành, yêu cầu bảo hành 5 năm tại chỗ, Dell cần duyệt giá đặc biệt trước ngày mở thầu."* (2) *"Thăng Long Tech đề nghị Synnex FPT hỗ trợ bảo lãnh dự thầu 2% giá trị."* · Task **"Gửi tờ trình giá đặc biệt cho Dell"** hạn **hôm qua** (quá hạn) · Task **"Hoàn thiện hồ sơ năng lực"** hạn **hôm nay** · 1 comment ở Discussion: *"@Trưởng kênh cần anh/chị hỗ trợ đẩy Dell duyệt giá tuần này."* |
| Ngân hàng TMCP Sao Bắc Á – Máy tính giao dịch viên 600 bộ | Note: *"Đã thống nhất giá với ngân hàng, đang rà điều khoản HĐ 3 bên: ngân hàng – Thăng Long Tech – Synnex FPT; tạm ứng 30%."* · Task **"Gửi dự thảo HĐ 3 bên cho pháp chế"** hạn **+2 ngày** |
| Chuỗi Điện máy Sao Việt – Mở ngành Thiết bị mạng Cisco | Note: *"AI phát hiện: Sao Việt mua Máy tính đều 12 tháng nhưng chưa phát sinh PO Thiết bị mạng. 34 cửa hàng đang dùng router dân dụng."* · Task **"Hẹn chủ chuỗi giới thiệu Cisco SMB Partner Q4"** hạn **+1 ngày** |

Thêm 1 note cho account **Tin học Đức Trí**: *"Đại lý nhắn Zalo OA hỏi chính sách chiết khấu Q4 và xin báo giá 50 laptop Dell Vostro — chatbot đã chuyển thành cơ hội."*

## PHẦN 8 — Dashboard

`Reports → + New dashboard`, tên **Tổng quan kinh doanh Synnex FPT**, mô tả *"Pipeline dự án, bán chéo đại lý và hiệu suất Sales."* Tạo chart:
1. **Summary** "Tổng quan pipeline dự án" — Deals + Deal value, pipeline Dự án B2G & Enterprise.
2. **Funnel** "Phễu dự án theo giai đoạn" — Deals, group by Stage.
3. **Bar** "Cơ hội bán chéo theo nhân viên" — Deal value, pipeline Bán chéo, group by Owner.
4. **Pie** "Cơ hội bán chéo theo nguồn" — Deals, group by *Nguồn cơ hội* (nếu chart cho chọn custom field; không có thì bỏ qua).

## PHẦN 9 — Nghiệm thu (agent tự kiểm, báo cáo kết quả từng dòng)

- [ ] 2 pipeline đủ stage, không stage nào trống deal.
- [ ] Tổng giá trị pipeline Dự án ≈ **193,9 tỷ**; Bán chéo ≈ **70,8 tỷ**; tiền tệ đều VND, không có `$`.
- [ ] Mở deal IOC: có Primary account, Primary contact, custom field, 2 note, 1 task quá hạn.
- [ ] `Home → Tasks` có việc hôm nay và việc quá hạn.
- [ ] `Duplications` không báo trùng.
- [ ] Mở 1 deal → bấm icon Copilot (tia sáng ở header) → hỏi *"Tóm tắt deal và 3 việc cần làm"* → có câu trả lời bám rule.
- [ ] Liệt kê mọi mục đã bỏ qua hoặc lỗi để người dùng xử lý tay.

> **Giới hạn đã biết của Base Sales (đừng cố làm):** Automations / Sequences / SLAs / Agent flows cấp deal đang "coming soon"; Webhooks và Permissions ở Settings tổng "lands in the next iteration"; Copilot chỉ chạy khi đang mở deal/account/report; Inboxes cần nối mailbox ở app Mail.
