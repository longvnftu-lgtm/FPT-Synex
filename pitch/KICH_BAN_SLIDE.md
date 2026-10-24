# Guideline và kịch bản slide · Agentic Sale Operation System for Synnex FPT

Tài liệu này mô tả cách deck được dựng và toàn bộ nội dung hiện có (11 slide, 58 bước demo).
Anh sửa trực tiếp phần chữ trong **Phần B** rồi gửi lại file này, em sẽ dựng lại deck theo đúng bản đã sửa.

- Deck: https://claude.ai/artifact/Mn3QqYovBCb8WSaF6niwLj
- Mã nguồn: `pitch/index.html` (giao diện, slide tĩnh) · `pitch/steps.json` (kịch bản các bước demo) · `pitch/screens/` (34 ảnh chụp tenant)

---

## Phần A · Nguyên tắc xây dựng

### A1. Thông điệp
1. **Hook chính:** Xây dữ liệu hành trình khách hàng, tạo bệ phóng cho AI.
2. **Mạch kể:** Nhu cầu của Synnex FPT → Chuỗi giá trị (điểm nghẽn, giá trị) → Lưu đồ giải pháp → Kiến trúc → 4 use case demo → Quản trị AI → Đề xuất showcase.
3. **Viết theo giá trị cho khách hàng:** mỗi đoạn trả lời câu hỏi "Synnex FPT được gì", không mô tả tính năng suông. Mỗi bước demo có 2 phần tách bạch: *Mô tả* (màn hình đang hiện gì) và *Giá trị* (khách được gì).
4. **Bám đúng nhu cầu khách đã nêu:**
   - Kênh Đại lý (70% doanh thu, 250 Sales): theo dõi chăm sóc, tỷ lệ up-sell/cross-sell theo ngành hàng, lưu lại tương tác, quản lý tập trung hội thoại, chatbot cho nhóm SME.
   - Dự án B2G (30% doanh thu, 50 Sales): pipeline từ lead in, deal planning đến closing; theo dõi chăm sóc và chốt deal.
5. **Không dùng giả định ngoài dữ liệu khách cung cấp.** Ví dụ: đã bỏ con số "1.000 đại lý".

### A2. Dữ liệu demo
1. **Mọi bước demo chạy trên ảnh chụp thật của tenant demo.** Không dựng lại màn hình bằng HTML.
2. **Phần Mô tả chỉ ghi những gì có trên ảnh:** số liệu, tên, nhãn, trạng thái đọc từ ảnh. Không thêm số, ngày, tài liệu hay tính năng không có trên màn hình.
3. **Chữ tiếng Anh trên giao diện được giữ nguyên trong ngoặc kép.** Ví dụ ngày "Sun, Oct 18".
4. **Dữ liệu tenant là dữ liệu hư cấu** (account, liên hệ, deal) sinh từ `demo-data/scripts/demo_master.py`. Tên chuỗi thật của khách (TGDĐ, FPT Shop) chỉ xuất hiện ở slide Nhu cầu, vì đó là thông tin khách cung cấp.
5. **Muốn thêm bước mới thì phải có ảnh chụp mới.** Ảnh dán trực tiếp vào chat không lưu được ra file, nên anh gửi ảnh dạng file hoặc zip.

### A3. Giới hạn trình bày (để không tràn khung)
| Thành phần | Giới hạn gợi ý |
|---|---|
| Tiêu đề slide demo (h2) | ≤ 85 ký tự, 1 dòng |
| Tiêu đề slide tĩnh (h2) | ≤ 70 ký tự, tối đa 2 dòng |
| Tên bước | ≤ 45 ký tự |
| Mô tả bước | ≤ 360 ký tự |
| Giá trị bước | ≤ 140 ký tự |
| Nút hành động | ≤ 40 ký tự |
| Ô trong lưu đồ giải pháp | tiêu đề ≤ 25 ký tự, nội dung ≤ 110 ký tự |

### A4. Cơ chế demo (để viết kịch bản cho khớp)
- **Khung demo:** mỗi slide demo có khung ảnh bên trái và bảng kịch bản bên phải (Bước x/y · Tên · Mô tả · Giá trị · Nút).
- **Thao tác:** người trình bày bấm nút, bấm điểm xanh nhấp nháy trên ảnh, bấm số bước, hoặc dùng phím →. Có chế độ Tự chạy, 6 giây mỗi bước.
- **Hiệu ứng trên ảnh:**
  - camera zoom vào vùng đang nói
  - khung vàng (spotlight)
  - viền nét đứt đánh dấu chi tiết
  - điểm bấm màu xanh
  - hiệu ứng "gõ ra" cho câu trả lời AI
- **Toạ độ vùng zoom và đánh dấu nằm trong `steps.json`.** Toạ độ do em chỉnh, anh chỉ cần sửa chữ. Nếu muốn đổi vùng nhấn, anh ghi chú kiểu "zoom vào ô Công nợ".
- **Nút "Màn hình thật (G)"** mở thư viện 34 ảnh gốc.

### A5. Cách sửa và gửi lại
- **Sửa chữ:** sửa trực tiếp trong Phần B.
- **Xoá bước:** ghi `[XOÁ]` cạnh tên bước.
- **Đổi thứ tự:** đánh lại số bước.
- **Thêm bước:** ghi `[THÊM]`, kèm tên ảnh (hoặc gửi ảnh mới) và vùng cần nhấn.
- **Thêm, bớt, đổi thứ tự slide:** ghi rõ ở đầu slide tương ứng.

---

## Phần B · Kịch bản từng slide

### Slide 1 · Mở đầu
- **Dòng trên:** Base.vn × Synnex FPT
- **Tiêu đề:** Agentic Sale Operation System **for Synnex FPT**
- **Hook:** Xây dữ liệu hành trình khách hàng, **tạo bệ phóng cho AI**
- **Đoạn dẫn:** Sales biết chăm sóc đại lý nào và làm gì tiếp theo. Quản lý thấy rõ từng hoạt động, từng deal dự án. Đại lý SME được phục vụ 24/7 mà không cần thêm người.
- **4 chỉ số (chạy số):** 300 · Sales trên 2 mảng kinh doanh | 70% · doanh thu từ kênh Đại lý | 30% · doanh thu từ Dự án B2G | 4 · use case chạy trên tenant demo
- **Chân trang:** Dữ liệu từ tenant demo · 15/10/2026 · Phím ← → để chuyển slide · G để xem màn hình thật
- **Hình nền:** mạng lưới điểm lan toả từ một tâm (tượng trưng hệ thống phân phối)

### Slide 2 · 01 Nhu cầu của Synnex FPT
- **Tiêu đề:** Hai mảng kinh doanh, *hai bài toán quản trị* khác nhau
- **Thanh tỷ trọng:**
  - Kênh Đại lý (B2B channel) · 250 Sales · 4 ngành hàng: Thiết bị máy tính, Linh kiện và ngoại vi, Điện thoại và thiết bị thông minh, Giải pháp CNTT: **70%**
  - Dự án (B2G) · 50 Sales: **30%**
- **Khung "Kênh Đại lý cần"** (Key account · SME)
  - Bối cảnh: Key account: TGDĐ, FPT Shop, các chuỗi lớn · Doanh số tập trung ở vài chục account top · Account đã có hợp đồng nguyên tắc · Đã có hệ thống quản lý PO
  - Theo dõi hoạt động chăm sóc đại lý của Sales và tỷ lệ up-sell, cross-sell theo ngành hàng → UC1
  - Lưu lại toàn bộ quá trình trao đổi, chăm sóc, tương tác với đại lý → UC1 · UC4
  - Một công cụ quản lý tập trung các cuộc hội thoại giữa Sales và đại lý → UC4
  - Nhóm SME chưa có người phụ trách: tự động hoá chăm sóc bằng chatbot, giảm workload → UC3
- **Khung "Dự án B2G cần"** (Bộ ban ngành · HĐ 3 bên)
  - Bối cảnh: Có lead và deal pipeline · Chu kỳ dài, nhiều bên tham gia
  - Quản lý pipeline xuyên suốt từ lead in, deal planning đến closing → UC2
  - Theo dõi quá trình chăm sóc và chốt deal của từng team dự án → UC2
  - Thấy sớm deal chậm tiến độ để lãnh đạo hỗ trợ đúng lúc → UC2

### Slide 3 · 02 Chuỗi giá trị vận hành (tương tác: bấm từng chặng)
- **Tiêu đề:** Mỗi chặng: *điểm nghẽn hôm nay* và giá trị khi có Agentic Sales OS
- Mỗi chặng mở ra 3 cột: Điểm nghẽn hôm nay · Giá trị mang lại · Đo bằng + Use case.

**1. Chăm sóc Key account** (Kênh Đại lý · 70% · 250 Sales · account đã có HĐ nguyên tắc)
- Điểm nghẽn hôm nay: Doanh số tập trung ở vài chục account top, khó thấy sớm account đang chững lại; Quản lý khó biết Sales đã chăm sóc đại lý nào, khi nào, kết quả ra sao
- Giá trị mang lại: Mỗi account có kế hoạch chăm sóc, lịch sử hoạt động và tình trạng sức khoẻ; Quy tắc tự động nhắc Sales khi account cần được chăm sóc
- Đo bằng: Số hoạt động chăm sóc / account / tháng
- Use case: UC1 · Account Farming

**2. Up-sell, cross-sell theo ngành hàng** (Kênh Đại lý · 70% · Máy tính · Ngoại vi · Thiết bị thông minh · Giải pháp CNTT)
- Điểm nghẽn hôm nay: Không thấy ngay đại lý đã mua ngành nào, chưa mua ngành nào; Cơ hội phát hiện khi đi thị trường không được ghi lại
- Giá trị mang lại: Ngành chưa khai thác hiện trên từng account và trở thành deal bán chéo; Copilot tóm tắt và đề xuất việc cần làm cho từng cơ hội
- Đo bằng: Tỷ lệ up-sell, cross-sell theo ngành hàng
- Use case: UC1 · Pipeline Phát triển Đại lý & Bán chéo

**3. Hội thoại với đại lý** (Kênh Đại lý · 70% · Chat, điện thoại, email)
- Điểm nghẽn hôm nay: Trao đổi với đại lý nằm trong điện thoại và ứng dụng chat cá nhân của Sales; Sales đổi tuyến hoặc nghỉ việc là mất lịch sử chăm sóc
- Giá trị mang lại: Hội thoại tập trung về một Hộp thư, gắn với hồ sơ khách hàng; AI tự ghi thông tin khách; Sales hỏi AI để nắm nhanh ngữ cảnh
- Đo bằng: Thời gian phản hồi · tỷ lệ hội thoại có người phụ trách
- Use case: UC4 · Chat đa kênh và AI tư vấn

**4. Chăm sóc tự động nhóm SME** (Kênh Đại lý · SME · Doanh thu vài trăm triệu đến vài tỷ, chưa có người phụ trách)
- Điểm nghẽn hôm nay: Nhóm SME đông nhưng chưa có Sales phụ trách riêng; Câu hỏi chính sách, công nợ, bảo hành lặp lại mỗi ngày
- Giá trị mang lại: AI trả lời 24/7 theo đúng chính sách, có trích số chính sách; Chấm điểm tín hiệu mua, chuyển cơ hội lớn cho Sales trong 4 giờ
- Đo bằng: Số câu hỏi AI xử lý · số cơ hội chuyển Sales
- Use case: UC3 · AI chat tự động cho SMEs GTM

**5. Lead in → deal planning → closing** (Dự án B2G · 30% · 50 Sales · Bộ ban ngành · HĐ 3 bên)
- Điểm nghẽn hôm nay: Deal kéo dài nhiều tháng, khó biết đang nghẽn ở giai đoạn nào; Phối hợp Hãng, SI, chủ đầu tư qua email rời rạc, không lưu vết
- Giá trị mang lại: Pipeline 5 giai đoạn có SLA, kế hoạch việc và team dự án trên từng deal; AI đọc dashboard, chỉ ra deal và rủi ro cần chú ý
- Đo bằng: Số deal quá SLA · tỷ lệ chuyển giai đoạn
- Use case: UC2 · Quy trình bán hàng B2G

**6. PO, tín dụng, giao hàng** (Thực thi · Giữ nguyên hệ thống PO hiện có)
- Điểm nghẽn hôm nay: Sales nhập liệu hai nơi; Vượt hạn mức mới biết, đơn bị chặn
- Giá trị mang lại: Base đứng phía trước, không thay hệ thống PO; Doanh số, công nợ đồng bộ về account khi triển khai tích hợp
- Đo bằng: Số đơn bị chặn vì hạn mức
- Use case: Tích hợp PO/ERP khi triển khai

### Slide 4 · 03 Lưu đồ giải pháp
- **Tiêu đề:** Một luồng vận hành cho *cả hai mảng kinh doanh*, AI đồng hành ở từng chặng
- **5 chặng (cột):** 1 Tiếp nhận → 2 Chăm sóc & tư vấn → 3 Cơ hội & kế hoạch → 4 Chốt & thực thi → 5 Đo lường & cải tiến
- **Dấu ✦** đánh dấu chặng có AI tham gia. Nhãn UC bấm được để mở slide demo.

| Làn | 1 Tiếp nhận | 2 Chăm sóc & tư vấn | 3 Cơ hội & kế hoạch | 4 Chốt & thực thi | 5 Đo lường |
|---|---|---|---|---|---|
| **Key account** (Kênh Đại lý · 250 Sales) | **Account có HĐ nguyên tắc**: Danh bạ đại lý tập trung, phân hạng Key Account, Gold, Silver, SME. [UC1] | **Kế hoạch chăm sóc**: Gọi, email, họp, fieldwork, báo giá ghi trên hồ sơ đại lý. ✦ Nhắc việc theo quy tắc [UC1] | **Khai thác ngành hàng**: Ngành chưa mua thành deal up-sell, cross-sell. ✦ Copilot đề xuất việc cần làm [UC1] | **Báo giá → PO**: Đặt hàng trên hệ thống PO hiện có của Synnex FPT. | **Đo lường**: Hoạt động chăm sóc theo Sales, tỷ lệ up-sell, cross-sell theo ngành. [UC1] |
| **Đại lý SME** (Chưa có người phụ trách) | **Chat đa kênh**: Mọi hội thoại của đại lý và khách về một Hộp thư. [UC4] | **AI tư vấn 24/7**: Trả lời chính sách, công nợ, bảo hành bằng ngôn ngữ tự nhiên. ✦ Tự ghi hồ sơ khách [UC3, UC4] | **Chấm điểm tín hiệu mua**: ✦ Cơ hội A1 đến B2 được lập Phiếu chuyển Sales, hạn 4 giờ. [UC3] | **Sales tiếp nhận**: Nhận hội thoại kèm ngữ cảnh, báo giá, chốt đơn. ✦ Copilot tóm tắt, gợi ý trả lời [UC4] | **Đo lường**: Chất lượng trả lời của AI, số cơ hội chuyển Sales, kịch bản chăm sóc 30 ngày. [UC3, Quản trị AI] |
| **Dự án B2G** (50 Sales · HĐ 3 bên) | **Lead in**: Lead dự án từ Bộ ban ngành, Hãng, SI vào pipeline B2G. [UC2] | **Khảo sát & tư vấn**: Team dự án cùng làm việc, thảo luận và tag người hỗ trợ ngay trên deal. [UC2] | **Deal planning**: Đăng ký Deal Hãng, kế hoạch việc có hạn, giá đặc biệt. ✦ Copilot review kế hoạch [UC2] | **Closing**: Báo giá & hồ sơ thầu, đàm phán HĐ 3 bên, SLA từng giai đoạn. [UC2] | **Đo lường**: Phễu theo giai đoạn, doanh thu dự kiến. ✦ AI đọc dashboard [UC2] |

- **Nền tảng dùng chung:**
  - **Tầng AI:** Copilot trên account, deal và hội thoại · Trợ lý AgentHub · Trợ lý tư vấn trong Hộp thư · Quy tắc và quy trình tự động. AI làm theo chính sách do Synnex FPT đặt ra.
  - **Dữ liệu:** Một hồ sơ khách hàng duy nhất trên Base Sales gồm hoạt động, hội thoại, ngành hàng, doanh số, công nợ. Đồng bộ PO/ERP khi triển khai.
- **Lưu ý:** "✦ Copilot review kế hoạch" (UC2) và "✦ Nhắc việc theo quy tắc" (UC1) là mô tả đề xuất, chưa có ảnh chụp minh hoạ trong demo.

### Slide 5 · 04 Kiến trúc đề xuất
- **Tiêu đề:** Base là *lớp vận hành phía trước*, hệ thống PO giữ nguyên phía sau
- **Điểm chạm** (ai dùng, ở đâu): Đại lý và khách nhắn qua kênh chat · Sales chăm sóc, đi thị trường · Trưởng kênh, Ban lãnh đạo xem dashboard
- **Tầng Agent** (Base AgentHub + Copilot): Trợ lý Chăm sóc Đại lý SME · Trợ lý Điều phối Chăm sóc SME · Trợ lý tư vấn SME trong Hộp thư · Copilot trên account, deal, hội thoại · Phân tích AI trên dashboard
- **Tầng ứng dụng** (quy trình bán hàng): Base Sales · 2 pipeline · Danh bạ Đại lý và Khách hàng · Hộp thư hội thoại đa kênh · Báo giá · Quy trình tự động · SLA
- **Tầng dữ liệu** (một nguồn sự thật): Một hồ sơ khách hàng: hoạt động, hội thoại, ngành hàng, doanh số, hạn mức, công nợ · Hệ thống PO / ERP Synnex FPT (viền nét đứt: hệ thống hiện có)
- **Ghi chú:** Synnex FPT giữ nguyên hệ thống PO đang chạy, Sales không phải nhập liệu hai nơi. Trên tenant demo, doanh số và công nợ được nhập vào trường dữ liệu của account; khi triển khai sẽ đồng bộ từ PO/ERP qua tích hợp.

### Slide 6 · Use case 1 · Account Farming (demo 14 bước)
- **Dòng trên:** Quản lý account · kế hoạch chăm sóc · AI hỏi đáp
- **Tiêu đề:** Sales biết *chăm sóc ai, làm gì tiếp theo*; quản lý thấy được từng hoạt động

#### Bước 1 · Trang chủ Base Sales
- **Ảnh:** `01_sales_trang_chu_thuong_vu.jpg` (Trang chủ Base Sales: 31 thương vụ, 2 pipeline FPT Synnex)
- **Mô tả:** Long Nguyễn đang phụ trách 31 thương vụ trên 2 pipeline [FPT Synnex]: Phát triển Đại lý & Bán chéo và Dự án B2G & Enterprise.
- **Giá trị:** Mỗi Sales mở máy là thấy toàn bộ cơ hội mình phụ trách trên cả hai mảng, không phải tổng hợp từ Excel.
- **Nút hành động:** Bấm Công ty để mở danh bạ đại lý  _(có điểm bấm trên ảnh)_

#### Bước 2 · Danh bạ Đại lý & Khách hàng
- **Ảnh:** `04_sales_danh_sach_dai_ly_khach_hang.jpg` (Danh bạ 25 đại lý và khách hàng, lọc theo phân hạng)
- **Mô tả:** 25 bản ghi, xem dạng Bảng hoặc Kanban, cột Tên, Tên miền, Địa chỉ, Chủ sở hữu. Bộ lọc bên trái theo Phân hạng đại lý: Key Account, Gold, Silver, SME.
- **Giá trị:** Danh bạ đại lý tập trung, phân hạng rõ ràng, giúp Trưởng kênh phân bổ nguồn lực chăm sóc theo giá trị của từng account.
- **Nút hành động:** Bấm Chuỗi Điện máy Sao Việt  _(có điểm bấm trên ảnh)_

#### Bước 3 · Kế hoạch hành động của account
- **Ảnh:** `05_sales_account_saoviet_tong_quan.jpg` (Account Chuỗi Điện máy Sao Việt: tổng quan, nhật ký thị sát)
- **Mô tả:** Công việc đang mở: "Thẩm định kỳ chuỗi Sao Việt – review doanh số Q4 và công…", hạn Sun, Oct 18. Việc cần làm cá nhân ở ngay bên dưới.
- **Giá trị:** Mỗi account có kế hoạch chăm sóc cụ thể, có hạn, có người làm. Quản lý theo dõi được mà không cần hỏi lại Sales.
- **Nút hành động:** Tiếp

#### Bước 4 · Ghi mọi loại hoạt động
- **Ảnh:** `05_sales_account_saoviet_tong_quan.jpg` (Account Chuỗi Điện máy Sao Việt: tổng quan, nhật ký thị sát)
- **Mô tả:** Dòng công việc nhận Ghi chú, Email, Cuộc gọi, Cuộc họp, Log activity. Menu trái của account có thêm Công việc hiện trường cho fieldwork và Quy trình tự động.
- **Giá trị:** Mọi cuộc gọi, email, buổi họp, chuyến đi thị trường đều nằm trên hồ sơ đại lý, không còn thất lạc trong điện thoại hay sổ tay cá nhân.
- **Nút hành động:** Tiếp

#### Bước 5 · Nhật ký thị sát (fieldwork)
- **Ảnh:** `05_sales_account_saoviet_tong_quan.jpg` (Account Chuỗi Điện máy Sao Việt: tổng quan, nhật ký thị sát)
- **Mô tả:** "Nhật ký thị sát 10/10: thăm 3 cửa hàng Quận 1, Quận 7, Thủ Đức. Laptop Dell/HP bán tốt, khu trưng bày Smart Device đông khách. Kho mỗi cửa hàng vẫn dùng router dân dụng, wifi chập chờn giờ cao điểm."
- **Giá trị:** Thông tin thực địa trở thành dữ liệu: nhu cầu thiết bị mạng của Sao Việt được phát hiện ngay từ chuyến thăm cửa hàng.
- **Nút hành động:** Tiếp

#### Bước 6 · Công nợ và nhãn chăm sóc
- **Ảnh:** `05_sales_account_saoviet_tong_quan.jpg` (Account Chuỗi Điện máy Sao Việt: tổng quan, nhật ký thị sát)
- **Mô tả:** "Công nợ hiện tại 18,78 tỷ / hạn mức 27 tỷ (≈70%). Kỳ hạn thanh toán Net 30, 6 tháng gần nhất thanh toán đúng hạn. Doanh số 12 tháng 276,4 tỷ, tăng 13,8% so cùng kỳ." Account gắn nhãn Chiến lược và Bán chéo.
- **Giá trị:** Sales nắm doanh số, công nợ, hạn mức trước khi gặp khách, tư vấn đúng mức và tránh đơn bị chặn.
- **Nút hành động:** Tiếp

#### Bước 7 · Trường dữ liệu 12/12
- **Ảnh:** `06_sales_account_saoviet_truong_du_lieu.jpg` (Sao Việt: ngành đang mua, ngành chưa khai thác, hạn mức, doanh số 12 tháng)
- **Mô tả:** Mã đại lý SFD-N0001, Key Account, Miền Nam. Ngành hàng đang mua: Máy tính, Smart Device, Linh kiện & Ngoại vi. Chưa khai thác: Thiết bị mạng, Phần mềm & Cloud, Giải pháp CNTT. Sức khoẻ Account: Ổn định.
- **Giá trị:** Thấy rõ đại lý đã mua và chưa mua ngành hàng nào. Đây là đầu vào trực tiếp cho up-sell, cross-sell.
- **Nút hành động:** Tiếp

#### Bước 8 · Tổng quan hoạt động
- **Ảnh:** `06_sales_account_saoviet_truong_du_lieu.jpg` (Sao Việt: ngành đang mua, ngành chưa khai thác, hạn mức, doanh số 12 tháng)
- **Mô tả:** Base tự đếm tương tác theo loại: 2 ghi chú, chưa có email, cuộc họp, cuộc gọi. Phân tích: giá trị vòng đời ước tính ₫276.427.000.000, 1 thương vụ đang mở, 3 liên hệ.
- **Giá trị:** Quản lý đo được mức độ chăm sóc thực tế trên từng account thay vì đánh giá cảm tính.
- **Nút hành động:** Mở thương vụ bán chéo của Sao Việt

#### Bước 9 · Deal bán chéo: Mở ngành Thiết bị mạng Cisco
- **Ảnh:** `07_sales_deal_saoviet_chi_tiet.jpg` (Deal Sao Việt mở ngành Thiết bị mạng Cisco: ghi chú AI, task, báo giá SFO-0001)
- **Mô tả:** ₫10.800.000.000, giai đoạn Phát hiện cơ hội, xác suất 15%. Kế hoạch 2 công việc: "Hẹn chủ chuỗi giới thiệu Cisco SMB Partner Q4" (Ngày mai) và "Gửi báo giá trial Cisco SMB cho 5 cửa hàng" (Tue, Oct 20).
- **Giá trị:** Khoảng trống ngành hàng trở thành thương vụ có giá trị, giai đoạn và kế hoạch, nên tỷ lệ bán chéo đo được.
- **Nút hành động:** Tiếp

#### Bước 10 · Báo giá ngay trong dòng công việc
- **Ảnh:** `07_sales_deal_saoviet_chi_tiet.jpg` (Deal Sao Việt mở ngành Thiết bị mạng Cisco: ghi chú AI, task, báo giá SFO-0001)
- **Mô tả:** Báo giá SFO-0001 "Báo giá trial Cisco SMB cho 5 cửa hàng Sao Việt" ₫204.500.000, hết hạn Nov 14, 2026. Ghi chú gốc của cơ hội: "AI phát hiện: Sao Việt mua Máy tính đều 12 tháng nhưng chưa phát sinh PO Thiết bị mạng."
- **Giá trị:** Báo giá gắn liền với cơ hội và lịch sử chăm sóc, khách hỏi lại thì Sales tra một chỗ là đủ.
- **Nút hành động:** Tiếp

#### Bước 11 · Vận hành thông minh
- **Ảnh:** `07_sales_deal_saoviet_chi_tiet.jpg` (Deal Sao Việt mở ngành Thiết bị mạng Cisco: ghi chú AI, task, báo giá SFO-0001)
- **Mô tả:** Deal có nhóm Quy trình tự động, Sequence, SLA, Luồng agent. Trường tuỳ chỉnh ghi nguồn cơ hội "AI gợi ý từ dữ liệu PO", sản lượng 1.800.000.000/tháng.
- **Giá trị:** Quy trình tự động, SLA và nguồn cơ hội gắn sẵn trên deal, giúp đo hiệu quả của từng nguồn up-sell.
- **Nút hành động:** Bấm biểu tượng Copilot để hỏi AI  _(có điểm bấm trên ảnh)_

#### Bước 12 · Copilot đang tra cứu
- **Ảnh:** `08_sales_deal_saoviet_copilot_dang_nghi.jpg` (Copilot đang tra cứu deal, công ty, liên hệ, hoạt động)
- **Mô tả:** Câu hỏi: "Tóm tắt deal và 3 việc cần làm". Copilot lần lượt tra thương vụ, 4 hoạt động gần nhất, 2 công việc, 0 việc cần làm, công ty Chuỗi Điện máy Sao Việt, liên hệ Ngô Quốc Quân.
- **Giá trị:** Copilot tự đọc toàn bộ ngữ cảnh của deal, Sales không phải tự lục lại lịch sử.
- **Nút hành động:** Tiếp

#### Bước 13 · Copilot tóm tắt deal
- **Ảnh:** `09_sales_deal_saoviet_copilot_tom_tat.jpg` (Copilot tóm tắt deal)
- **Mô tả:** Sau 18 giây: khách hàng hiện hữu mua máy tính đều 12 tháng; 34 cửa hàng dùng router dân dụng; CNTT đồng ý chạy thử 5 cửa hàng; Kế toán đề nghị kỳ hạn Net 30.
- **Giá trị:** Trong chưa đầy 20 giây, Sales hoặc người tiếp quản account nắm được toàn cảnh khách hàng.
- **Nút hành động:** Tiếp

#### Bước 14 · 3 việc cần làm
- **Ảnh:** `10_sales_deal_saoviet_copilot_3_viec.jpg` (Copilot đề xuất 3 việc cần làm và câu hỏi gợi ý)
- **Mô tả:** 1) Phê duyệt chính sách công nợ Net 30 cho ngành hàng Cisco. 2) Chốt kế hoạch và tiêu chí PoC/Trial cho 5 cửa hàng. 3) Gửi báo giá trial và sắp xếp buổi demo 3 bên FPT Synnex – Cisco – Sao Việt. Kèm 3 câu hỏi gợi ý tiếp.
- **Giá trị:** Từ dữ liệu đến hành động: Sales biết ngay bước tiếp theo để chốt cơ hội bán chéo.
- **Nút hành động:** Xem lại từ đầu

### Slide 7 · Use case 2 · Quy trình bán hàng B2G (demo 12 bước)
- **Dòng trên:** Theo giai đoạn · theo team dự án · AI phân tích
- **Tiêu đề:** Mỗi deal B2G có *giai đoạn, team và kế hoạch rõ ràng* từ lead đến closing

#### Bước 1 · Pipeline Dự án B2G & Enterprise
- **Ảnh:** `02_sales_pipeline_du_an_B2G.jpg` (Kanban Dự án B2G và Enterprise: 18 deal, 193,9 tỷ)
- **Mô tả:** 18 thương vụ · Tổng ₫193.900.000.000 · Dự kiến ₫91.545.000.000 (giá trị nhân xác suất từng giai đoạn).
- **Giá trị:** Ban lãnh đạo thấy ngay quy mô pipeline dự án và doanh thu dự kiến theo xác suất, phục vụ dự báo.
- **Nút hành động:** Tiếp

#### Bước 2 · 5 giai đoạn bán hàng B2G
- **Ảnh:** `02_sales_pipeline_du_an_B2G.jpg` (Kanban Dự án B2G và Enterprise: 18 deal, 193,9 tỷ)
- **Mô tả:** Lead dự án 3 deal · Khảo sát & Tư vấn 4 · Đăng ký Deal Hãng 3 · Báo giá & Hồ sơ thầu 5 · Đàm phán HĐ 3 bên 3. Mỗi cột hiện tổng giá trị và % của pipeline.
- **Giá trị:** Quy trình B2G chuẩn hoá thành 5 giai đoạn từ lead đến đàm phán HĐ 3 bên, biết ngay deal đang nghẽn ở đâu.
- **Nút hành động:** Tiếp

#### Bước 3 · SLA và kiểm soát dữ liệu
- **Ảnh:** `02_sales_pipeline_du_an_B2G.jpg` (Kanban Dự án B2G và Enterprise: 18 deal, 193,9 tỷ)
- **Mô tả:** Ngay trên pipeline: SLA theo giai đoạn, Trùng lặp, Lịch sử nhập & xuất, Sửa pipeline, Cài đặt.
- **Giá trị:** SLA theo giai đoạn cảnh báo deal nằm quá lâu một chỗ; kiểm soát trùng lặp giữ dữ liệu sạch.
- **Nút hành động:** Tiếp

#### Bước 4 · Deal chủ lực ở cột Báo giá & Hồ sơ thầu
- **Ảnh:** `02_sales_pipeline_du_an_B2G.jpg` (Kanban Dự án B2G và Enterprise: 18 deal, 193,9 tỷ)
- **Mô tả:** Ban QLDA Chuyển đổi số tỉnh Đông Hải – Trung tâm IOC tỉnh giai đoạn 2, ₫42.000.000.000.
- **Giá trị:** Deal chủ lực được nhận diện ngay trên kanban để tập trung nguồn lực.
- **Nút hành động:** Bấm thẻ deal IOC  _(có điểm bấm trên ảnh)_

#### Bước 5 · Bán hàng theo giai đoạn
- **Ảnh:** `11_sales_deal_IOC_chu_luc_qua_han.jpg` (Deal IOC 42 tỷ: task quá hạn, thảo luận @Trưởng kênh)
- **Mô tả:** Deal đã qua Lead dự án, Khảo sát & Tư vấn, Đăng ký Deal Hãng và đang ở Báo giá & Hồ sơ thầu (4/5), xác suất 60%. SLA giai đoạn: Đúng tiến độ · 0 trên 1 ngày.
- **Giá trị:** Cả team biết chính xác deal đang ở bước nào và còn trong SLA hay không.
- **Nút hành động:** Tiếp

#### Bước 6 · Kế hoạch làm việc của deal
- **Ảnh:** `11_sales_deal_IOC_chu_luc_qua_han.jpg` (Deal IOC 42 tỷ: task quá hạn, thảo luận @Trưởng kênh)
- **Mô tả:** "Gửi tờ trình giá đặc biệt cho Dell" đang quá hạn 1 ngày. "Hoàn thiện hồ sơ năng lực" hạn hôm nay. Đã xong 0/2.
- **Giá trị:** Việc nào chậm hiện cảnh báo quá hạn, được xử lý trước khi ảnh hưởng tiến độ thầu.
- **Nút hành động:** Tiếp

#### Bước 7 · Trường tuỳ chỉnh của deal B2G
- **Ảnh:** `11_sales_deal_IOC_chu_luc_qua_han.jpg` (Deal IOC 42 tỷ: task quá hạn, thảo luận @Trưởng kênh)
- **Mô tả:** Hãng chính Dell · SI: Công ty CP Giải pháp Tích hợp Thăng Long Tech · Nguồn vốn Ngân sách nhà nước · Tình trạng bảo vệ dự án: Đã được bảo vệ · Giá đặc biệt: Đang chờ duyệt · Bước tiếp theo: Hoàn thiện hồ sơ năng lực và bảo lãnh dự thầu.
- **Giá trị:** Thông tin đặc thù B2G (Hãng, SI, nguồn vốn, bảo vệ dự án, giá đặc biệt) thành trường dữ liệu để lọc và báo cáo.
- **Nút hành động:** Tiếp

#### Bước 8 · Team dự án trên deal
- **Ảnh:** `11_sales_deal_IOC_chu_luc_qua_han.jpg` (Deal IOC 42 tỷ: task quá hạn, thảo luận @Trưởng kênh)
- **Mô tả:** Chủ sở hữu và đội ngũ: chủ sở hữu, người cộng tác, người theo dõi. Thảo luận: "@Trưởng kênh cần anh/chị hỗ trợ đẩy Dell duyệt giá tuần này."
- **Giá trị:** Team dự án nhiều bên phối hợp ngay trên deal, tag đúng người cần hỗ trợ thay vì email rời rạc.
- **Nút hành động:** Tiếp

#### Bước 9 · Dòng công việc của deal
- **Ảnh:** `11_sales_deal_IOC_chu_luc_qua_han.jpg` (Deal IOC 42 tỷ: task quá hạn, thảo luận @Trưởng kênh)
- **Mô tả:** Họp với Trưởng ban QLDA về hồ sơ mời thầu và yêu cầu bảo hành 5 năm; Thăng Long Tech đề nghị hỗ trợ bảo lãnh dự thầu 2%; ghi chú deal chủ lực chờ Dell duyệt giá.
- **Giá trị:** Toàn bộ quá trình chăm sóc và chốt deal được lưu vết, phục vụ review và bàn giao.
- **Nút hành động:** Bấm Báo cáo  _(có điểm bấm trên ảnh)_

#### Bước 10 · Dashboard Tổng quan kinh doanh
- **Ảnh:** `12_sales_dashboard_tong_quan.jpg` (Dashboard Tổng quan kinh doanh)
- **Mô tả:** 18 Deals · 193,900,000,000 Deal value. Phễu dự án theo giai đoạn: Báo giá & Hồ sơ thầu 5, Khảo sát & Tư vấn 4, Lead dự án 3, Đăng ký Deal Hãng 3, Đàm phán HĐ 3 bên 3.
- **Giá trị:** Dashboard chạy trên dữ liệu thật, không cần tổng hợp báo cáo thủ công cuối tuần.
- **Nút hành động:** Tiếp

#### Bước 11 · Biểu đồ bán chéo
- **Ảnh:** `12_sales_dashboard_tong_quan.jpg` (Dashboard Tổng quan kinh doanh)
- **Mô tả:** Cơ hội bán chéo theo nhân viên và theo nguồn: AI gợi ý từ dữ liệu PO, Chương trình của Hãng, Sales phát hiện khi thăm, Đại lý hỏi qua Zalo OA.
- **Giá trị:** Biết cơ hội bán chéo đến từ nguồn nào và ai đang nắm, để nhân rộng nguồn hiệu quả.
- **Nút hành động:** Bấm Phân tích AI  _(có điểm bấm trên ảnh)_

#### Bước 12 · Phân tích AI đọc dashboard
- **Ảnh:** `13_sales_dashboard_phan_tich_AI.jpg` (Panel Phân tích AI đọc dashboard)
- **Mô tả:** Bản dịch: "Tổng giá trị pipeline đạt 193,9 tỷ trên 18 deal, một chủ sở hữu nắm 70,8 tỷ cơ hội bán chéo." · Một Sales duy nhất nắm 70,8 tỷ bán chéo · 18 deal trải 5 giai đoạn, giai đoạn lớn nhất 5 deal · 12 deal bán chéo thuộc 4 nguồn, lớn nhất 5, nhỏ nhất 1.
- **Giá trị:** AI đọc số và chỉ ra điểm cần chú ý, ví dụ rủi ro cơ hội dồn vào một Sales.
- **Nút hành động:** Xem lại từ đầu

### Slide 8 · Use case 3 · AI chat tự động cho SMEs GTM (demo 14 bước)
- **Dòng trên:** AI chăm sóc · phân về Sales · kịch bản nuôi dưỡng
- **Tiêu đề:** Đại lý SME được *chăm sóc 24/7*, cơ hội lớn về tay Sales trong 4 giờ

#### Bước 1 · Folder Kinh doanh Kênh Đại lý
- **Ảnh:** `14_agenthub_folder_kenh_dai_ly.jpg` (AgentHub: folder Kinh doanh Kênh Đại lý với 2 agent)
- **Mô tả:** 2 trợ lý trên AgentHub: Trợ lý Chăm sóc Đại lý SME (trả lời đại lý 24/7, chuyển cơ hội lớn cho Sales trong 4 giờ) và Trợ lý Điều phối Chăm sóc SME (cho Trưởng kênh).
- **Giá trị:** Đại lý SME chưa có người phụ trách vẫn được chăm sóc 24/7, giảm workload cho đội Sales.
- **Nút hành động:** Bấm Chat của Trợ lý Chăm sóc Đại lý SME  _(có điểm bấm trên ảnh)_

#### Bước 2 · Màn hình chào
- **Ảnh:** `15_agenthub_agent1_man_hinh_chao.jpg` (Màn hình chào Trợ lý Chăm sóc Đại lý SME)
- **Mô tả:** "Chào anh/chị, em là trợ lý chăm sóc đại lý Synnex FPT. Anh/chị cần hỏi về chính sách, công nợ, đặt hàng hay bảo hành ạ?" · Trả lời 24/7 · Chuyển nhân viên kinh doanh trong 4 giờ.
- **Giá trị:** Đại lý có một điểm hỏi duy nhất cho chính sách, công nợ, đặt hàng và bảo hành.
- **Nút hành động:** Bấm câu gợi ý Thưởng mở ngành mới  _(có điểm bấm trên ảnh)_

#### Bước 3 · Câu 1 · Thưởng mở ngành mới
- **Ảnh:** `16_agenthub_agent1_hoi1_thuong_mo_nganh.jpg` (Hỏi thưởng mở ngành: 2,4 triệu + 0,6 triệu, quà Wifi Cisco)
- **Mô tả:** Đơn đầu 60 triệu Thiết bị mạng: chiết khấu 4% = 2.400.000đ + thưởng mở ngành 1% = 600.000đ, tổng 3.000.000đ, căn cứ SFD-CS-01.
- **Giá trị:** Câu trả lời có tính toán cụ thể và trích số chính sách, đại lý tin tưởng, Sales không phải trả lời lặp lại.
- **Nút hành động:** Tiếp

#### Bước 4 · Cộng dồn chương trình Hãng
- **Ảnh:** `16_agenthub_agent1_hoi1_thuong_mo_nganh.jpg` (Hỏi thưởng mở ngành: 2,4 triệu + 0,6 triệu, quà Wifi Cisco)
- **Mô tả:** Hàng Cisco từ 30 triệu được tặng 1 bộ phát Wifi văn phòng và 1 buổi đào tạo (SFD-CS-06); từ 20 triệu miễn phí giao, Quảng Ngãi 48–72 giờ (SFD-CS-03). Trợ lý hỏi lại hãng và thời điểm nhập.
- **Giá trị:** AI chủ động cộng dồn ưu đãi của Hãng, tăng khả năng chốt đơn mở ngành mới.
- **Nút hành động:** Bấm câu 2 ở thanh bên phải  _(có điểm bấm trên ảnh)_

#### Bước 5 · Câu 2 · Hạn mức và công nợ
- **Ảnh:** `17_agenthub_agent1_hoi2_han_muc_cong_no.jpg` (Hạn mức và công nợ: vượt 150 triệu, Phiếu chuyển Sales B2)
- **Mô tả:** Trợ lý chạy 2 phép tính: 700 triệu + 450 triệu = 1,15 tỷ, vượt hạn mức 1 tỷ đúng 150 triệu (SFD-CS-02). Hai hướng: thanh toán bớt 150 triệu, hoặc xin tăng hạn mức tạm thời tối đa 30% = 300 triệu.
- **Giá trị:** Đại lý biết ngay tình trạng hạn mức và cách xử lý, tránh đặt hàng rồi bị chặn.
- **Nút hành động:** Tiếp

#### Bước 6 · Phiếu chuyển Sales B2
- **Ảnh:** `17_agenthub_agent1_hoi2_han_muc_cong_no.jpg` (Hạn mức và công nợ: vượt 150 triệu, Phiếu chuyển Sales B2)
- **Mô tả:** Trợ lý không tự duyệt hạn mức, lập PHIẾU CHUYỂN SALES: nhu cầu nhập hàng Tết 450 triệu, điểm B2 (đơn 100–500 triệu, cần trong 30 ngày), hạn xử lý 4 giờ làm việc.
- **Giá trị:** AI không vượt quyền: việc cần duyệt được chuyển cho Sales kèm đủ thông tin và hạn xử lý.
- **Nút hành động:** Bấm câu 3  _(có điểm bấm trên ảnh)_

#### Bước 7 · Câu 3 · Báo giá 50 Dell Vostro
- **Ảnh:** `18_agenthub_agent1_hoi3_bao_gia_50_vostro.jpg` (Báo giá 50 Dell Vostro: 680 triệu)
- **Mô tả:** 50 × 13,6 triệu = 680 triệu (SFD-CS-04). Dell Back to School giảm thêm 3% đến 30/11. Cảnh báo 2 rủi ro: 700 triệu nợ + 680 triệu = 1,38 tỷ vượt cả mức tạm thời 1,3 tỷ; chưa xác nhận được tồn kho và ngày giao.
- **Giá trị:** Báo giá tức thì kèm cảnh báo rủi ro, đơn lớn không bị bỏ sót.
- **Nút hành động:** Tiếp

#### Bước 8 · Phiếu chuyển Sales A1
- **Ảnh:** `19_agenthub_agent1_hoi3_phieu_chuyen_sales.jpg` (Phiếu chuyển Sales điểm A1, hạn 4 giờ)
- **Mô tả:** Điểm A1: đơn trên 500 triệu và cần báo giá/giao hàng trong 7 ngày. Việc Sales cần làm: kiểm tra tồn kho 50 Vostro 14, so sánh giá dự án trường học, phối hợp xử lý vượt hạn mức. Hạn 4 giờ làm việc.
- **Giá trị:** Cơ hội lớn đến tay Sales trong 4 giờ, có điểm ưu tiên rõ ràng.
- **Nút hành động:** Bấm câu 4  _(có điểm bấm trên ảnh)_

#### Bước 9 · Câu 4 · Bảo hành Xiaomi
- **Ảnh:** `20_agenthub_agent1_hoi4_bao_hanh_xiaomi.jpg` (Bảo hành Xiaomi: còn hạn đổi mới 15 ngày)
- **Mô tả:** 10 ngày vẫn trong hạn đổi mới 15 ngày của Xiaomi (SFD-CS-05). Hướng dẫn chuẩn bị hoá đơn bán lẻ, ảnh tem, serial và tạo phiếu RMA. Trợ lý không tự kết luận lỗi.
- **Giá trị:** Hỗ trợ sau bán đúng chính sách Hãng, giảm tải cho bộ phận bảo hành.
- **Nút hành động:** Bấm câu 5  _(có điểm bấm trên ảnh)_

#### Bước 10 · Câu 5 · Xin thêm 2% chiết khấu
- **Ảnh:** `21_agenthub_agent1_hoi5_tu_choi_chiet_khau.jpg` (Từ chối xin thêm 2% chiết khấu, lập phiếu xin giá đặc biệt)
- **Mô tả:** Trợ lý từ chối lịch sự: mức ngoài SFD-CS-01 phải do Trưởng kênh Đại lý duyệt bằng văn bản. Gợi ý mức cộng dồn khoảng 6% trong chính sách và lập phiếu chuyển Sales A1 kèm đề nghị giá đặc biệt.
- **Giá trị:** Giữ biên lợi nhuận: AI bám khung chiết khấu và chuyển đề nghị ngoại lệ cho người có thẩm quyền.
- **Nút hành động:** Tiếp

#### Bước 11 · Trợ lý Điều phối Chăm sóc SME
- **Ảnh:** `22_agenthub_agent2_kichban_dau.jpg` (Trợ lý Điều phối: mở đầu kịch bản 30 ngày)
- **Mô tả:** Trưởng kênh yêu cầu: "Soạn kịch bản chăm sóc 30 ngày cho nhóm đại lý SME chưa mua thiết bị mạng". Trợ lý nêu mục tiêu, khung D0 = 20/10 → D30 = 19/11/2026, cơ sở chính sách và 2 combo 30 triệu / 51,2 triệu.
- **Giá trị:** Trưởng kênh có ngay kịch bản chăm sóc nhóm SME bám sát chính sách, chỉ cần duyệt và triển khai.
- **Nút hành động:** Tiếp

#### Bước 12 · Lịch chạm 8 mốc
- **Ảnh:** `23_agenthub_agent2_kichban_lichcham.jpg` (Lịch chăm sóc D0 đến D30 và nội dung từng mốc)
- **Mô tả:** D0 Zalo OA · D3 Email · D7 Gọi điện · D12 Zalo OA · D18 Email · D22 Gọi điện · D26 Zalo OA · D30 Gọi điện + Email, mỗi mốc có người làm và mục tiêu. Bên dưới là nội dung tin D0 (286 ký tự).
- **Giá trị:** Chăm sóc SME thành lịch chạm đều đặn trên nhiều kênh, không phụ thuộc trí nhớ của từng người.
- **Nút hành động:** Tiếp

#### Bước 13 · Email D3 và khung gọi D7
- **Ảnh:** `24_agenthub_agent2_kichban_email.jpg` (Email D3: combo thiết bị mạng)
- **Mô tả:** Email combo thiết bị mạng: 4% chiết khấu, tặng Wifi từ đơn 30 triệu, bảng combo A/B. Khung gọi D7 5–7 phút với 3 câu hỏi dò nhu cầu bắt buộc và cách xử lý từ chối.
- **Giá trị:** Nội dung soạn sẵn đúng chính sách, Sales chỉ cần gửi và gọi theo khung.
- **Nút hành động:** Tiếp

#### Bước 14 · Chốt D26, D30 và lưu ý triển khai
- **Ảnh:** `25_agenthub_agent2_kichban_cuoi.jpg` (Phần cuối kịch bản và đo lường)
- **Mô tả:** D26 Zalo nhắc hạn (265 ký tự); D30 gọi chốt một trong ba kết quả. Lưu ý: tin dưới 400 ký tự, không tự thêm chiết khấu, nội dung là bản nháp để Trưởng kênh duyệt.
- **Giá trị:** Mọi nội dung là bản nháp chờ duyệt, Synnex FPT giữ quyền kiểm soát thông điệp.
- **Nút hành động:** Xem lại từ đầu

### Slide 9 · Use case 4 · Chat đa kênh và AI tư vấn (demo 13 bước)
- **Dòng trên:** Hộp thư · AI trả lời · chuyển Sales · AI ghi dữ liệu · Sales hỏi AI
- **Tiêu đề:** Mọi hội thoại về một nơi, *AI trả lời và tự ghi hồ sơ*, Sales vào đúng lúc

#### Bước 1 · Hộp thư hội thoại
- **Ảnh:** `31_inbox_hoi_thoai_copilot.jpg` (Hộp thư: hội thoại Trần Thị Ngọc Ánh, AI chuyển giao Sales, Copilot hỏi về hội thoại)
- **Mô tả:** Mọi hội thoại của khách về một hộp thư, lọc theo Tất cả / Mới / Cần trả lời / Đang chờ. Mỗi hội thoại hiện tin nhắn cuối, thời gian, trạng thái Đang chờ và nhãn như Giới thiệu, Nhóm.
- **Giá trị:** Mọi hội thoại với đại lý và khách về một hộp thư; quản lý thấy được ai đang chờ trả lời.
- **Nút hành động:** Bấm hội thoại Đặng Minh Khoa  _(có điểm bấm trên ảnh)_

#### Bước 2 · AI chào và hỏi nhu cầu
- **Ảnh:** `34_inbox_hoi_thoai_dang_minh_khoa.jpg` (Hội thoại Đặng Minh Khoa: AI hỏi nhu cầu, ghi hồ sơ, nguồn và phân công)
- **Mô tả:** Trợ lý mở lời: "Synnex FPT xin chào! Doanh nghiệp anh/chị đang cần trang bị laptop, máy chủ, thiết bị mạng hay phần mềm bản quyền ạ?" Khách để lại họ tên Đặng Minh Khoa, số điện thoại 0912738054, doanh nghiệp Công ty Luật TNHH Trí Việt.
- **Giá trị:** AI tiếp khách ngay lập tức, kể cả ngoài giờ, và lấy thông tin liên hệ ngay từ đầu.
- **Nút hành động:** Tiếp

#### Bước 3 · AI tự ghi nhận thông tin vào hồ sơ
- **Ảnh:** `34_inbox_hoi_thoai_dang_minh_khoa.jpg` (Hội thoại Đặng Minh Khoa: AI hỏi nhu cầu, ghi hồ sơ, nguồn và phân công)
- **Mô tả:** "Trợ lý tư vấn SME - Synnex FPT đã cập nhật hồ sơ: Tên doanh nghiệp từ — đến Công ty Luật TNHH Trí Việt", rồi chào anh Khoa và hỏi tiếp nhu cầu thiết bị, phần mềm và số lượng máy.
- **Giá trị:** Thông tin khách tự thành dữ liệu CRM, Sales không phải nhập lại.
- **Nút hành động:** Tiếp

#### Bước 4 · Khách hỏi bằng ngôn ngữ tự nhiên
- **Ảnh:** `34_inbox_hoi_thoai_dang_minh_khoa.jpg` (Hội thoại Đặng Minh Khoa: AI hỏi nhu cầu, ghi hồ sơ, nguồn và phân công)
- **Mô tả:** "Cho mình hỏi giá Microsoft 365 Business Standard. Văn phòng mình 8 người, muốn chuyển hết sang bản quyền cả Windows".
- **Giá trị:** Khách hỏi tự nhiên như nói chuyện với người, không cần menu hay biểu mẫu.
- **Nút hành động:** Tiếp

#### Bước 5 · Thông tin hội thoại và nguồn
- **Ảnh:** `34_inbox_hoi_thoai_dang_minh_khoa.jpg` (Hội thoại Đặng Minh Khoa: AI hỏi nhu cầu, ghi hồ sơ, nguồn và phân công)
- **Mô tả:** Trạng thái Mở · Đang chờ; nhà cung cấp Live Chat - Bán hàng; dịch vụ [Synnex FPT] Tư vấn thiết bị CNTT cho doanh nghiệp SME; tạo ngày Oct 15, 2026. Nguồn: vị trí Hanoi, Vietnam, khách đến từ trang prospect.base.com.vn.
- **Giá trị:** Biết khách đến từ kênh, trang và dịch vụ nào để đánh giá hiệu quả từng kênh.
- **Nút hành động:** Tiếp

#### Bước 6 · AI đang xử lý, chưa cần gán Sales
- **Ảnh:** `34_inbox_hoi_thoai_dang_minh_khoa.jpg` (Hội thoại Đặng Minh Khoa: AI hỏi nhu cầu, ghi hồ sơ, nguồn và phân công)
- **Mô tả:** Phân công cho: chưa gán người; Trợ lý tư vấn SME - Synnex FPT (gemini-3.8-flash) đang trả lời. Nhãn hội thoại: Phần mềm bản quyền, AI đã xử lý.
- **Giá trị:** Câu hỏi phổ biến được AI xử lý trọn vẹn, Sales chỉ tham gia khi thật sự cần.
- **Nút hành động:** Bấm hội thoại Trần Thị Ngọc Ánh  _(có điểm bấm trên ảnh)_

#### Bước 7 · Kịch bản AI kết hợp Sales
- **Ảnh:** `31_inbox_hoi_thoai_copilot.jpg` (Hộp thư: hội thoại Trần Thị Ngọc Ánh, AI chuyển giao Sales, Copilot hỏi về hội thoại)
- **Mô tả:** Khách báo laptop Dell Latitude 3450 mua tháng 6 bị liệt mấy phím, serial 7HKQ3Z3. Trợ lý cập nhật Nhóm sản phẩm quan tâm → Laptop doanh nghiệp, Tóm tắt nhu cầu → Khách báo bảo hành máy Dell Latitude 34…, rồi chuyển giao cho Nhung Vũ Thị.
- **Giá trị:** AI và Sales phối hợp trong cùng một hội thoại: AI thu thập, Sales tiếp nhận khi khách có nhu cầu.
- **Nút hành động:** Tiếp

#### Bước 8 · Trả lời và chuyển người phụ trách
- **Ảnh:** `31_inbox_hoi_thoai_copilot.jpg` (Hộp thư: hội thoại Trần Thị Ngọc Ánh, AI chuyển giao Sales, Copilot hỏi về hội thoại)
- **Mô tả:** "Dạ dòng Dell Latitude 3450 có chính sách bảo hành 36 tháng tận nơi (onsite) chính hãng ạ." Trợ lý ghi nhận serial và chuyển chị Nhung Vũ Thị phụ trách bảo hành. Long Nguyễn thêm nhãn Bảo hành - kỹ thuật và Laptop doanh nghiệp.
- **Giá trị:** Khách được trả lời ngay và chuyển đúng người phụ trách, không phải kể lại từ đầu.
- **Nút hành động:** Tiếp

#### Bước 9 · Dữ liệu AI ghi vào hệ thống
- **Ảnh:** `32_inbox_truong_tuy_chinh_ai_ghi_nhan.jpg` (Trường tuỳ chỉnh và hồ sơ KH tiềm năng do AI ghi nhận)
- **Mô tả:** Trường tuỳ chỉnh do trợ lý điền: Tên doanh nghiệp Công ty CP May Thành Đạt · Nhóm sản phẩm quan tâm Laptop doanh nghiệp · Tóm tắt nhu cầu "Khách báo bảo hành máy Dell Latitude 3450 serial 7HKQ3Z3 bị liệt phím" · Đã gửi báo giá NO. Các trường chờ bổ sung: Mã số thuế, Số lượng, Ngân sách, Thời gian cần hàng, Mức độ tiềm năng, Mã báo giá, Tỉnh/Thành giao hàng.
- **Giá trị:** Dữ liệu khách hàng được làm giàu sau mỗi hội thoại, phục vụ phân loại và chăm sóc tiếp.
- **Nút hành động:** Tiếp

#### Bước 10 · Hồ sơ khách hàng tiềm năng
- **Ảnh:** `32_inbox_truong_tuy_chinh_ai_ghi_nhan.jpg` (Trường tuỳ chỉnh và hồ sơ KH tiềm năng do AI ghi nhận)
- **Mô tả:** KH tiềm năng Trần Thị Ngọc Ánh, số điện thoại +84 973-609-128 (Live Chat - Bán hàng · Chính), chưa có địa chỉ email, công ty Công ty CP May Thành Đạt.
- **Giá trị:** Hồ sơ khách tiềm năng tạo tự động từ hội thoại, lead không thất thoát.
- **Nút hành động:** Tiếp

#### Bước 11 · Sales hỏi đáp AI về hội thoại
- **Ảnh:** `31_inbox_hoi_thoai_copilot.jpg` (Hộp thư: hội thoại Trần Thị Ngọc Ánh, AI chuyển giao Sales, Copilot hỏi về hội thoại)
- **Mô tả:** Copilot "Hỏi về hội thoại này": hỏi bất cứ điều gì về khách, hoặc nhờ Copilot soạn sẵn câu trả lời từ kho tri thức; gửi gì là do Sales quyết định. Gợi ý: Tóm tắt nhanh hội thoại này · Khách còn câu hỏi nào chưa được trả lời không? · Nên nhắn gì để giữ liên lạc?
- **Giá trị:** Sales hỏi AI để nắm nhanh hội thoại và soạn phản hồi; quyết định gửi vẫn thuộc về Sales.
- **Nút hành động:** Tiếp

#### Bước 12 · Cấu hình Trợ lý tư vấn SME
- **Ảnh:** `33_inbox_cai_dat_tro_ly_ai.jpg` (Cài đặt Trợ lý tư vấn SME - Synnex FPT)
- **Mô tả:** Trợ lý tổng quát: trả lời và điều hướng, sẵn sàng khi đã có quy tắc chuyển giao và một công cụ. Mặc định cho dịch vụ [Synnex FPT] Tư vấn thiết bị CNTT cho doanh nghiệp SME (1 hộp thư trả lời bằng trợ lý). Nhà cung cấp Gemini, mô hình gemini-3.8-flash.
- **Giá trị:** Trợ lý cấu hình theo từng dịch vụ và hộp thư, triển khai nhanh cho nhiều kênh.
- **Nút hành động:** Tiếp

#### Bước 13 · Mức sẵn sàng 100%
- **Ảnh:** `33_inbox_cai_dat_tro_ly_ai.jpg` (Cài đặt Trợ lý tư vấn SME - Synnex FPT)
- **Mô tả:** Thiết lập Chung, Hướng dẫn, Nâng cao; lĩnh vực Commerce, các lĩnh vực Chăm sóc khách hàng, Bán hàng, Công việc, Tuyển dụng ghi Sắp có. Checklist: đã có danh tính và mô hình, đã viết hướng dẫn, đã đặt quy tắc chuyển giao, đã bật ít nhất một công cụ.
- **Giá trị:** Checklist sẵn sàng giúp triển khai có kiểm soát trước khi AI tiếp khách thật.
- **Nút hành động:** Xem lại từ đầu

### Slide 10 · Quản trị AI (demo 5 bước)
- **Dòng trên:** Cấu hình · kỹ năng · đo lường
- **Tiêu đề:** AI làm theo *chính sách của Synnex FPT*, có giới hạn và đo được chất lượng

#### Bước 1 · Cấu hình Trợ lý Chăm sóc Đại lý SME
- **Ảnh:** `26_agenthub_agent1_cau_hinh.jpg` (Cấu hình agent: model, instruction, skill, tool group)
- **Mô tả:** Model claude-opus-5 · Instruction mô tả vai trò, việc được làm, giới hạn · Skill "Chấm điểm tín hiệu mua" · Tool group "Tính toán chính sách".
- **Giá trị:** Synnex FPT tự định nghĩa vai trò, giới hạn và công cụ của AI.
- **Nút hành động:** Tiếp

#### Bước 2 · Sơ đồ luồng của agent
- **Ảnh:** `27_agenthub_agent1_map_luong.jpg` (Sơ đồ luồng agent: Chat input → Memory + Skill → Agent → Reply)
- **Mô tả:** Chat input → Memory và skill Chấm điểm tín hiệu mua → Agent (claude-opus-5, Toolsets 1 attached, Skills 1 enabled, 3 starters) → Reply.
- **Giá trị:** Luồng xử lý minh bạch, kiểm tra được AI dùng dữ liệu và kỹ năng nào.
- **Nút hành động:** Tiếp

#### Bước 3 · Skill Chấm điểm tín hiệu mua và chuyển Sales
- **Ảnh:** `28_agenthub_skill_cham_diem_tin_hieu_mua.jpg` (Kỹ năng chấm điểm A1–D4 và quy tắc lập phiếu)
- **Mô tả:** Trục chữ theo giá trị đơn: A từ 500 triệu, B 100–500, C 30–100, D dưới 30. Trục số theo mức khẩn: 1 trong 7 ngày, 2 trong 30 ngày, 3 trong quý, 4 chưa có thời điểm. A1, A2, B1, B2: lập phiếu ngay, hạn 4 giờ.
- **Giá trị:** Quy tắc ưu tiên cơ hội do Synnex FPT đặt ra được AI áp dụng nhất quán cho mọi đại lý.
- **Nút hành động:** Tiếp

#### Bước 4 · Monitoring 30 ngày
- **Ảnh:** `29_agenthub_agent1_monitoring.jpg` (Monitoring: 100% Helpful, 100% tool success, 17 giây)
- **Mô tả:** 5 tin nhắn · 1 cuộc trò chuyện · 10,1k token · 17s phản hồi trung bình · 100% Helpful (5/5) · 100% Tool success (6 bước) · 76,2% prompt cache · 0% lỗi.
- **Giá trị:** Chất lượng AI đo bằng số liệu: tỷ lệ hữu ích, độ trễ, lỗi, chi phí token.
- **Nút hành động:** Tiếp

#### Bước 5 · Logs từng câu hỏi
- **Ảnh:** `30_agenthub_agent1_logs.jpg` (Logs 5 câu hỏi, đều được đánh giá tốt)
- **Mô tả:** 5 câu hỏi của đại lý, model claude-opus-5, nguồn CONSOLE, cả 5 đều được đánh giá tốt, có token và độ trễ từng lượt.
- **Giá trị:** Mọi câu trả lời được lưu lại để kiểm tra, đánh giá và cải tiến.
- **Nút hành động:** Xem lại từ đầu

### Slide 11 · 05 Bước tiếp theo
- **Tiêu đề:** Đề xuất showcase trên quy trình vận hành hiện tại của Synnex FPT
- **Bước 1 · Khảo sát:** Làm việc với kinh doanh kênh Đại lý, kênh Dự án và IT · Chọn một số quy trình vận hành đang chạy để showcase
- **Bước 2 · Xin dữ liệu:** Danh sách account, ngành hàng, doanh số và công nợ mẫu · Chính sách kênh đại lý và một vài deal dự án đã ẩn danh
- **Bước 3 · Chạy thử demo:** Dựng các quy trình đã chọn trên tenant với dữ liệu của Synnex FPT · Cùng đội kinh doanh chạy thử, so với cách làm hiện tại và ghi nhận phản hồi
- **Câu chốt:** Synnex FPT đã có hệ thống quản lý PO. Mảnh còn thiếu là lớp vận hành phía trước: ghi lại mọi tương tác với đại lý, biến khoảng trống ngành hàng thành cơ hội, và để AI gánh phần chăm sóc lặp lại.

---

## Phần C · Danh mục ảnh chụp tenant

| # | File | Nội dung |
|---|---|---|
| 01 | `01_sales_trang_chu_thuong_vu.jpg` | Trang chủ Base Sales: 31 thương vụ, 2 pipeline FPT Synnex |
| 02 | `02_sales_pipeline_du_an_B2G.jpg` | Kanban Dự án B2G và Enterprise: 18 deal, 193,9 tỷ |
| 03 | `03_sales_pipeline_ban_cheo_dai_ly.jpg` | Kanban Phát triển Đại lý và Bán chéo: 12 deal, 70,8 tỷ |
| 04 | `04_sales_danh_sach_dai_ly_khach_hang.jpg` | Danh bạ 25 đại lý và khách hàng, lọc theo phân hạng |
| 05 | `05_sales_account_saoviet_tong_quan.jpg` | Account Chuỗi Điện máy Sao Việt: tổng quan, nhật ký thị sát |
| 06 | `06_sales_account_saoviet_truong_du_lieu.jpg` | Sao Việt: ngành đang mua, ngành chưa khai thác, hạn mức, doanh số 12 tháng |
| 07 | `07_sales_deal_saoviet_chi_tiet.jpg` | Deal Sao Việt mở ngành Thiết bị mạng Cisco: ghi chú AI, task, báo giá SFO-0001 |
| 08 | `08_sales_deal_saoviet_copilot_dang_nghi.jpg` | Copilot đang tra cứu deal, công ty, liên hệ, hoạt động |
| 09 | `09_sales_deal_saoviet_copilot_tom_tat.jpg` | Copilot tóm tắt deal |
| 10 | `10_sales_deal_saoviet_copilot_3_viec.jpg` | Copilot đề xuất 3 việc cần làm và câu hỏi gợi ý |
| 11 | `11_sales_deal_IOC_chu_luc_qua_han.jpg` | Deal IOC 42 tỷ: task quá hạn, thảo luận @Trưởng kênh |
| 12 | `12_sales_dashboard_tong_quan.jpg` | Dashboard Tổng quan kinh doanh |
| 13 | `13_sales_dashboard_phan_tich_AI.jpg` | Panel Phân tích AI đọc dashboard |
| 14 | `14_agenthub_folder_kenh_dai_ly.jpg` | AgentHub: folder Kinh doanh Kênh Đại lý với 2 agent |
| 15 | `15_agenthub_agent1_man_hinh_chao.jpg` | Màn hình chào Trợ lý Chăm sóc Đại lý SME |
| 16 | `16_agenthub_agent1_hoi1_thuong_mo_nganh.jpg` | Hỏi thưởng mở ngành: 2,4 triệu + 0,6 triệu, quà Wifi Cisco |
| 17 | `17_agenthub_agent1_hoi2_han_muc_cong_no.jpg` | Hạn mức và công nợ: vượt 150 triệu, Phiếu chuyển Sales B2 |
| 18 | `18_agenthub_agent1_hoi3_bao_gia_50_vostro.jpg` | Báo giá 50 Dell Vostro: 680 triệu |
| 19 | `19_agenthub_agent1_hoi3_phieu_chuyen_sales.jpg` | Phiếu chuyển Sales điểm A1, hạn 4 giờ |
| 20 | `20_agenthub_agent1_hoi4_bao_hanh_xiaomi.jpg` | Bảo hành Xiaomi: còn hạn đổi mới 15 ngày |
| 21 | `21_agenthub_agent1_hoi5_tu_choi_chiet_khau.jpg` | Từ chối xin thêm 2% chiết khấu, lập phiếu xin giá đặc biệt |
| 22 | `22_agenthub_agent2_kichban_dau.jpg` | Trợ lý Điều phối: mở đầu kịch bản 30 ngày |
| 23 | `23_agenthub_agent2_kichban_lichcham.jpg` | Lịch chăm sóc D0 đến D30 và nội dung từng mốc |
| 24 | `24_agenthub_agent2_kichban_email.jpg` | Email D3: combo thiết bị mạng |
| 25 | `25_agenthub_agent2_kichban_cuoi.jpg` | Phần cuối kịch bản và đo lường |
| 26 | `26_agenthub_agent1_cau_hinh.jpg` | Cấu hình agent: model, instruction, skill, tool group |
| 27 | `27_agenthub_agent1_map_luong.jpg` | Sơ đồ luồng agent: Chat input → Memory + Skill → Agent → Reply |
| 28 | `28_agenthub_skill_cham_diem_tin_hieu_mua.jpg` | Kỹ năng chấm điểm A1–D4 và quy tắc lập phiếu |
| 29 | `29_agenthub_agent1_monitoring.jpg` | Monitoring: 100% Helpful, 100% tool success, 17 giây |
| 30 | `30_agenthub_agent1_logs.jpg` | Logs 5 câu hỏi, đều được đánh giá tốt |
| 31 | `31_inbox_hoi_thoai_copilot.jpg` | Hộp thư: hội thoại Trần Thị Ngọc Ánh, AI chuyển giao Sales, Copilot hỏi về hội thoại |
| 32 | `32_inbox_truong_tuy_chinh_ai_ghi_nhan.jpg` | Trường tuỳ chỉnh và hồ sơ KH tiềm năng do AI ghi nhận |
| 33 | `33_inbox_cai_dat_tro_ly_ai.jpg` | Cài đặt Trợ lý tư vấn SME - Synnex FPT |
| 34 | `34_inbox_hoi_thoai_dang_minh_khoa.jpg` | Hội thoại Đặng Minh Khoa: AI hỏi nhu cầu, ghi hồ sơ, nguồn và phân công |

**Ảnh còn thiếu** (đã gửi trong chat nhưng không lưu được ra file, cần gửi lại dạng zip):
- Kết nối kênh
- Copilot trên account Sao Việt (rule, đang nghĩ, câu trả lời)
- Copilot trên deal IOC với rule "Kiểm soát deal dự án B2G và HĐ 3 bên"
- Dashboard có biểu đồ tròn
- Copilot trả lời trên dashboard
- Kanban bản nét
- Deal IOC bản nét
- Các tab của Sao Việt (Tổng quan / Liên hệ / Thương vụ / Trường dữ liệu / tổng quan hoạt động)
