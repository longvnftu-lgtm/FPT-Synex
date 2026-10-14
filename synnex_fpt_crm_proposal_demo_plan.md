# Synnex FPT - Phân tích Nhu cầu CRM & Kịch bản Demo Solution

Tài liệu tổng hợp phân tích bài toán kinh doanh, nhu cầu ứng dụng CRM và thiết kế kịch bản Demo giải pháp cho **Synnex FPT** dựa trên cấu trúc vận hành thực tế.

---

## 📌 1. Bối cảnh & Hiện trạng Kinh doanh

Synnex FPT vận hành bộ máy kinh doanh khoảng **~300 Sales**, chia làm 2 mảng riêng biệt với mô hình quản trị hoàn toàn khác nhau:

```
                                  ┌───────────────────────────┐
                                  │   Synnex FPT (~300 Sales) │
                                  └─────────────┬─────────────┘
                                                │
                ┌───────────────────────────────┴───────────────────────────────┐
                ▼                                                               ▼
┌───────────────────────────────┐                               ┌───────────────────────────────┐
│   Mảng Đại lý (B2B Channel)   │                               │    Mảng Dự án (B2G/Enterprise)│
├───────────────────────────────┤                               ├───────────────────────────────┤
│ • Tỷ trọng: 70% Doanh thu     │                               │ • Tỷ trọng: 30% Doanh thu     │
│ • Quy mô: ~250 Sales          │                               │ • Quy mô: ~50 Sales           │
│ • Tệp KH: ~1.000 Accounts     │                               │ • Tệp KH: Bộ ban ngành, Đơn vị│
│   (TGĐĐ, FPT Shop, Chuỗi lớn) │                               │   hành chính công, Dự án lớn  │
│ • Đã có hệ thống quản lý PO   │                               │ • Mô hình: Hợp đồng 3 bên     │
└───────────────────────────────┘                               └───────────────────────────────┘
```

### Chi tiết đặc thù từng mảng:

| Tiêu chí | Mảng Đại lý (B2B Channel) | Mảng Dự án (B2G / Enterprise) |
| :--- | :--- | :--- |
| **Bản chất kinh doanh** | Bán buôn/Phân phối qua hệ thống đại lý. Đã ký hợp đồng nguyên tắc, ít phát sinh account mới. | Bán hàng dự án dài hạn, tham gia đấu thầu, chu kỳ bán kéo dài. |
| **Sản phẩm/Ngành hàng** | Thiết bị máy tính, Linh kiện/Ngoại vi, Điện thoại/Smart Device, Giải pháp CNTT. | Hạ tầng CNTT, Giải pháp tích hợp hệ thống. |
| **Hệ thống hiện có** | Đã có hệ thống quản lý PO đại lý riêng (không lên đơn trực tiếp trên CRM). | Đã có luồng quản lý Lead/Deal cơ bản nhưng chưa tối ưu. |
| **Nhu cầu chính đối với CRM** | • Quản lý & Chăm sóc Account (Account Management).<br>• Tối ưu bán chéo/bán thêm (Cross-sell/Up-sell).<br>• Quản lý lịch sử tương tác, trao đổi tập trung.<br>• Tự động hóa chăm sóc tệp đại lý SME (doanh thu nhỏ, chưa có nhân sự phụ trách). | • Quản lý Pipeline Deal từ Lead $\rightarrow$ Đấu thầu $\rightarrow$ Chốt hợp đồng.<br>• Theo dõi tiến độ chăm sóc & tỷ lệ chuyển đổi Deal. |

---

## 🎯 2. Định hướng Kịch bản Demo Giải pháp (Use Cases)

Dựa trên nhu cầu thực tế, buổi Demo giải pháp sẽ tập trung vào **3 Use Cases trọng tâm**, không đi vào luồng tạo đơn hàng (để tránh trùng lặp với hệ thống PO hiện tại).

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                                 TỔNG HOÀN KỊCH BẢN DEMO                                 │
├────────────────────────────┬────────────────────────────┬──────────────────────────────┤
│  Use Case 1: Account Mgmt  │   Use Case 2: Project Deal │  Use Case 3: Automation & AI │
│     (B2B Channel - 70%)    │      (B2G/Project - 30%)   │        (SME Accounts)        │
├────────────────────────────┼────────────────────────────┼──────────────────────────────┤
│ • Account 360 View         │ • B2G Deal Pipeline        │ • AI Chatbot Qualification   │
│ • Cross-sell Matrix        │ • Quản lý Báo giá/Hợp đồng │ • Auto-Nurturing Workflows   │
│ • Fieldwork & Activity Log │ • Cảnh báo Deal rủi ro     │ • Lead Routing sang Sales    │
│ • Integration Report (PO)  │                            │                              │
└────────────────────────────┴────────────────────────────┴──────────────────────────────┘
```

### 📋 Use Case 1: Quản trị & Phát triển Account Đại lý (B2B Channel)
> **Mục tiêu:** Tăng doanh số trên tập khách hàng hiện hữu thông qua hoạt động chăm sóc và bán chéo (Cross-sell).

* **Giao diện Account 360:**
  * Hiển thị toàn bộ thông tin đối tác, phân hạng đại lý (Key Account vs SME), đầu mối liên hệ (Contact).
  * Lưu trữ tập trung mọi tương tác: Lịch sử cuộc gọi, email, ghi chú trao đổi, nhật ký thị sát (Fieldwork Log khi sales đi thăm đại lý).
* **Ma trận Bán chéo (Cross-sell / Up-sell Matrix):**
  * Thống kê ngành hàng đại lý đã mua vs chưa mua (ví dụ: Đại lý đã mua Máy tính nhưng chưa mua Linh kiện/Thiết bị mạng).
  * Gợi ý chương trình thúc đẩy doanh số theo từng ngành hàng cho Sales.
* **Mô phỏng Báo cáo Doanh thu Tích hợp (PO System Integration):**
  * Tích hợp dữ liệu đơn hàng từ Hệ thống PO của Synnex FPT về CRM.
  * Hiển thị báo cáo Doanh số theo Account, Báo cáo hiệu suất chăm sóc của Sales mà Sales không cần thao tác nhập đơn 2 lần.

---

### 📋 Use Case 2: Quản lý Pipeline Dự án & Đấu thầu (B2G / Enterprise)
> **Mục tiêu:** Minh bạch hóa tiến độ dự án, tăng tỷ lệ thắng thầu (Win Rate).

* **Quy trình Quản lý Pipeline Chuẩn:**
  * Thiết lập các giai đoạn (Stages): `Lead` $\rightarrow$ `Khảo sát & Tư vấn` $\rightarrow$ `Báo giá / Hồ sơ Thầu` $\rightarrow$ `Đàm phán Hợp đồng 3 bên` $\rightarrow$ `Won/Lost`.
* **Quản lý Hồ sơ & Báo giá:**
  * Số hóa quy trình phê duyệt bảng giá đặc biệt (Special Price Request) cho dự án lớn.
  * Lưu trữ hợp đồng, hồ sơ thầu ngay trên từng Card Deal.
* **Cảnh báo tiến độ (Deal SLA & Warning):**
  * Tự động cảnh báo các Deal bị ngâm quá lâu tại một giai đoạn thầu để quản lý kịp thời hỗ trợ.

---

### 📋 Use Case 3: Chăm sóc Tự động & AI Chatbot cho Tệp SME
> **Mục tiêu:** Tự động hóa quy trình, giảm tải công việc cho 250 sales đối với tệp đại lý nhỏ.

* **AI Chatbot Tiếp nhận & Tư vấn:**
  * Tự động giải đáp các thắc mắc về chính sách, danh mục sản phẩm, quy trình hợp tác cho đại lý mới/SME.
* **Chăm sóc Tự động (Nurturing Automation):**
  * Thiết lập kịch bản gửi thông báo khuyến mãi, chính sách chiết khấu định kỳ qua Zalo OA / Email / SMS.
* **Chuyển đổi Cơ hội (Lead Routing):**
  * Khi AI Chatbot phát hiện đại lý SME có nhu cầu phát sinh đơn hàng lớn hoặc cần hỗ trợ trực tiếp, hệ thống tự động tạo Lead/Task phân công cho Sales chuyên trách.

---

## 🚀 3. Lộ trình Triển khai & Tích hợp Hệ thống

```
┌─────────────────────────┐      API Sync      ┌─────────────────────────┐
│   Synnex FPT PO System  │ ─────────────────> │   Base / Enterprise CRM │
│ (Quản lý Đơn/Công nợ)   │  (Doanh thu/Đơn)   │  (Quản trị tương tác)   │
└─────────────────────────┘                    └─────────────────────────┘
```

1. **Giai đoạn 1 (Khảo sát & Chuẩn hóa):**
   * Làm việc với bộ phận IT/Vận hành của Synnex FPT để khảo sát cấu trúc API của Hệ thống PO hiện tại.
   * Chuẩn hóa danh mục Master Data (Account, Ngành hàng, Sales).
2. **Giai đoạn 2 (Setup & Demo PoC):**
   * Cấu hình 2 Pipeline riêng biệt (B2B Account Management & B2G Project).
   * Xây dựng Mockup dữ liệu tích hợp báo cáo doanh thu từ PO sang CRM.
3. **Giai đoạn 3 (Đào tạo & Triển khai):**
   * Đào tạo phân quyền cho 300 Sales và cấp Quản lý.
   * Kích hoạt hệ thống AI Chatbot & Kịch bản Chăm sóc Tự động.

---

## 🛠️ 4. Checklists Chuẩn bị cho Buổi Meeting Demo

- [ ] Data mẫu sát thực tế ngành ICT (Tên các chuỗi đại lý lớn, mã ngành hàng phân phối).
- [ ] Kịch bản thao tác Fieldwork Log trên Mobile App dành cho Sales đi thị sát đại lý.
- [ ] Luồng duyệt Báo giá / Giá đặc biệt trên CRM.
- [ ] Demo tính năng AI Chatbot tương tác tự động với khách hàng.