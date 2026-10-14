# -*- coding: utf-8 -*-
"""Sinh 3 file import custom field (Account + 2 Pipeline) cho demo Synnex FPT.

Theo skill base-crm-account-import-field: 12 cot co dinh, Field scope luon `internal`,
khong dong ghi chu cuoi bang, file tao bang write_import_excel.py (tu verify).

Chay: python demo-data/scripts/build_field_imports.py
"""
import json
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT_DIR = os.path.join(ROOT, "Dữ liệu setup", "CRM Sale")
SPEC_DIR = os.path.join(ROOT, "scripts", "_specs")
WRITER = os.path.join(ROOT, "scripts", "write_import_excel.py")

HEADERS = [
    "Field name *", "Field key", "Field type *", "Field scope *", "Short description",
    "Field options", "Is stage output", "Stages", "Required", "Table columns",
    "Field formula", "Enable default zero value",
]
WIDTHS = [28, 18, 20, 14, 36, 60, 16, 24, 10, 24, 24, 22]

NGANH_HANG = "Máy tính,Linh kiện & Ngoại vi,Thiết bị mạng,Smart Device,Phần mềm & Cloud,Giải pháp CNTT"
HANG = "Dell,HP,Lenovo,Cisco,Intel,Microsoft,Apple,Xiaomi"


def f(name, ftype, options=None, stages=None, required=0, zero=False):
    """1 dong field theo 12 cot. stages != None => Is stage output = 1."""
    return [
        name, None, ftype, "internal", None,
        options, 1 if stages else 0, stages, required, None, None,
        "YES" if zero else None,
    ]


ACCOUNT_FIELDS = [
    f("Mã đại lý", "text"),
    f("Loại tài khoản", "select",
      "Chuỗi bán lẻ,Đại lý bán lẻ,Nhà phân phối cấp 2,System Integrator,Telco · Service Provider,"
      "Cơ quan nhà nước,Doanh nghiệp Enterprise"),
    f("Mảng kinh doanh", "select", "Kênh Đại lý,Kênh Dự án"),
    f("Hạng đại lý", "select", "Key Account,Gold,Silver,SME"),
    f("Khu vực", "select", "Miền Bắc,Miền Trung,Miền Nam"),
    f("Tỉnh/Thành phố", "text"),
    f("Mã số thuế", "text"),
    f("Ngành hàng đang mua", "select-m", NGANH_HANG),
    f("Ngành hàng chưa khai thác", "select-m", NGANH_HANG),
    f("Hãng đang phân phối", "select-m", HANG),
    f("Hạn mức tín dụng (VND)", "float", zero=True),
    f("Công nợ hiện tại (VND)", "float", zero=True),
    f("Doanh số 12 tháng (VND)", "float", zero=True),
    f("Doanh số tháng gần nhất (VND)", "float", zero=True),
    f("Tăng trưởng so cùng kỳ (%)", "float", zero=True),
    f("Tình trạng HĐ nguyên tắc", "select", "Còn hiệu lực,Sắp hết hạn,Hết hạn,Chưa ký"),
    f("Ngày hết hạn HĐ nguyên tắc", "date"),
    f("Kỳ hạn thanh toán", "select", "Trả trước,Net 15,Net 30,Net 45,Net 60"),
    f("Sức khoẻ Account", "select", "Ổn định,Cần theo dõi,Rủi ro sụt doanh số"),
    f("Ngày thăm gần nhất", "date"),
    f("Tần suất thăm (lần/tháng)", "int", zero=True),
    f("Nhật ký thị sát gần nhất", "textarea"),
]

# Ten stage phai trung khop 100% voi stage tao tren pipeline.
B2G_STAGES = ["Lead dự án", "Khảo sát & Tư vấn", "Đăng ký Deal Hãng",
              "Báo giá & Hồ sơ thầu", "Đàm phán HĐ 3 bên"]
B2G_FIELDS = [
    f("Chủ đầu tư", "text"),
    f("Đơn vị SI / đối tác triển khai", "text"),
    f("Hãng chính", "select", "Dell,HP,Lenovo,Cisco,Microsoft,Intel,Apple"),
    f("Hạng mục dự án", "select-m",
      "Hạ tầng máy chủ & lưu trữ,Thiết bị mạng & bảo mật,Máy tính đầu cuối,"
      "Phần mềm bản quyền & Cloud,Giải pháp tích hợp"),
    f("Nguồn vốn", "select", "Ngân sách nhà nước,Vốn doanh nghiệp,ODA · Vốn vay,Xã hội hoá"),
    f("Hình thức lựa chọn nhà thầu", "select",
      "Đấu thầu rộng rãi,Chào hàng cạnh tranh,Chỉ định thầu,Mua sắm trực tiếp,Mua sắm doanh nghiệp"),
    f("Ngân sách dự kiến (VND)", "float", zero=True),
    f("Người quyết định và quy trình phê duyệt", "textarea"),
    f("Mã đăng ký deal với Hãng", "text", stages="Đăng ký Deal Hãng"),
    f("Tình trạng bảo vệ dự án", "select",
      "Chưa đăng ký,Đang chờ Hãng duyệt,Đã được bảo vệ,Bị từ chối", stages="Đăng ký Deal Hãng"),
    f("Ngày mở thầu", "date", stages="Báo giá & Hồ sơ thầu"),
    f("Giá đặc biệt", "select", "Chưa xin,Đang chờ duyệt,Đã duyệt,Bị trả lại",
      stages="Báo giá & Hồ sơ thầu"),
    f("Biên lợi nhuận dự kiến (%)", "float", zero=True),
    f("Điều khoản thanh toán HĐ 3 bên", "textarea", stages="Đàm phán HĐ 3 bên"),
    f("Bước tiếp theo", "text"),
    f("Hạn bước tiếp theo", "date"),
]

XSELL_STAGES = ["Phát hiện cơ hội", "Tư vấn ngành hàng", "Đại lý đặt thử", "Đặt hàng định kỳ"]
XSELL_FIELDS = [
    f("Loại cơ hội", "select",
      "Bán chéo ngành hàng,Bán thêm sản lượng,Kích hoạt lại đại lý,Mở rộng điểm bán"),
    f("Nguồn cơ hội", "select",
      "AI gợi ý từ dữ liệu PO,Sales phát hiện khi thăm,Đại lý hỏi qua Zalo OA,Chương trình của Hãng"),
    f("Ngành hàng mục tiêu", "select", NGANH_HANG),
    f("Hãng mục tiêu", "select", HANG),
    f("Chương trình áp dụng", "text"),
    f("Sản lượng dự kiến/tháng (VND)", "float", zero=True),
    f("Kết quả thăm đại lý", "textarea"),
    f("Ngày đặt thử", "date", stages="Đại lý đặt thử"),
    f("Giá trị đơn đặt thử (VND)", "float", stages="Đại lý đặt thử", zero=True),
    f("Mã PO đầu tiên", "text", stages="Đại lý đặt thử"),
    f("Bước tiếp theo", "text"),
    f("Hạn bước tiếp theo", "date"),
]

JOBS = [
    ("Account", "Import - CRM Account Đại lý & Khách hàng Synnex FPT.xlsx", ACCOUNT_FIELDS),
    ("Pipeline", "Import - CRM Pipeline Dự án B2G & Enterprise - Field.xlsx", B2G_FIELDS),
    ("Pipeline", "Import - CRM Pipeline Phát triển Đại lý & Bán chéo - Field.xlsx", XSELL_FIELDS),
]


def main():
    os.makedirs(SPEC_DIR, exist_ok=True)
    for i, (sub, fname, rows) in enumerate(JOBS):
        out_dir = os.path.join(OUT_DIR, sub)
        os.makedirs(out_dir, exist_ok=True)
        spec = {
            "output": os.path.join(out_dir, fname),
            "sheet_name": "Exported file",
            "profile": "crm",
            "headers": HEADERS,
            "rows": rows,
            "column_widths": WIDTHS,
        }
        spec_path = os.path.join(SPEC_DIR, f"field_{i}.json")
        with open(spec_path, "w", encoding="utf-8") as fh:
            json.dump(spec, fh, ensure_ascii=False, indent=1)
        r = subprocess.run([sys.executable, WRITER, "--spec", spec_path])
        if r.returncode:
            sys.exit(r.returncode)


if __name__ == "__main__":
    main()
