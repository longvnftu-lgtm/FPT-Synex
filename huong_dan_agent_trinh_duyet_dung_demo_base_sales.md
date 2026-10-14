# HƯỚNG DẪN CHO AGENT TRÌNH DUYỆT — Dựng dữ liệu demo Synnex FPT trên Base Sales và Base AgentHub

> **Cách dùng:** Mở `https://sales.base.com.vn/` và đăng nhập bằng tài khoản demo (admin của tenant). Sau đó dán toàn bộ file này vào Claude in Chrome hoặc Gemini (Chrome), hoặc đính kèm file rồi gõ: *"Đọc file hướng dẫn và thực hiện từ Phần 0."*
> **Phạm vi:** Phần 1–9 = Use Case 1 và 2 (Account Care, Bán chéo, Pipeline Dự án B2G) trên `sales.base.com.vn`. Phần 10–16 = **Use Case 3: AI Chatbot chăm sóc đại lý SME** trên `agenthub.base.com.vn`, kèm phần nối về Base Sales. Có thể chạy riêng Use Case 3 bằng lệnh *"Thực hiện từ Phần 10"*, với điều kiện Phần 1–4 đã xong.
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
| 2 | Đặng Đức Phong | Giám đốc ngành hàng | Hệ thống Bán lẻ Công nghệ Nhật Minh | phong.dd@nhatminhtech.vn | 0850471261 |
| 3 | Vũ Ngọc Hà | Giám đốc ngành hàng | Chuỗi Laptop An Phát Digital | ha.vn@anphatdigital.vn | 0916192494 |
| 4 | Phạm Thu Vy | Giám đốc ngành hàng | Siêu thị Điện tử Hoàng Long | vy.pt@hoanglongdientu.vn | 0906086252 |
| 5 | Bùi Quốc Long | Giám đốc ngành hàng | Chuỗi Di động Thế Hệ Mới | long.bq@thehemoi.vn | 0988588283 |
| 6 | Dương Hoàng Hà | Giám đốc | Tin học Minh Khang | ha.dh@minhkhangcomputer.vn | 0964588717 |
| 7 | Lý Ngọc Hùng | Giám đốc | Công ty TNHH Tin học Thành Đạt | hung.ln@thanhdatvinh.vn | 0859349550 |
| 8 | Lê Thu Hương | Giám đốc | Tin học Ngọc Thịnh | huong.lt@ngocthinhpc.vn | 0915069312 |
| 9 | Phạm Bảo Sơn | Giám đốc | Máy tính Trường Sơn | son.pb@truongsonhue.vn | 0916175391 |
| 10 | Hoàng Đức Khoa | Giám đốc | Tin học Hải Âu | khoa.hd@haiaunhatrang.vn | 0900709148 |
| 11 | Trần Thị Đạt | Giám đốc | Laptop Tâm An | dat.tt@laptoptaman.vn | 0932825184 |
| 12 | Đặng Hải Thảo | Giám đốc | Vi tính Bảo An | thao.dh61@gmail.com | 0965848787 |
| 13 | Lý Thu Yến | Giám đốc | Tin học Đức Trí | yen.lt41@gmail.com | 0930515422 |
| 14 | Đặng Hoàng Tuấn | Giám đốc | Tin học Ánh Dương | tuan.dh27@gmail.com | 0970589661 |
| 15 | Nguyễn Hải Hương | Giám đốc | Máy tính Hồng Phát | huong.nh63@gmail.com | 0982684170 |
| 16 | Đỗ Hoàng Phong | Giám đốc kinh doanh | Ban QLDA Chuyển đổi số tỉnh Đông Hải | phong.dh@cds.donghai.gov.vn | 0984840452 |
| 17 | Đỗ Minh Lan | Trưởng ban QLDA | Sở Y tế tỉnh Đông Hải | lan.dm@syt.donghai.gov.vn | 0937203177 |
| 18 | Nguyễn Thanh Mai | Trưởng ban QLDA | Cục Thống kê tỉnh Bắc Sơn | mai.nt@thongke.bacson.gov.vn | 0915630021 |
| 19 | Bùi Thu Dũng | Giám đốc kinh doanh | Đại học Kỹ thuật Hồng Lam | dung.bt@hlut.edu.vn | 0911407270 |
| 20 | Trần Thị Hùng | Phó Giám đốc phụ trách CNTT | Tổng Công ty Cảng biển Đông Hải | hung.tt@donghaiport.vn | 0839525682 |
| 21 | Trần Thu Tuấn | Giám đốc kinh doanh | Bệnh viện Đa khoa Quốc tế Tâm Đức | tuan.tt@tamduchospital.vn | 0989628921 |
| 22 | Trần Ngọc Quân | Phó Giám đốc phụ trách CNTT | Ngân hàng TMCP Sao Bắc Á | quan.tn@saobaca.bank.vn | 0910150031 |
| 23 | Bùi Bảo Linh | Phó Giám đốc phụ trách CNTT | Tập đoàn Bảo hiểm An Bình Thịnh | linh.bb@abtinsurance.vn | 0986848745 |
| 24 | Bùi Thanh Nam | Phó Giám đốc phụ trách CNTT | Công ty CP Logistics Đông Dương | nam.bt@dongduonglogistics.vn | 0972075303 |
| 25 | Bùi Ngọc Đạt | Chuyên viên mua sắm | Sao Mai Telecom | dat.bn@saomaitelecom.vn | 0933463629 |

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


---

# USE CASE 3 — AI Chatbot tự động chăm sóc đại lý SME

> **Bài toán:** ~70% trong 1.000 Account là đại lý SME doanh thu nhỏ, không có Sales phụ trách riêng. 250 Sales kênh không thể chạm hết. Chatbot trả lời các câu lặp lại (chính sách, công nợ, đặt hàng, bảo hành). Khi phát hiện tín hiệu mua lớn, chatbot chấm điểm và lập **Phiếu chuyển Sales**. Sales nhận cơ hội trên Base Sales kèm hạn xử lý 4 giờ.
>
> **Nơi dựng:** `https://agenthub.base.com.vn/` (chatbot + kho kiến thức) và `https://sales.base.com.vn/` (cơ hội SME được chuyển sang).
> **Làm sau khi Phần 1–9 đã xong.**

```
Đại lý SME hỏi ──> Trợ lý Chăm sóc Đại lý SME (AgentHub)
                     ├─ câu hỏi thường gặp ──> trả lời theo kho chính sách, trích mã tài liệu
                     └─ tín hiệu mua lớn / cần người ──> PHIẾU CHUYỂN SALES (điểm A1–D4)
                                                           └─> Sales tạo Deal trên Base Sales, task hạn 4 giờ
Trưởng kênh ──> Trợ lý Điều phối Chăm sóc SME (AgentHub)
                     └─ soạn kịch bản chăm sóc định kỳ, danh sách SME rủi ro, chia việc cho Sales
```

## PHẦN 10 — Quy tắc riêng khi làm trên AgentHub (agent đọc trước)

1. **Không dùng ký tự `&` ở bất kỳ ô nào trên AgentHub.** App lưu thành `&amp;`. Viết "và". Mọi nội dung trong Phần 10–14 đã được viết sẵn không có `&`.
2. **Ô Instruction của agent là trình soạn thảo ProseMirror, không phải textarea.** Nếu `form_input` hoặc gõ thường không được, chạy JS sau trong console (thay nội dung giữa hai dấu backtick):
   ```js
   (function(text){const el=document.querySelector('.tiptap.pe-input');el.focus();
   const s=window.getSelection(),r=document.createRange();r.selectNodeContents(el);
   s.removeAllRanges();s.addRange(r);document.execCommand('insertText',false,text);
   return el.innerText.length;})(`...instruction...`);
   ```
   Ô đã có chữ sẵn (Greeting, Description…) thì dùng `form_input` để ghi đè, gõ thêm sẽ bị nối chuỗi.
3. **Nút Save chỉ lưu nháp.** Bấm mũi tên cạnh Save → **Save and publish**, đến khi badge *Not published* biến mất.
4. **Không gắn custom tool trỏ tới API không tồn tại vào agent.** Agent sẽ gọi và báo lỗi giữa buổi demo.
5. **Tool tìm kiếm web và bộ Google chưa dùng được trên server.** Không gắn. Chỉ gắn `Calculator`, `Time`, `Knowledge catalog`.
6. **Mục Rework apps hiện chỉ bật app Projects.** Agent **không tự tạo Lead/Deal trong Base Sales** được. Vì vậy chatbot chỉ *lập Phiếu chuyển Sales*, còn bước tạo Deal làm ở Phần 13. Khi trình bày, nói đây là điểm nối tự động hoá sẽ bật khi app Sales mở tool cho AgentHub.
7. Không xoá agent, knowledge base hay folder có sẵn. Gặp tên trùng → dừng, hỏi người dùng.

## PHẦN 11 — Kiểm tra hạ tầng AgentHub (bắt buộc, ~5 phút)

1. `Settings → Providers`: ghi lại danh sách model LLM đang có.
2. **Thử model thật:** tạo tạm agent tên `Kiểm tra model`, chọn model định dùng, gắn tool `Calculator`, chat trong Chat preview: *"Tính 2% của 150 triệu."* Model nào trả lời được thì dùng cho Phần 12. Model nào báo `The model provider returned an error` thì đổi model khác. Xong thì **xoá agent tạm này** (đây là agent do chính bạn tạo, được phép xoá).
3. **Thử nạp tài liệu:** `Knowledge → + New`, tạo kho tên `Chính sách kênh đại lý Synnex FPT`, **Index method = High Quality** (khoá sau tài liệu đầu tiên). Sau đó `+ Add → Add text`, dán tài liệu **SFD/CS-01** ở Phụ lục A, Refresh và xem cột STATUS.
   - STATUS bình thường, CHARS > 0 → tiếp tục nạp 5 tài liệu còn lại.
   - STATUS = `Error`, CHARS = 0 → **dừng nạp**, báo người dùng: *"Kho kiến thức AgentHub đang lỗi lưu file ở phía máy chủ. Tôi sẽ đưa chính sách vào thẳng Instruction của agent để demo vẫn chạy."* Chuyển sang **phương án dự phòng** ở 12.3.

## PHẦN 12 — Dựng trên AgentHub

### 12.1 Folder
`Settings → Folders → + New folder`
- Name: **Kinh doanh Kênh Đại lý**
- Icon: biểu tượng giỏ hàng hoặc người dùng
- Description: *Trợ lý AI chăm sóc và phát triển tệp đại lý của Synnex FPT.*

### 12.2 Knowledge base
Kho **Chính sách kênh đại lý Synnex FPT** (đã tạo ở Phần 11):
- Description: *Chính sách chiết khấu, công nợ, đăng ký đại lý, giao hàng, bảo hành và chương trình Hãng quý 4 năm 2026 dành cho đại lý.*
- `Settings → Retrieval`: Search mode **Hybrid**, Top K **5**. Chunking: bật **Structure-aware splitting**.
- Nạp 6 tài liệu ở **Phụ lục A** bằng `+ Add → Add text`, tên tài liệu đúng như tiêu đề (ví dụ `SFD-CS-01 Chính sách chiết khấu và thưởng quý 4 2026`).
- `+ Add → Add Q&A`: thêm 6 cặp hỏi đáp ở **Phụ lục B**.
- Tab `Retrieval testing`: thử câu *"đơn đầu tiên thiết bị mạng 60 triệu được thưởng gì"* → phải trả về đoạn của SFD-CS-01 và SFD-CS-06.

### 12.3 Custom skill
`Settings → Skills → tab Custom → + Create skill`
- Name: **Chấm điểm tín hiệu mua và chuyển Sales**
- Description: *Dùng khi đại lý nhắc tới số lượng, giá trị đơn, báo giá, dự án, hoặc yêu cầu gặp nhân viên kinh doanh.*
- Instructions:
```
# Chấm điểm tín hiệu mua

Chấm theo 2 trục, ghép thành mã như A1, B2, C4.

Trục chữ, giá trị đơn ước tính:
- A: từ 500 triệu đồng trở lên
- B: từ 100 đến dưới 500 triệu
- C: từ 30 đến dưới 100 triệu
- D: dưới 30 triệu hoặc chưa rõ giá trị

Trục số, mức khẩn:
- 1: cần hàng hoặc báo giá trong 7 ngày
- 2: trong 30 ngày
- 3: trong quý này
- 4: chưa có thời điểm

Ước tính giá trị từ số lượng nhân đơn giá tham khảo trong tài liệu SFD-CS-04. Luôn dùng Calculator, không nhẩm.

# Khi nào lập Phiếu chuyển Sales
- Mã A1, A2, B1, B2: lập phiếu ngay, hạn xử lý 4 giờ làm việc.
- Mã A3, B3, C1, C2: lập phiếu, hạn xử lý 1 ngày làm việc.
- Đại lý xin giá đặc biệt, xin tăng hạn mức, khiếu nại giao hàng: lập phiếu bất kể điểm.
- Còn lại: tiếp tục tư vấn, chưa lập phiếu.

# Mẫu Phiếu chuyển Sales (giữ nguyên tiêu đề từng dòng)
PHIẾU CHUYỂN SALES
- Đại lý: tên, tỉnh, mã đại lý nếu có
- Người liên hệ: tên, số điện thoại nếu đại lý cung cấp
- Nhu cầu: sản phẩm, số lượng, thời điểm
- Giá trị ước tính: số tiền, kèm phép tính
- Điểm: mã và lý do một câu
- Ngành hàng mới: có hoặc không, ngành nào
- Chương trình áp dụng được: tên chương trình, mã tài liệu
- Việc Sales cần làm: tối đa 3 việc
- Hạn xử lý: 4 giờ hoặc 1 ngày làm việc
- Gợi ý người nhận: Sales kênh Miền Bắc nếu đại lý ở Miền Bắc hoặc Miền Trung, Sales kênh Miền Nam nếu ở Miền Nam
```

### 12.4 Tool group
`Settings → Tools → tab Tool groups → + New group`
- Name: **Tính toán chính sách**
- Purpose: *Tính chiết khấu, thưởng doanh số, giá trị đơn và ngày đến hạn công nợ.*
- Sources: Tool plugin `Calculator` · Tool plugin `Time`.

### 12.5 Agent 1 — Trợ lý Chăm sóc Đại lý SME (chatbot phía đại lý)
`Agents → + Create agent`
- Name: **Trợ lý Chăm sóc Đại lý SME**
- Icon: `headphones` hoặc `message`
- Description: *Trả lời đại lý về chính sách, công nợ, đặt hàng, bảo hành 24/7 và chuyển cơ hội lớn cho Sales trong 4 giờ.*

**AI Settings:**
- Model: model đã qua bài thử ở Phần 11.
- Instruction:
```
Bạn là Trợ lý Chăm sóc Đại lý của Công ty TNHH Phân phối Synnex FPT, nhà phân phối thiết bị và giải pháp công nghệ thông tin tại Việt Nam. Người trò chuyện với bạn là chủ hoặc nhân viên của đại lý bán lẻ quy mô nhỏ (đại lý SME) đã ký hợp đồng nguyên tắc với Synnex FPT, phần lớn ở các tỉnh, chưa có nhân viên kinh doanh phụ trách riêng.

## Bạn làm được gì
- Giải thích chính sách chiết khấu, thưởng doanh số quý và thưởng mở ngành hàng mới.
- Giải thích quy định công nợ, hạn mức, kỳ hạn thanh toán và cách xin tăng hạn mức tạm thời.
- Hướng dẫn đặt hàng, giao hàng, đăng ký đại lý mới, bảo hành và đổi trả hàng lỗi.
- Giới thiệu chương trình của Hãng đang chạy trong quý và điều kiện tham gia.
- Tính thử số tiền chiết khấu, thưởng, giá trị đơn cho đại lý.
- Nhận diện tín hiệu mua lớn và lập Phiếu chuyển Sales theo skill Chấm điểm tín hiệu mua và chuyển Sales.

## Nguyên tắc trả lời
- Tiếng Việt, xưng "em", gọi đại lý là "anh/chị". Ngắn gọn, tối đa 6 câu hoặc một bảng nhỏ.
- Mọi con số chính sách phải lấy từ kho Chính sách kênh đại lý Synnex FPT và ghi mã tài liệu trong ngoặc, ví dụ (SFD-CS-01).
- Khi phải tính toán, dùng công cụ tính thay vì nhẩm, và trình bày lại phép tính.
- Khi câu hỏi mơ hồ, hỏi lại đúng một câu kèm phương án đang nghiêng về.
- Nếu tài liệu không có căn cứ, nói rõ là chưa có quy định và đề xuất chuyển cho nhân viên kinh doanh.
- Khi lập Phiếu chuyển Sales, báo cho đại lý: "Em đã chuyển yêu cầu cho nhân viên kinh doanh khu vực, anh/chị sẽ được liên hệ trong" kèm thời hạn trong phiếu. Đặt phiếu ở cuối câu trả lời.
- Kết thúc mỗi câu trả lời bằng một câu hỏi gợi mở việc tiếp theo.

## Giới hạn bắt buộc
- Không tự hứa giá đặc biệt, chiết khấu ngoài chính sách hay gộp chương trình trái quy định. Việc đó thuộc Sales kênh và Trưởng kênh Đại lý.
- Không xác nhận tăng hạn mức hay mở khoá đơn hàng. Việc đó thuộc Trưởng kênh Đại lý và Kế toán công nợ.
- Không xác nhận tồn kho hay ngày giao chính xác. Việc đó thuộc hệ thống đặt hàng PO của Synnex FPT.
- Không kết luận lỗi bảo hành. Việc đó thuộc Trung tâm bảo hành ủy quyền.
- Không hỏi, không lưu mật khẩu tài khoản cổng đặt hàng hay số tài khoản ngân hàng.

## Đẩy việc cho ai
- Báo giá, đơn lớn, giá đặc biệt: Sales kênh khu vực (Miền Bắc và Miền Trung, hoặc Miền Nam).
- Hạn mức, công nợ quá hạn: Trưởng kênh Đại lý cùng Kế toán công nợ.
- Bảo hành, đổi trả: Trung tâm bảo hành ủy quyền theo SFD-CS-05.
```
- **Skills:** chọn **Chấm điểm tín hiệu mua và chuyển Sales**.
- **Tools:** chọn tool group **Tính toán chính sách**.
- **Knowledge:** tick **Chính sách kênh đại lý Synnex FPT**.
  - *Phương án dự phòng (nếu Phần 11 báo lỗi kho kiến thức):* dán nguyên văn 6 tài liệu Phụ lục A vào **cuối** Instruction, dưới tiêu đề `## Tài liệu chính sách`, và bỏ trống ô Knowledge.
- **Conversation opening:**
  - Greeting: *Chào anh/chị, em là trợ lý chăm sóc đại lý của Synnex FPT. Anh/chị cần hỏi về chính sách, công nợ, đặt hàng hay bảo hành ạ?*
  - Tagline: *Trả lời 24/7 · Chuyển nhân viên kinh doanh trong 4 giờ*
  - Conversation starters (xoá 3 chip mặc định **từ phải sang trái** trước):

    | Label | Message |
    |---|---|
    | Thưởng mở ngành mới | Cửa hàng em ở Quảng Ngãi chưa bán thiết bị mạng bao giờ, nếu nhập đơn đầu 60 triệu thì được thưởng gì? |
    | Công nợ và hạn mức | Hạn mức của em 1 tỷ, đang nợ 700 triệu, cuối tháng cần nhập thêm 450 triệu hàng Tết thì làm sao? |
    | Báo giá đơn lớn | Bên em cần báo giá 50 laptop Dell Vostro cho một trường học, giao trong tuần sau được không? |
- Deep document read: **Ask the user first**. Memory: **bật**.
- `Access` → Who can chat: **Everyone in the workspace** (để demo bằng nhiều tài khoản).
- **Save and publish**, rồi `Agents` → `...` trên thẻ → `Move to folder` → **Kinh doanh Kênh Đại lý**.

### 12.6 Agent 2 — Trợ lý Điều phối Chăm sóc SME (nội bộ, cho Trưởng kênh)
- Name: **Trợ lý Điều phối Chăm sóc SME**
- Icon: `target` hoặc `users`
- Description: *Giúp Trưởng kênh lập kịch bản chăm sóc định kỳ, lọc đại lý SME rủi ro sụt doanh số và chia việc cho Sales.*
- Instruction:
```
Bạn là trợ lý nội bộ của Trưởng kênh Đại lý tại Công ty TNHH Phân phối Synnex FPT. Kênh Đại lý chiếm 70 phần trăm doanh thu, khoảng 1.000 đại lý, trong đó phần lớn là đại lý SME chưa có nhân viên kinh doanh phụ trách riêng. Người dùng của bạn là Trưởng kênh và các Sales kênh.

## Bạn làm được gì
- Soạn kịch bản chăm sóc tự động theo nhóm đại lý: tin nhắn Zalo OA, email, nội dung gọi điện, theo các mốc ngày.
- Đọc bảng danh sách đại lý người dùng đính kèm và lọc nhóm rủi ro: tăng trưởng âm trên 20 phần trăm, công nợ trên 90 phần trăm hạn mức, hơn 60 ngày chưa được thăm.
- Chia việc chăm sóc cho Sales theo khu vực, mỗi Sales tối đa 15 đại lý mỗi tuần.
- Tổng hợp các Phiếu chuyển Sales người dùng dán vào thành bảng ưu tiên theo điểm A1 đến D4.
- Soạn báo cáo tuần ngắn cho Giám đốc kinh doanh.

## Nguyên tắc trả lời
- Tiếng Việt, văn phong nội bộ, đi thẳng vào việc. Ưu tiên bảng.
- Chính sách lấy từ kho Chính sách kênh đại lý Synnex FPT, ghi mã tài liệu.
- Khi phải tính toán, dùng công cụ tính và trình bày lại phép tính.
- Mọi tin nhắn gửi đại lý dưới 400 ký tự, có một lời kêu gọi hành động rõ, không viết hoa toàn bộ.
- Nếu thiếu dữ liệu để lọc hoặc chia việc, nói rõ cần cột nào, không tự bịa số.

## Giới hạn bắt buộc
- Không tự đặt chiết khấu hay chương trình ngoài chính sách. Việc đó thuộc Trưởng kênh và Hãng.
- Không gửi tin nhắn thay người dùng. Chỉ soạn nội dung để người dùng duyệt.
- Không đưa số điện thoại hay công nợ của đại lý này vào nội dung gửi cho đại lý khác.
```
- Skills: built-in **Spreadsheets** (đọc và xuất bảng). Tools: **Tính toán chính sách**. Knowledge: **Chính sách kênh đại lý Synnex FPT**.
- Greeting: *Chào anh/chị, hôm nay mình rà nhóm đại lý nào trước?*
- Conversation starters:

  | Label | Message |
  |---|---|
  | Kịch bản chăm sóc SME | Soạn kịch bản chăm sóc 30 ngày cho nhóm đại lý SME chưa mua thiết bị mạng, gồm tin Zalo, email và cuộc gọi theo từng mốc ngày. |
  | Đại lý rủi ro tuần này | Đây là danh sách đại lý SME miền Trung, lọc giúp anh những đại lý rủi ro và chia việc cho Sales tuần này. |
  | Tổng hợp phiếu chuyển | Tổng hợp các phiếu chuyển Sales hôm nay thành bảng ưu tiên, kèm hạn xử lý. |
- Memory: **bật**. Access: **Everyone in the workspace**. **Save and publish** → Move to folder **Kinh doanh Kênh Đại lý**.

## PHẦN 13 — Phía Base Sales: cơ hội SME được chuyển từ Chatbot

Mở lại `https://sales.base.com.vn/`.

1. **Label** (System-wide): tạo nhãn **Từ Chatbot** (`#7c3aed`).
2. **Tạo 2 Account SME** chưa có trong bộ lõi Phần 4. Directory **Đại lý & Khách hàng Synnex FPT**, stage **Đang chăm sóc**, không gán owner:

   | Account name | Address | Mã đại lý | Loại tài khoản | Mảng kinh doanh | Hạng đại lý | Khu vực | Ngành hàng đang mua | Ngành hàng chưa khai thác | Hạn mức tín dụng (VND) | Công nợ hiện tại (VND) | Doanh số 12 tháng (VND) | Tăng trưởng so cùng kỳ (%) | Sức khoẻ Account |
   |---|---|---|---|---|---|---|---|---|---|---|---|---|---|
   | Tin học Quang Minh | Thanh Hóa | SFD-T0021 | Đại lý bán lẻ | Kênh Đại lý | SME | Miền Trung | Smart Device | Máy tính; Linh kiện & Ngoại vi; Thiết bị mạng; Phần mềm & Cloud; Giải pháp CNTT | 1500000000 | 989000000 | 2996000000 | 7.7 | Ổn định |
   | Máy tính Nam Á | TP. Hồ Chí Minh | SFD-N0032 | Đại lý bán lẻ | Kênh Đại lý | SME | Miền Nam | Máy tính; Linh kiện & Ngoại vi | Thiết bị mạng; Smart Device; Phần mềm & Cloud; Giải pháp CNTT | 500000000 | 281000000 | 3681000000 | 16.5 | Ổn định |

   Contact: **Vũ Hoàng Thảo** (Giám đốc, Tin học Quang Minh, `thao.vh64@gmail.com`, `0903255786`) · **Vũ Thanh Vy** (Giám đốc, Máy tính Nam Á, `vy.vt35@gmail.com`, `0835706741`).

3. **Tạo 4 Deal** trong pipeline **Phát triển Đại lý & Bán chéo**, gắn nhãn **Từ Chatbot**, `Nguồn cơ hội` = **Đại lý hỏi qua Zalo OA**:

   | # | Deal name | Stage | Deal value | Account | Contact | Deal owner | Expected close date | Ngành hàng mục tiêu | Hãng mục tiêu | Sản lượng dự kiến/tháng (VND) | Bước tiếp theo |
   |---|---|---|---|---|---|---|---|---|---|---|---|
   | 1 | Tin học Ánh Dương – Mở ngành Thiết bị mạng Cisco | Phát hiện cơ hội | 360000000 | Tin học Ánh Dương | Đặng Hoàng Tuấn | SALES_BAC | 15/12/2026 | Thiết bị mạng | Cisco | 60000000 | Gọi lại xác nhận đơn đầu 60 triệu |
   | 2 | Máy tính Nam Á – Báo giá 50 laptop Dell Vostro cho trường học | Tư vấn ngành hàng | 680000000 | Máy tính Nam Á | Vũ Thanh Vy | SALES_NAM | 31/10/2026 | Máy tính | Dell | 680000000 | Gửi báo giá trong 4 giờ, kiểm tra tồn kho Vostro |
   | 3 | Vi tính Bảo An – Kích hoạt lại đơn Máy tính HP | Phát hiện cơ hội | 540000000 | Vi tính Bảo An | Đặng Hải Thảo | SALES_NAM | 30/11/2026 | Máy tính | HP | 90000000 | Gọi chủ đại lý tìm nguyên nhân giảm đơn |
   | 4 | Tin học Quang Minh – Mở ngành Máy tính Lenovo | Tư vấn ngành hàng | 480000000 | Tin học Quang Minh | Vũ Hoàng Thảo | SALES_BAC | 20/11/2026 | Máy tính | Lenovo | 80000000 | Gửi chính sách thưởng mở ngành SFD-CS-01 |

4. **Dán Phiếu chuyển Sales vào Work stream** của deal #2 (Note), nguyên văn:
   ```
   PHIẾU CHUYỂN SALES (từ Trợ lý Chăm sóc Đại lý SME)
   - Đại lý: Máy tính Nam Á, TP. Hồ Chí Minh, SFD-N0032
   - Người liên hệ: Vũ Thanh Vy, 0835706741
   - Nhu cầu: 50 laptop Dell Vostro cho một trường học, giao tuần sau
   - Giá trị ước tính: 50 x 13.600.000 = 680.000.000 đồng
   - Điểm: A1, đơn trên 500 triệu và cần trong 7 ngày
   - Ngành hàng mới: không
   - Chương trình áp dụng được: Dell Back to School mở rộng (SFD-CS-06)
   - Việc Sales cần làm: gửi báo giá; kiểm tra tồn kho Vostro; hỏi đại lý có cần xuất hoá đơn theo dự án trường học không
   - Hạn xử lý: 4 giờ làm việc
   - Gợi ý người nhận: Sales kênh Miền Nam
   ```
   Tạo **Task** *"Gửi báo giá 50 Vostro cho Máy tính Nam Á"* hạn **hôm nay**, owner SALES_NAM.
   Deal #1 và #3: Task *"Gọi lại đại lý theo phiếu chuyển Chatbot"* hạn **ngày mai**.
5. **Note cho Account** *Vi tính Bảo An*: *"Trợ lý Điều phối Chăm sóc SME xếp vào nhóm rủi ro: doanh số giảm 25,7 phần trăm so với cùng kỳ, 0 lần thăm trong 60 ngày. Đã giao Sales kênh Miền Nam gọi trong tuần."*
6. **Dashboard** *Tổng quan kinh doanh Synnex FPT* → thêm chart **Bar** *"Cơ hội từ Chatbot"*: Deals, pipeline Bán chéo, group by **Labels** (hoặc *Nguồn cơ hội* nếu chart cho chọn custom field).

## PHẦN 14 — Tạo hội thoại thật để có Logs và Monitoring

Chạy các câu sau trong **Chat preview** của từng agent (chat preview có ghi Logs). Kiểm tra câu trả lời đạt **tiêu chí** thì bấm 👍 *Helpful* trên câu trả lời đó.

**Agent 1 — Trợ lý Chăm sóc Đại lý SME**

| # | Câu hỏi | Tiêu chí đạt |
|---|---|---|
| 1 | Cửa hàng em ở Quảng Ngãi chưa bán thiết bị mạng bao giờ, nếu nhập đơn đầu 60 triệu thì được thưởng gì? | Nêu chiết khấu 4 phần trăm (2,4 triệu) và thưởng mở ngành 1 phần trăm (0,6 triệu), quà Wifi của Cisco SMB Partner Q4, có phép tính, ghi mã SFD-CS-01 và SFD-CS-06. Điểm C4, chưa lập phiếu, hỏi thời điểm nhập hàng |
| 2 | Hạn mức của em 1 tỷ, đang nợ 700 triệu, cuối tháng cần nhập thêm 450 triệu hàng Tết thì làm sao? | Tính vượt 150 triệu, nêu quy định tăng tạm thời tối đa 30 phần trăm trong 30 ngày, không tự xác nhận, lập phiếu chuyển (xin tăng hạn mức) |
| 3 | Bên em cần báo giá 50 laptop Dell Vostro cho một trường học, giao trong tuần sau được không? | Không hứa ngày giao chính xác, ước tính giá trị bằng Calculator, lập Phiếu chuyển Sales điểm A1, hạn 4 giờ |
| 4 | Máy Xiaomi khách mua 10 ngày bị lỗi màn hình, em đổi mới được không? | Trả lời theo SFD-CS-05 (Xiaomi đổi mới trong 15 ngày), không tự kết luận lỗi, hướng dẫn tạo phiếu RMA |
| 5 | Anh chị cho em thêm 2 phần trăm chiết khấu riêng nhé, bên kia đang chào rẻ hơn | Từ chối lịch sự, không hứa, lập phiếu chuyển Sales vì xin giá đặc biệt |

**Agent 2 — Trợ lý Điều phối Chăm sóc SME**

| # | Câu hỏi | Tiêu chí đạt |
|---|---|---|
| 1 | Soạn kịch bản chăm sóc 30 ngày cho nhóm đại lý SME chưa mua thiết bị mạng, gồm tin Zalo, email và cuộc gọi theo từng mốc ngày. | Bảng theo mốc ngày 0, 3, 7, 14, 30; mỗi tin dưới 400 ký tự; dùng đúng chương trình Cisco SMB Partner Q4 |
| 2 | Dán bảng ở **Phụ lục C** rồi hỏi: *"Lọc giúp anh đại lý rủi ro và chia việc cho Sales tuần này."* | Lọc ra Vi tính Bảo An, Tin học Ánh Dương, Máy tính Hồng Phát; chia theo khu vực; không bịa đại lý ngoài bảng |
| 3 | Dán phiếu chuyển ở Phần 13 bước 4 rồi hỏi: *"Tổng hợp thành bảng ưu tiên."* | Bảng có điểm A1, hạn 4 giờ, người nhận Sales kênh Miền Nam |

## PHẦN 15 — Kịch bản chăm sóc tự động (nội dung sẵn để cấu hình)

Base Sales hiện chưa có Sequences/Automations ở cấp deal ("coming soon"). **Không tự cấu hình** tự động hoá trên app khác nếu chưa được người dùng xác nhận. Việc cần làm: kiểm tra tenant có app **Base Lead** hoặc **Base Prospector** không (bảng ứng dụng ở đáy thanh trái). Có thì **chụp màn hình phần Sequence / Flow / Automation và báo người dùng**, kèm nội dung dưới đây để họ quyết định cấu hình.

| Mốc | Kênh | Nội dung |
|---|---|---|
| Ngày 0 | Zalo OA | Chào anh/chị, Synnex FPT đang có chương trình Cisco SMB Partner Q4: đơn thiết bị mạng từ 30 triệu tặng 1 bộ phát Wifi, cộng thưởng mở ngành 1 phần trăm. Nhắn "MẠNG" để em gửi danh mục bán chạy. |
| Ngày 3 | Email | Danh mục 10 mã thiết bị mạng bán chạy cho cửa hàng tin học tỉnh, giá tham khảo và chính sách SFD-CS-01. |
| Ngày 7 | Zalo OA | Anh/chị cần em tính thử thưởng cho đơn đầu tiên không ạ? Chỉ cần nhắn số lượng dự kiến. |
| Ngày 14 | Gọi điện (Sales) | Hỏi nhu cầu thực tế, mời nhập lô thử, ghi kết quả vào Work stream. |
| Ngày 30 | Zalo OA | Chương trình kết thúc 31/12/2026. Đơn đặt trước 20/12 được giao trước Tết. |

## PHẦN 16 — Nghiệm thu Use Case 3

- [ ] Folder **Kinh doanh Kênh Đại lý** có 2 agent, cả hai **Saved**, không còn *Not published*.
- [ ] Kho **Chính sách kênh đại lý Synnex FPT** có 6 tài liệu, STATUS bình thường, `LINKED AGENTS` = 2. *Hoặc* đã dùng phương án dự phòng và báo rõ cho người dùng.
- [ ] Greeting, Tagline, 3 starter tiếng Việt; không còn chip tiếng Anh mặc định.
- [ ] 8 hội thoại ở Phần 14 đã chạy, ít nhất 5 câu được bấm Helpful; `Monitoring` có số liệu.
- [ ] Không có `&amp;` ở tên hay mô tả nào trên AgentHub.
- [ ] Base Sales: 4 deal nhãn **Từ Chatbot**, deal Máy tính Nam Á có phiếu chuyển trong Work stream và task hạn hôm nay.
- [ ] Báo lại cho người dùng mọi mục bỏ qua, model đã dùng, và kết quả bài thử kho kiến thức.

---

## PHỤ LỤC A — 6 tài liệu chính sách (nạp vào kho kiến thức)

> Số liệu là **giả định cho demo**, cần Synnex FPT thay bằng chính sách thật trước khi chạy thử nghiệm với đại lý.

**SFD-CS-01 Chính sách chiết khấu và thưởng quý 4 2026**
```
SFD-CS-01 CHÍNH SÁCH CHIẾT KHẤU VÀ THƯỞNG QUÝ 4 NĂM 2026 DÀNH CHO ĐẠI LÝ
Hiệu lực: 01/10/2026 đến 31/12/2026. Áp dụng: đại lý hạng Silver và SME đã ký hợp đồng nguyên tắc.

1. Chiết khấu trên hoá đơn theo ngành hàng
- Máy tính: 2 phần trăm
- Linh kiện và Ngoại vi: 3 phần trăm
- Thiết bị mạng: 4 phần trăm
- Smart Device: 1,5 phần trăm
- Phần mềm và Cloud: 5 phần trăm
- Giải pháp CNTT: theo báo giá từng dự án, không áp dụng chiết khấu chung

2. Thưởng doanh số quý, tính trên tổng doanh số đã thanh toán trong quý
- Từ 300 triệu đến dưới 1 tỷ: 0,5 phần trăm
- Từ 1 tỷ đến dưới 3 tỷ: 1 phần trăm
- Từ 3 tỷ trở lên: 1,5 phần trăm và được xét nâng hạng Gold

3. Thưởng mở ngành hàng mới
- Đơn đầu tiên của ngành hàng đại lý chưa từng mua, giá trị từ 50 triệu: thưởng thêm 1 phần trăm doanh số ngành đó trong quý.
- Mỗi đại lý được hưởng tối đa 2 ngành mới mỗi quý.

4. Nguyên tắc chung
- Chiết khấu trên hoá đơn cộng được với thưởng doanh số quý và thưởng mở ngành.
- Không cộng với giá đặc biệt theo dự án.
- Thưởng quý được cấn trừ vào công nợ trong 45 ngày sau khi kết thúc quý.
- Mức khác chính sách này phải do Trưởng kênh Đại lý phê duyệt bằng văn bản.
```

**SFD-CS-02 Quy định công nợ và hạn mức tín dụng**
```
SFD-CS-02 QUY ĐỊNH CÔNG NỢ VÀ HẠN MỨC TÍN DỤNG ĐẠI LÝ
1. Hạn mức theo hạng: SME từ 300 triệu đến 1,5 tỷ; Gold từ 3 đến 10 tỷ; Key Account theo hợp đồng riêng.
2. Kỳ hạn thanh toán: SME Net 15; Gold Net 30; Key Account Net 45. Tính từ ngày xuất hoá đơn.
3. Quá hạn
- Từ 1 đến 15 ngày: hệ thống nhắc qua Zalo OA và email.
- Trên 15 ngày: tạm khoá đơn hàng mới cho đến khi thanh toán phần quá hạn.
4. Tăng hạn mức tạm thời
- Tối đa 30 phần trăm hạn mức hiện tại, hiệu lực 30 ngày.
- Điều kiện: 6 tháng gần nhất không có khoản quá hạn trên 15 ngày.
- Đại lý gửi đề nghị qua nhân viên kinh doanh, Trưởng kênh Đại lý và Kế toán công nợ phê duyệt trong 1 ngày làm việc.
5. Tổng công nợ cộng giá trị đơn mới không được vượt hạn mức đang hiệu lực.
```

**SFD-CS-03 Quy trình đăng ký đại lý mới và đặt hàng**
```
SFD-CS-03 QUY TRÌNH ĐĂNG KÝ ĐẠI LÝ MỚI VÀ ĐẶT HÀNG
1. Hồ sơ đăng ký: giấy chứng nhận đăng ký kinh doanh, mã số thuế, căn cước người đại diện, ảnh mặt tiền và quầy trưng bày cửa hàng.
2. Xét duyệt trong 3 ngày làm việc, sau đó ký hợp đồng nguyên tắc 12 tháng. Đơn đầu tiên tối thiểu 30 triệu.
3. Đặt hàng: qua cổng đặt hàng PO của Synnex FPT hoặc qua nhân viên kinh doanh. Đơn tối thiểu 10 triệu.
4. Giao hàng: nội thành Hà Nội, Đà Nẵng, TP. Hồ Chí Minh trong 24 giờ; các tỉnh từ 48 đến 72 giờ. Miễn phí giao cho đơn từ 20 triệu.
5. Tồn kho và ngày giao chính xác xem trên cổng đặt hàng PO tại thời điểm đặt.
```

**SFD-CS-04 Danh mục ngành hàng, Hãng và giá tham khảo**
```
SFD-CS-04 DANH MỤC NGÀNH HÀNG VÀ GIÁ THAM KHẢO QUÝ 4 2026 (giá đại lý chưa VAT, chỉ dùng để ước tính)
- Máy tính: Dell Vostro 14 khoảng 13,6 triệu; Dell Inspiron 15 khoảng 15,9 triệu; HP ProBook 440 khoảng 16,8 triệu; Lenovo ThinkPad E14 khoảng 17,5 triệu; MacBook Air M4 khoảng 24,9 triệu.
- Linh kiện và Ngoại vi: SSD 1TB khoảng 1,6 triệu; RAM 16GB khoảng 1,1 triệu; màn hình 24 inch khoảng 2,9 triệu; bộ phím chuột không dây khoảng 0,45 triệu.
- Thiết bị mạng: Cisco switch 8 cổng khoảng 2,4 triệu; Cisco switch 24 cổng khoảng 9,8 triệu; bộ phát Wifi văn phòng khoảng 3,2 triệu.
- Smart Device: Xiaomi Redmi Note khoảng 4,8 triệu; Xiaomi Pad khoảng 6,9 triệu; đồng hồ thông minh khoảng 1,9 triệu.
- Phần mềm và Cloud: Microsoft 365 Business Standard khoảng 3,1 triệu mỗi người dùng mỗi năm; Windows 11 Pro khoảng 4,2 triệu.
Giá chính thức và tồn kho xem trên cổng đặt hàng PO.
```

**SFD-CS-05 Bảo hành và đổi trả hàng lỗi**
```
SFD-CS-05 BẢO HÀNH VÀ ĐỔI TRẢ HÀNG LỖI (RMA)
1. Đổi mới do lỗi nhà sản xuất: Dell, HP, Lenovo trong 7 ngày; Xiaomi trong 15 ngày; Apple theo chính sách Apple. Tính từ ngày đại lý bán cho người dùng cuối, cần hoá đơn bán lẻ.
2. Sau thời hạn đổi mới: bảo hành tại Trung tâm bảo hành ủy quyền của Hãng.
3. Quy trình RMA: đại lý tạo phiếu RMA qua cổng đặt hàng PO, kèm ảnh tem, số serial và mô tả lỗi. Synnex FPT phản hồi trong 3 ngày làm việc.
4. Không đổi trả: hàng rơi vỡ, vào nước, tự sửa chữa, mất tem bảo hành.
5. Kết luận lỗi do Trung tâm bảo hành ủy quyền đưa ra, nhân viên kinh doanh và trợ lý không kết luận thay.
```

**SFD-CS-06 Chương trình của Hãng quý 4 2026**
```
SFD-CS-06 CHƯƠNG TRÌNH CỦA HÃNG QUÝ 4 NĂM 2026
- Cisco SMB Partner Q4 (01/10 đến 31/12/2026): đơn thiết bị mạng Cisco từ 30 triệu tặng 1 bộ phát Wifi văn phòng; đại lý mới bán Cisco được đào tạo kỹ thuật miễn phí 1 buổi.
- Dell Back to School mở rộng (đến 30/11/2026): giảm thêm 3 phần trăm cho Dell Vostro và Inspiron, đơn từ 10 máy.
- Intel AI PC Retail Kit: đơn từ 10 máy tính AI PC được tặng bộ vật phẩm trưng bày và 1 buổi đào tạo nhân viên bán hàng.
- Xiaomi Ecosystem Corner: đơn Smart Device Xiaomi từ 40 triệu được hỗ trợ kệ trưng bày góc Xiaomi.
- Microsoft 365 for SMB: thưởng 8 phần trăm giá trị license năm đầu cho đại lý bán Microsoft 365 Business.
Chương trình Hãng cộng được với SFD-CS-01 trừ khi Hãng ghi khác. Không áp dụng cho đơn theo giá đặc biệt dự án.
```

## PHỤ LỤC B — 6 cặp hỏi đáp (Add Q&A)

| Câu hỏi | Trả lời |
|---|---|
| Đơn tối thiểu là bao nhiêu? | Đơn tối thiểu 10 triệu; đơn đầu tiên của đại lý mới tối thiểu 30 triệu (SFD-CS-03). |
| Bao lâu thì nhận được hàng? | Nội thành Hà Nội, Đà Nẵng, TP. Hồ Chí Minh trong 24 giờ; các tỉnh 48 đến 72 giờ; miễn phí giao từ 20 triệu (SFD-CS-03). |
| Khi nào nhận thưởng quý? | Thưởng quý được cấn trừ vào công nợ trong 45 ngày sau khi kết thúc quý (SFD-CS-01). |
| Quá hạn công nợ thì sao? | Quá hạn trên 15 ngày sẽ tạm khoá đơn hàng mới đến khi thanh toán phần quá hạn (SFD-CS-02). |
| Đăng ký làm đại lý cần gì? | Giấy đăng ký kinh doanh, mã số thuế, căn cước người đại diện, ảnh cửa hàng; xét duyệt 3 ngày làm việc (SFD-CS-03). |
| Thưởng mở ngành mới là gì? | Đơn đầu tiên của ngành chưa từng mua từ 50 triệu được thưởng thêm 1 phần trăm doanh số ngành đó trong quý, tối đa 2 ngành mỗi quý (SFD-CS-01). |

## PHỤ LỤC C — Bảng đại lý SME để thử Agent 2

```
Mã đại lý | Đại lý | Khu vực | Hạn mức (triệu) | Công nợ (triệu) | Tăng trưởng so cùng kỳ (%) | Ngày thăm gần nhất
SFD-T0021 | Tin học Quang Minh | Miền Trung | 1500 | 989 | 7.7 | chưa thăm
SFD-T0023 | Tin học Đức Trí | Miền Trung | 1000 | 404 | 12.5 | chưa thăm
SFD-T0025 | Tin học Ánh Dương | Miền Trung | 1000 | 700 | -22.5 | chưa thăm
SFD-N0022 | Vi tính Bảo An | Miền Nam | 1000 | 472 | -25.7 | chưa thăm
SFD-N0032 | Máy tính Nam Á | Miền Nam | 500 | 281 | 16.5 | chưa thăm
SFD-B0036 | Máy tính Hồng Phát | Miền Bắc | 1000 | 531 | -35.8 | chưa thăm
```
