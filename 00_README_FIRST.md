# 00 — ĐỌC TRƯỚC / README FIRST
### Kho tài liệu **[Foundation] Base 3.0 ready** — hướng dẫn dùng cho khối kinh doanh

> Cập nhật: 24/08/2026 · Phụ trách: Nghĩa Trần (nghia.tran@base.vn)
> Link kho: https://drive.google.com/drive/folders/1L9QAWGzZPenCguZ81VdxKrbuTeJx5ZxZ?usp=sharing

---

## 1. Kho này là gì

Một thư mục Drive gom **toàn bộ tài liệu nền của bộ sản phẩm Base 3.0**: 16 nhóm sản phẩm, mỗi nhóm có tới 5 lớp tài liệu.

Mục tiêu rất cụ thể: một bạn kinh doanh, không cần hỏi product, vẫn có thể **hiểu sản phẩm → nói với khách → chứng minh bằng hồ sơ → tự dựng bản demo** trong ngày.

Điểm khác biệt so với các kho tài liệu cũ: ở đây có hai loại file được thiết kế để **nạp thẳng vào Claude** chứ không phải để đọc bằng mắt — `Knowledge_*.md` và `Skill_setup_*.skill`. Nạp xong, Claude của bạn hiểu sản phẩm Base ở mức chi tiết như người đã khảo sát app, và biết tự thao tác trên tenant demo.

---

## 2. Bốn bước để dùng được ngay (lần đầu ~10 phút)

**Bước 1 — Mở thư mục sản phẩm bạn đang bán.**
Xem mục 4 bên dưới để biết thư mục nào đang có gì.

**Bước 2 — Tải hai file cốt lõi về máy.**
- `Knowledge_[App].md` — để Claude hiểu sản phẩm.
- `Skill_setup_[App].skill` — để Claude tự dựng demo.
Tải nguyên file `.skill`, **không giải nén, không đổi tên, không sửa nội dung**. (Một vài app hiện để skill ở dạng `.md` — xem mục 4; loại này bạn tải như file kiến thức bình thường.)

**Bước 3 — Nạp vào Claude.** Chọn đúng đường theo nơi bạn dùng Claude:

*Nếu dùng Claude Desktop (Cowork):*
1. Kéo thả file `.skill` vào khung chat → bấm **Save skill**.
2. Bấm **Add folder** và trỏ vào thư mục bạn vừa tải về, để Claude đọc được các file `.md`.
3. Mở một chat mới, gõ việc cần làm — skill tự kích hoạt khi đúng ngữ cảnh.

*Nếu dùng claude.ai trên trình duyệt:*
1. Tạo một **Project** riêng cho sản phẩm bạn phụ trách (ví dụ “Base Commerce — Sales”).
2. **Add knowledge** → tải lên các file `.md` của sản phẩm đó.
3. Cài skill: **Settings → Capabilities → Skills → Upload skill**, chọn file `.skill`.

**Bước 4 — Ra lệnh bằng tiếng Việt, như nói với đồng nghiệp.**
Không cần cú pháp đặc biệt. Xem bộ câu lệnh mẫu ở mục 5.

---

## 3. Quy ước tên file — nhìn tên là biết mở khi nào

Mọi file đều theo mẫu `Loại_TênApp`. Có 5 loại:

| Tệp | Là gì | Mở ra khi |
|---|---|---|
| `Knowledge_[App].md` | Bộ não sản phẩm: mô hình dữ liệu, thuật ngữ, cách app vận hành thật, các giới hạn đã kiểm chứng. | Khách hỏi sâu về nghiệp vụ; bạn cần soạn kịch bản tư vấn. **Nạp vào Claude, không đọc chay.** |
| `Proposal_[App].html` | Bản đề xuất hoàn chỉnh kèm ảnh màn hình thật của sản phẩm. Mở bằng trình duyệt. | Trình bày tại chỗ hoặc gửi khách ngay sau buổi gặp. Cần bản cứng thì in ra PDF từ trình duyệt (Ctrl/Cmd + P). |
| `Feature_[App].docx` | Phụ lục tính năng đầy đủ, liệt kê theo từng phân hệ. | Đính kèm hợp đồng, hồ sơ thầu; đối chiếu tính năng với đối thủ. |
| `Skill_setup_[App].skill` | Gói kỹ năng dạy Claude tự thao tác trên tenant: tạo cấu hình, bơm dữ liệu mẫu, dựng kịch bản demo. | Cần dựng môi trường demo cho khách mà không phải chờ đội triển khai. |
| `Notes_` · `Assumptions_` · `Checklist_` (`.md`) | Nhật ký khảo sát, giả định nghiệp vụ và checklist nghiệm thu demo. | Khi cần biết *vì sao cấu hình như vậy*, hoặc tự soát lại demo trước khi đưa khách xem. |

Ngoài ra một số thư mục có `*_Screenshot/` hoặc file `.zip` chứa ảnh màn hình gốc — dùng khi cần chèn ảnh vào slide, đề xuất riêng của bạn.

Ở thư mục gốc còn hai skill dùng chung, không gắn với app nào:
- `build_proposal.skill` — dựng một bản proposal mới theo đúng format của bộ này.
- `base-demo-data.skill` — dựng dữ liệu demo cho app **chưa có** skill riêng.

---

## 4. Bản đồ kho — thư mục nào đang có gì

Ký hiệu: ✅ có · — chưa có

| Thư mục | Knowledge | Proposal | Feature | Skill setup | Ghi chú |
|---|:--:|:--:|:--:|:--:|---|
| **BPM** | ✅ (2 file) | ✅ | ✅ | ✅ | có `Notes_` + thư mục ảnh |
| **Commerce** | ✅ | ✅ | ✅ | ✅ | có `Notes_`, `Assumptions_`, `Inventory_`, ảnh `.zip` |
| **Requests** | ✅ | ✅ | ✅ | ✅ | kèm mẫu văn bản `S1_De_nghi_mua_nguyen_vat_lieu.docx` |
| **Prospector** | ✅ | ✅ | ✅ | ✅ | |
| **Lead** | ✅ | ✅ | ✅ | ✅ *(dạng `.md`)* | |
| **Tasks** | ✅ | ✅ | ✅ | — | tạm dùng `base-demo-data.skill` ở thư mục gốc |
| **Projects** | — | — | — | ✅ | mới có skill + ảnh màn hình, tài liệu đang làm |
| **Cowork** | ✅ | ✅ | ✅ | ✅ | |
| **Meetings** | ✅ | ✅ | ✅ | ✅ | |
| **E-Office** | ✅ | ✅ | ✅ | ✅ | có `notes_` + ảnh `.zip` |
| **Esigns** | ✅ | ✅ | ✅ | ✅ | |
| **Townhall** | ✅ | ✅ | ✅ | ✅ | có `Notes_`, hồ sơ khảo sát `.zip` |
| **Dataset** | ✅ | ✅ | ✅ | ✅ *(dạng `.md`)* | có `Notes_` |
| **Inventories** | ✅ | ✅ | ✅ | ✅ | có `Notes_`, `Assumptions_`, `Checklist_setup_` |
| **AgentHub** | ✅ | ✅ | ✅ | ✅ | có `Notes_` |
| **HRM** | *(6 app con — xem bảng dưới)* | | | | |

**Trong thư mục HRM:**

| Thư mục con | Knowledge | Proposal | Feature | Skill setup |
|---|:--:|:--:|:--:|:--:|
| **HRIS** | ✅ | — | — | ✅ |
| **Workforce** | ✅ (2 file) | ✅ | ✅ | ✅ *(dạng `.md`)* |
| **Career** | ✅ | ✅ | ✅ | ✅ |
| **Timesheet** | ✅ | ✅ | ✅ | ✅ *(dạng `.md`)* |
| **Awards** | ✅ | ✅ | ✅ | ✅ |
| **ESOP** | ✅ | ✅ | ✅ | ✅ |

Thấy ô nào là “—” mà bạn đang cần gấp cho một cơ hội cụ thể thì nhắn — sẽ ưu tiên làm trước theo nhu cầu bán hàng.

---

## 5. Câu lệnh mẫu — copy và sửa lại theo khách của bạn

**Chuẩn bị trước buổi gặp**
> Đọc `Knowledge_Commerce.md`. Khách của tôi là công ty cơ khí 200 người, đang dùng Excel để quản lý báo giá. Liệt kê 5 câu họ nhiều khả năng sẽ hỏi và cách trả lời, kèm tính năng cụ thể để dẫn chứng.

**Dựng demo cho khách**
> Setup demo Commerce cho khách ngành cơ khí: 12 sản phẩm, 2 bảng giá, chiết khấu theo sản lượng, quy trình duyệt báo giá 2 cấp. Dữ liệu phải trông như công ty thật, không lộ mùi demo.

**Trả lời hồ sơ thầu**
> Đây là danh sách 40 yêu cầu kỹ thuật của khách (đính kèm). Dựa trên `Knowledge_BPM.md` và `Feature_BPM.docx`, đánh dấu từng yêu cầu: đáp ứng / đáp ứng một phần / không đáp ứng, kèm giải thích ngắn.

**So sánh với đối thủ**
> Khách đang so sánh Base E-Office với một phần mềm văn thư trong nước. Dựa trên `Knowledge_EOffice.md`, chỉ ra 5 điểm Base mạnh hơn theo Nghị định 30/2020, và 2 điểm cần lưu ý khi cam kết với khách.

**Soát lại demo trước khi trình bày**
> Mở `Checklist_setup_inventories.md` và kiểm tra giúp tôi tenant demo đã đủ dữ liệu chưa, còn thiếu gì thì bổ sung.

---

## 6. Năm quy tắc bắt buộc

1. **Không sửa trực tiếp file gốc trên Drive.** Cần chỉnh cho khách của bạn thì `File → Make a copy` về Drive cá nhân rồi sửa bản copy.
2. **Không gửi file `.md` cho khách.** Đó là tài liệu nội bộ, viết cho Claude đọc — có cả giả định, giới hạn và ghi chú khảo sát. Gửi khách thì dùng `Proposal_*.html` hoặc `Feature_*.docx`.
3. **Mỗi lần dùng, tải lại bản mới.** Tài liệu được cập nhật liên tục theo phiên bản sản phẩm; bản bạn tải tuần trước có thể đã cũ.
4. **Kiểm tra lại trước khi cam kết với khách.** Claude trả lời dựa trên tài liệu trong kho; với những cam kết ảnh hưởng hợp đồng (tích hợp, bảo mật, lộ trình), xác nhận lại với product trước khi chốt.
5. **Demo là demo.** Dữ liệu do skill sinh ra là dữ liệu mẫu — không đưa dữ liệu thật của khách vào tenant demo dùng chung.

---

## 7. Cần gì thì nhắn

- Thiếu tài liệu cho một app, hoặc cần bổ sung gấp cho một cơ hội đang chạy.
- Skill chạy sai, dựng demo ra dữ liệu không hợp lý.
- Nội dung trong `Knowledge_` không khớp với sản phẩm thực tế bạn thấy trên tenant.
- Cần một bản proposal riêng cho ngành đặc thù.

**Nghĩa Trần — Product** · nghia.tran@base.vn
