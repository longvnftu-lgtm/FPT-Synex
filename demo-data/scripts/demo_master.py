# -*- coding: utf-8 -*-
"""Bo du lieu demo goc Synnex FPT — 1 nguon su that cho Account, Contact, Deal.

Toan bo ten cong ty / nguoi / domain / SDT / MST la HU CAU cho muc dich demo.
Owner dung ma persona (SALES_BAC...) — doi sang username that qua personas.json.
Khoa dict cua tung ban ghi = dung Field name / ten cot tren Base de fill_template.py
map theo ten header cua file mau that.
"""
import random
from datetime import date, timedelta

TODAY = date(2026, 10, 14)
rnd = random.Random(20261014)

PERSONAS = {
    "SALES_BAC": "Sales kênh Miền Bắc",
    "SALES_NAM": "Sales kênh Miền Nam",
    "SALES_DUAN": "Sales dự án B2G & Enterprise",
    "TRUONG_KENH": "Trưởng kênh Đại lý (quản lý)",
}

NGANH = ["Máy tính", "Linh kiện & Ngoại vi", "Thiết bị mạng", "Smart Device",
         "Phần mềm & Cloud", "Giải pháp CNTT"]

TY = 1_000_000_000
TR = 1_000_000


def d(days):
    return (TODAY + timedelta(days=days)).strftime("%d/%m/%Y")


def round_m(x):
    """Lam tron toi trieu dong cho so trong 'that'."""
    return int(round(x / TR) * TR)


# ---------------------------------------------------------------------------
# ACCOUNT — (ten, domain, loai, hang, khu vuc, tinh, dang mua, hang SX, ghi chu cau chuyen)
# ---------------------------------------------------------------------------
CHANNEL = [
    # Key Account (6)
    ("Chuỗi Điện máy Sao Việt", "saovietmart.vn", "Chuỗi bán lẻ", "Key Account", "Miền Nam", "TP. Hồ Chí Minh",
     ["Máy tính", "Smart Device", "Linh kiện & Ngoại vi"], ["Dell", "HP", "Apple", "Xiaomi"], "STORY_XSELL"),
    ("Hệ thống Bán lẻ Công nghệ Nhật Minh", "nhatminhtech.vn", "Chuỗi bán lẻ", "Key Account", "Miền Bắc", "Hà Nội",
     ["Máy tính", "Smart Device", "Linh kiện & Ngoại vi", "Thiết bị mạng"], ["Dell", "Lenovo", "Apple", "Xiaomi"], None),
    ("Chuỗi Laptop An Phát Digital", "anphatdigital.vn", "Chuỗi bán lẻ", "Key Account", "Miền Bắc", "Hà Nội",
     ["Máy tính", "Linh kiện & Ngoại vi"], ["Dell", "HP", "Lenovo", "Intel"], None),
    ("Siêu thị Điện tử Hoàng Long", "hoanglongdientu.vn", "Chuỗi bán lẻ", "Key Account", "Miền Trung", "Đà Nẵng",
     ["Máy tính", "Smart Device"], ["HP", "Apple", "Xiaomi"], None),
    ("Chuỗi Di động Thế Hệ Mới", "thehemoi.vn", "Chuỗi bán lẻ", "Key Account", "Miền Nam", "TP. Hồ Chí Minh",
     ["Smart Device", "Linh kiện & Ngoại vi"], ["Apple", "Xiaomi"], None),
    ("Công ty CP Phân phối Tin học Phương Đông", "phuongdongit.vn", "Nhà phân phối cấp 2", "Key Account", "Miền Nam",
     "TP. Hồ Chí Minh", ["Máy tính", "Linh kiện & Ngoại vi", "Thiết bị mạng", "Phần mềm & Cloud"],
     ["Dell", "HP", "Cisco", "Microsoft"], None),
    # Gold (12)
    ("Tin học Minh Khang", "minhkhangcomputer.vn", "Đại lý bán lẻ", "Gold", "Miền Nam", "Cần Thơ",
     ["Máy tính", "Linh kiện & Ngoại vi"], ["Dell", "HP"], "STORY_CREDIT"),
    ("Máy tính Bách Khoa Hải Phòng", "bachkhoahp.vn", "Đại lý bán lẻ", "Gold", "Miền Bắc", "Hải Phòng",
     ["Máy tính", "Linh kiện & Ngoại vi", "Thiết bị mạng"], ["Dell", "Lenovo", "Cisco"], None),
    ("Công ty TNHH Tin học Thành Đạt", "thanhdatvinh.vn", "Đại lý bán lẻ", "Gold", "Miền Trung", "Nghệ An",
     ["Máy tính", "Smart Device"], ["HP", "Xiaomi"], None),
    ("Tin học Ngọc Thịnh", "ngocthinhpc.vn", "Đại lý bán lẻ", "Gold", "Miền Nam", "Đồng Nai",
     ["Máy tính", "Linh kiện & Ngoại vi"], ["Dell", "Intel"], None),
    ("Công ty TNHH Công nghệ Việt Hưng", "viethungtech.vn", "Đại lý bán lẻ", "Gold", "Miền Bắc", "Bắc Ninh",
     ["Máy tính", "Thiết bị mạng", "Phần mềm & Cloud"], ["Lenovo", "Cisco", "Microsoft"], None),
    ("Máy tính Trường Sơn", "truongsonhue.vn", "Đại lý bán lẻ", "Gold", "Miền Trung", "Thừa Thiên Huế",
     ["Máy tính", "Linh kiện & Ngoại vi"], ["HP", "Lenovo"], None),
    ("Tin học Hải Âu", "haiaunhatrang.vn", "Đại lý bán lẻ", "Gold", "Miền Trung", "Khánh Hòa",
     ["Máy tính", "Smart Device"], ["Dell", "Apple"], None),
    ("Công ty CP Thiết bị Số Đông Dương", "dongduongdigital.vn", "Đại lý bán lẻ", "Gold", "Miền Nam",
     "TP. Hồ Chí Minh", ["Máy tính", "Thiết bị mạng", "Giải pháp CNTT"], ["Dell", "Cisco"], None),
    ("Laptop Tâm An", "laptoptaman.vn", "Đại lý bán lẻ", "Gold", "Miền Bắc", "Hà Nội",
     ["Máy tính", "Linh kiện & Ngoại vi"], ["Dell", "HP", "Lenovo"], None),
    ("Tin học Kim Long", "kimlongbd.vn", "Đại lý bán lẻ", "Gold", "Miền Nam", "Bình Dương",
     ["Máy tính", "Linh kiện & Ngoại vi", "Thiết bị mạng"], ["HP", "Cisco"], None),
    ("Công ty TNHH Viễn thông Tân Tiến", "tantientelecom.vn", "Đại lý bán lẻ", "Gold", "Miền Trung", "Bình Định",
     ["Smart Device", "Thiết bị mạng"], ["Xiaomi", "Cisco"], None),
    ("Tin học Sông Hàn", "songhanit.vn", "Đại lý bán lẻ", "Gold", "Miền Trung", "Đà Nẵng",
     ["Máy tính", "Linh kiện & Ngoại vi"], ["Dell", "Lenovo"], None),
]

SME_SHOPS = [
    ("Tin học Phúc Lộc", "Miền Bắc", "Thái Bình"), ("Máy tính Hưng Thịnh", "Miền Bắc", "Nam Định"),
    ("Tin học Quang Minh", "Miền Trung", "Thanh Hóa"), ("Vi tính Bảo An", "Miền Nam", "Vĩnh Long"),
    ("Tin học Đức Trí", "Miền Trung", "Đắk Lắk"), ("Máy tính Gia Huy", "Miền Nam", "An Giang"),
    ("Tin học Ánh Dương", "Miền Trung", "Quảng Ngãi"), ("Vi tính Thiên Phú", "Miền Nam", "Tiền Giang"),
    ("Tin học Hòa Bình Xanh", "Miền Bắc", "Hòa Bình"), ("Máy tính Phương Nam Cà Mau", "Miền Nam", "Cà Mau"),
    ("Tin học Lộc Phát", "Miền Trung", "Gia Lai"), ("Vi tính Tân Phát", "Miền Nam", "Kiên Giang"),
    ("Tin học Minh Châu", "Miền Bắc", "Hà Nội"), ("Máy tính Nam Á", "Miền Nam", "TP. Hồ Chí Minh"),
    ("Tin học Đại Việt Lạng Sơn", "Miền Bắc", "Lạng Sơn"), ("Vi tính Kim Ngân", "Miền Nam", "Bình Thuận"),
    ("Tin học Bình Minh", "Miền Trung", "Phú Yên"), ("Máy tính Hồng Phát", "Miền Bắc", "Bắc Giang"),
    ("Tin học Thuận Thành", "Miền Bắc", "Bắc Ninh"), ("Vi tính Nhật Quang", "Miền Nam", "Sóc Trăng"),
    ("Tin học An Khang", "Miền Nam", "Bà Rịa - Vũng Tàu"), ("Máy tính Thanh Bình", "Miền Bắc", "Hưng Yên"),
]
SME_STORY = {"Tin học Đức Trí": "STORY_ZALO", "Vi tính Bảo An": "STORY_CHURN",
             "Máy tính Hồng Phát": "STORY_CHURN", "Tin học Ánh Dương": "STORY_CHURN"}

PROJECT = [
    ("Ban QLDA Chuyển đổi số tỉnh Đông Hải", "cds.donghai.gov.vn", "Cơ quan nhà nước", "Miền Trung", "Tỉnh Đông Hải"),
    ("Sở Y tế tỉnh Đông Hải", "syt.donghai.gov.vn", "Cơ quan nhà nước", "Miền Trung", "Tỉnh Đông Hải"),
    ("Cục Thống kê tỉnh Bắc Sơn", "thongke.bacson.gov.vn", "Cơ quan nhà nước", "Miền Bắc", "Tỉnh Bắc Sơn"),
    ("Đại học Kỹ thuật Hồng Lam", "hlut.edu.vn", "Cơ quan nhà nước", "Miền Bắc", "Hà Nội"),
    ("Tổng Công ty Cảng biển Đông Hải", "donghaiport.vn", "Doanh nghiệp Enterprise", "Miền Trung", "Tỉnh Đông Hải"),
    ("Bệnh viện Đa khoa Quốc tế Tâm Đức", "tamduchospital.vn", "Doanh nghiệp Enterprise", "Miền Nam", "TP. Hồ Chí Minh"),
    ("Ngân hàng TMCP Sao Bắc Á", "saobaca.bank.vn", "Doanh nghiệp Enterprise", "Miền Bắc", "Hà Nội"),
    ("Tập đoàn Bảo hiểm An Bình Thịnh", "abtinsurance.vn", "Doanh nghiệp Enterprise", "Miền Nam", "TP. Hồ Chí Minh"),
    ("Công ty CP Logistics Đông Dương", "dongduonglogistics.vn", "Doanh nghiệp Enterprise", "Miền Nam", "TP. Hồ Chí Minh"),
    ("Công ty CP Giải pháp Tích hợp Thăng Long Tech", "thanglongtech.vn", "System Integrator", "Miền Bắc", "Hà Nội"),
    ("Công ty TNHH Hệ thống Số Hưng Việt", "hungvietsystems.vn", "System Integrator", "Miền Nam", "TP. Hồ Chí Minh"),
    ("Sao Mai Telecom", "saomaitelecom.vn", "Telco · Service Provider", "Miền Bắc", "Hà Nội"),
]

SLUG = {"Miền Bắc": "SALES_BAC", "Miền Trung": "SALES_BAC", "Miền Nam": "SALES_NAM"}

TIER_PROFILE = {  # (doanh so 12T min,max) , (han muc min,max), ky han, tan suat tham
    "Key Account": ((80 * TY, 350 * TY), (20 * TY, 60 * TY), "Net 45", 4),
    "Gold": ((12 * TY, 45 * TY), (3 * TY, 10 * TY), "Net 30", 2),
    "SME": ((0.8 * TY, 6 * TY), (0.3 * TY, 1.5 * TY), "Net 15", 0),
}

VISIT_NOTES = [
    "Thăm cửa hàng, trưng bày laptop Dell Inspiron đúng vị trí; chủ đại lý phản ánh hàng Vostro về chậm 5 ngày.",
    "Họp với chủ đại lý về chương trình thưởng Q4; đại lý muốn tăng hạn mức thêm 2 tỷ cho mùa Tết.",
    "Kiểm tra tồn kho linh kiện, đề xuất bổ sung SSD và RAM vì tồn dưới 2 tuần bán.",
    "Giới thiệu dòng thiết bị mạng Cisco Small Business; đại lý quan tâm nhưng chưa có kỹ thuật viên.",
    "Đối soát công nợ tháng 9, đã thống nhất lịch thanh toán 2 đợt.",
    "Đào tạo nhân viên bán hàng của đại lý về dòng laptop AI PC mới.",
]


def _mst():
    return "0" + "".join(str(rnd.randint(0, 9)) for _ in range(9))


def build_accounts():
    accounts = []
    idx = 0

    def make(name, domain, loai, tier, kv, tinh, dang_mua, hang, story, mang="Kênh Đại lý"):
        nonlocal idx
        idx += 1
        if mang == "Kênh Dự án":
            # chi so kenh dai ly khong ap dung cho khach du an -> de trong
            ds12 = han_muc = cong_no = ds_thang = tang = None
            ky_han, tan_suat, owner, ngay_tham, nhat_ky = "Net 30", 1, "SALES_DUAN", d(-rnd.randint(5, 40)), None
            hd, hd_han = "Chưa ký", None
            suc_khoe = "Ổn định"
        else:
            (ds_lo, ds_hi), (hm_lo, hm_hi), ky_han, tan_suat = TIER_PROFILE[tier]
            ds12 = round_m(rnd.uniform(ds_lo, ds_hi))
            han_muc = int(round(rnd.uniform(hm_lo, hm_hi) / (500 * TR))) * 500 * TR
            cong_no = round_m(han_muc * rnd.uniform(0.35, 0.8))
            tang = round(rnd.uniform(-4, 18), 1)
            suc_khoe = "Ổn định"
            if story == "STORY_CREDIT":
                cong_no = round_m(han_muc * 0.96)
                suc_khoe = "Cần theo dõi"
            if story == "STORY_CHURN":
                tang = round(rnd.uniform(-38, -22), 1)
                suc_khoe = "Rủi ro sụt doanh số"
            factor = 1 + tang / 100
            ds_thang = round_m(ds12 / 12 * factor * rnd.uniform(0.9, 1.15))
            owner = "SALES_BAC" if kv in ("Miền Bắc", "Miền Trung") else "SALES_NAM"
            if tier == "SME":
                owner = None  # tep SME chua co Sales phu trach -> Agent cham SME
            ngay_tham = d(-rnd.randint(3, 25)) if tan_suat else (d(-rnd.randint(70, 160)) if rnd.random() < .5 else None)
            nhat_ky = rnd.choice(VISIT_NOTES) if tan_suat else None
            hd = "Sắp hết hạn" if rnd.random() < .15 else "Còn hiệu lực"
            hd_han = d(rnd.randint(20, 60)) if hd == "Sắp hết hạn" else d(rnd.randint(120, 540))
        chua = [n for n in NGANH if n not in dang_mua] if mang == "Kênh Đại lý" else []
        accounts.append({
            "_story": story,
            "_tier": tier,
            "Account name": name,
            "Domain": domain,
            "Account owner": owner,
            "Account value": ds12,
            "Currency": "VND",
            "Address": tinh,
            "Mã đại lý": (f"SFD-{kv[5]}{idx:04d}" if mang == "Kênh Đại lý" else f"SFP-{idx:04d}"),
            "Loại tài khoản": loai,
            "Mảng kinh doanh": mang,
            "Hạng đại lý": tier,
            "Khu vực": kv,
            "Tỉnh/Thành phố": tinh,
            "Mã số thuế": _mst(),
            "Ngành hàng đang mua": dang_mua,
            "Ngành hàng chưa khai thác": chua,
            "Hãng đang phân phối": hang,
            "Hạn mức tín dụng (VND)": han_muc,
            "Công nợ hiện tại (VND)": cong_no,
            "Doanh số 12 tháng (VND)": ds12,
            "Doanh số tháng gần nhất (VND)": ds_thang,
            "Tăng trưởng so cùng kỳ (%)": tang,
            "Tình trạng HĐ nguyên tắc": hd,
            "Ngày hết hạn HĐ nguyên tắc": hd_han,
            "Kỳ hạn thanh toán": ky_han,
            "Sức khoẻ Account": suc_khoe,
            "Ngày thăm gần nhất": ngay_tham,
            "Tần suất thăm (lần/tháng)": tan_suat,
            "Nhật ký thị sát gần nhất": nhat_ky,
        })

    for row in CHANNEL:
        make(*row)
    sme_pool = [["Máy tính"], ["Máy tính", "Linh kiện & Ngoại vi"], ["Linh kiện & Ngoại vi"],
                ["Smart Device"], ["Máy tính", "Smart Device"]]
    for name, kv, tinh in SME_SHOPS:
        make(name, None, "Đại lý bán lẻ", "SME", kv, tinh, rnd.choice(sme_pool),
             rnd.sample(["Dell", "HP", "Lenovo", "Xiaomi"], 2), SME_STORY.get(name))
    for name, dom, loai, kv, tinh in PROJECT:
        make(name, dom, loai, None, kv, tinh, [], [], None, mang="Kênh Dự án")
    return accounts


# ---------------------------------------------------------------------------
# CONTACT
# ---------------------------------------------------------------------------
HO = ["Nguyễn", "Trần", "Lê", "Phạm", "Hoàng", "Vũ", "Đặng", "Bùi", "Đỗ", "Ngô", "Dương", "Lý"]
DEM = ["Văn", "Thị", "Minh", "Quốc", "Thu", "Hải", "Ngọc", "Đức", "Thanh", "Anh", "Hoàng", "Bảo"]
TEN = ["Hùng", "Lan", "Tuấn", "Hương", "Dũng", "Mai", "Long", "Trang", "Phong", "Linh", "Khoa", "Hà",
       "Sơn", "Thảo", "Nam", "Vy", "Quân", "Yến", "Đạt", "Ngân"]
ASCII = str.maketrans("àáảãạăằắẳẵặâầấẩẫậèéẻẽẹêềếểễệìíỉĩịòóỏõọôồốổỗộơờớởỡợùúủũụưừứửữựỳýỷỹỵđ",
                      "aaaaaaaaaaaaaaaaaeeeeeeeeeeeiiiiiooooooooooooooooouuuuuuuuuuuyyyyyd")

TITLES_CHANNEL = ["Giám đốc", "Trưởng phòng mua hàng", "Kế toán công nợ", "Quản lý cửa hàng"]
TITLES_PROJECT = ["Phó Giám đốc phụ trách CNTT", "Trưởng phòng CNTT", "Chuyên viên mua sắm",
                  "Giám đốc kinh doanh", "Trưởng ban QLDA"]


def _person():
    return f"{rnd.choice(HO)} {rnd.choice(DEM)} {rnd.choice(TEN)}"


def _phone():
    return rnd.choice(["090", "091", "093", "096", "098", "097", "083", "085"]) + \
        "".join(str(rnd.randint(0, 9)) for _ in range(7))


def build_contacts(accounts):
    contacts = []
    used = set()
    for a in accounts:
        proj = a["Mảng kinh doanh"] == "Kênh Dự án"
        n = 1 if a["_tier"] == "SME" else (3 if a["_tier"] == "Key Account" or proj else 2)
        titles = (TITLES_PROJECT if proj else TITLES_CHANNEL)[:]
        rnd.shuffle(titles)
        if not proj:
            titles.remove("Giám đốc")
            titles.insert(0, "Giám đốc" if a["_tier"] != "Key Account" else "Giám đốc ngành hàng")
        for i in range(n):
            name = _person()
            while name in used:
                name = _person()
            used.add(name)
            parts = name.lower().translate(ASCII).split()
            local = parts[-1] + "." + "".join(p[0] for p in parts[:-1])
            email = f"{local}@{a['Domain']}" if a["Domain"] else f"{local}{rnd.randint(10, 99)}@gmail.com"
            contacts.append({
                "Contact name": name,
                "Title": titles[i],
                "Account": a["Account name"],
                "Email": email,
                "Phone": _phone(),
                "Owner": a["Account owner"],
                "_primary": i == 0,
            })
    return contacts


# ---------------------------------------------------------------------------
# DEAL — pipeline Du an B2G & Enterprise (18 deal: 3/4/3/5/3)
# ---------------------------------------------------------------------------
# (account, giai phap, stage, gia tri ty, hang, hang muc, nguon von, hinh thuc, si, close+days, overview)
B2G = [
    ("Cục Thống kê tỉnh Bắc Sơn", "Máy trạm điều tra viên 120 bộ", "Lead dự án", 2.4, "HP",
     ["Máy tính đầu cuối"], "Ngân sách nhà nước", "Chào hàng cạnh tranh", None, 150,
     "Cục cần thay máy trạm cho đợt tổng điều tra 2027, đang lập dự toán."),
    ("Sao Mai Telecom", "Switch truy nhập 300 trạm", "Lead dự án", 6.8, "Cisco",
     ["Thiết bị mạng & bảo mật"], "Vốn doanh nghiệp", "Mua sắm doanh nghiệp", None, 170,
     "Nhà mạng mở rộng hạ tầng FTTH khu vực phía Bắc, mới gửi RFI."),
    ("Tập đoàn Bảo hiểm An Bình Thịnh", "Bản quyền Microsoft 365 1.500 user", "Lead dự án", 9.5, "Microsoft",
     ["Phần mềm bản quyền & Cloud"], "Vốn doanh nghiệp", "Mua sắm doanh nghiệp", None, 120,
     "Gia hạn và mở rộng bản quyền, khách đang so sánh EA và CSP."),
    ("Đại học Kỹ thuật Hồng Lam", "Phòng lab AI 60 máy trạm GPU", "Khảo sát & Tư vấn", 11.2, "Dell",
     ["Máy tính đầu cuối", "Hạ tầng máy chủ & lưu trữ"], "Ngân sách nhà nước", "Đấu thầu rộng rãi",
     "Công ty CP Giải pháp Tích hợp Thăng Long Tech", 160,
     "Đã khảo sát hiện trạng phòng lab, chờ khoa CNTT chốt cấu hình GPU."),
    ("Bệnh viện Đa khoa Quốc tế Tâm Đức", "Hạ tầng máy chủ HIS/PACS", "Khảo sát & Tư vấn", 14.6, "HP",
     ["Hạ tầng máy chủ & lưu trữ"], "Vốn doanh nghiệp", "Mua sắm doanh nghiệp",
     "Công ty TNHH Hệ thống Số Hưng Việt", 110,
     "Bệnh viện nâng cấp hệ thống PACS, cần lưu trữ 400TB, SI Hưng Việt dẫn dắt."),
    ("Công ty CP Logistics Đông Dương", "Wifi kho bãi 5 trung tâm", "Khảo sát & Tư vấn", 3.9, "Cisco",
     ["Thiết bị mạng & bảo mật"], "Vốn doanh nghiệp", "Mua sắm doanh nghiệp", None, 90,
     "Khảo sát 2/5 kho, cần phủ sóng cho máy quét mã vạch cầm tay."),
    ("Sở Y tế tỉnh Đông Hải", "Máy tính trạm y tế xã 220 bộ", "Khảo sát & Tư vấn", 4.4, "Lenovo",
     ["Máy tính đầu cuối"], "Ngân sách nhà nước", "Đấu thầu rộng rãi",
     "Công ty CP Giải pháp Tích hợp Thăng Long Tech", 200,
     "Thuộc đề án y tế số cơ sở, đang chờ phê duyệt chủ trương đầu tư."),
    ("Ngân hàng TMCP Sao Bắc Á", "Máy chủ & SAN cho DR site", "Đăng ký Deal Hãng", 28.5, "Dell",
     ["Hạ tầng máy chủ & lưu trữ"], "Vốn doanh nghiệp", "Mua sắm doanh nghiệp",
     "Công ty CP Giải pháp Tích hợp Thăng Long Tech", 95,
     "Dự án trung tâm dữ liệu dự phòng, đã nộp đăng ký deal với Dell, chờ phản hồi bảo vệ giá."),
    ("Tổng Công ty Cảng biển Đông Hải", "Firewall & SOC cảng", "Đăng ký Deal Hãng", 7.2, "Cisco",
     ["Thiết bị mạng & bảo mật"], "Vốn doanh nghiệp", "Chào hàng cạnh tranh",
     "Công ty TNHH Hệ thống Số Hưng Việt", 80,
     "Cisco đã bảo vệ dự án cho Synnex FPT qua SI Hưng Việt."),
    ("Tập đoàn Bảo hiểm An Bình Thịnh", "Laptop cho đại lý bảo hiểm 800 máy", "Đăng ký Deal Hãng", 15.6, "Lenovo",
     ["Máy tính đầu cuối"], "Vốn doanh nghiệp", "Mua sắm doanh nghiệp", None, 70,
     "Đối thủ cũng đăng ký deal, Lenovo đang xét theo thứ tự nộp."),
    ("Ban QLDA Chuyển đổi số tỉnh Đông Hải", "Trung tâm IOC tỉnh giai đoạn 2", "Báo giá & Hồ sơ thầu", 42.0,
     "Dell", ["Hạ tầng máy chủ & lưu trữ", "Thiết bị mạng & bảo mật", "Giải pháp tích hợp"],
     "Ngân sách nhà nước", "Đấu thầu rộng rãi", "Công ty CP Giải pháp Tích hợp Thăng Long Tech", 60,
     "DEAL CHỦ LỰC: hồ sơ thầu đã phát hành, giá đặc biệt Dell chưa duyệt xong — đang nằm quá SLA."),
    ("Đại học Kỹ thuật Hồng Lam", "Hạ tầng mạng ký túc xá", "Báo giá & Hồ sơ thầu", 5.3, "Cisco",
     ["Thiết bị mạng & bảo mật"], "Ngân sách nhà nước", "Chào hàng cạnh tranh", None, 45,
     "Đã nộp báo giá, chờ hội đồng chấm."),
    ("Sở Y tế tỉnh Đông Hải", "Máy chủ bệnh án điện tử tuyến tỉnh", "Báo giá & Hồ sơ thầu", 9.8, "HP",
     ["Hạ tầng máy chủ & lưu trữ"], "Ngân sách nhà nước", "Đấu thầu rộng rãi",
     "Công ty TNHH Hệ thống Số Hưng Việt", 55,
     "Hồ sơ mời thầu yêu cầu bảo hành 5 năm tại chỗ, cần xác nhận với HP."),
    ("Công ty CP Logistics Đông Dương", "Thiết bị cầm tay & máy in nhãn", "Báo giá & Hồ sơ thầu", 2.1, "HP",
     ["Máy tính đầu cuối"], "Vốn doanh nghiệp", "Mua sắm doanh nghiệp", None, 35,
     "Khách yêu cầu giao theo 3 đợt, thanh toán Net 45."),
    ("Bệnh viện Đa khoa Quốc tế Tâm Đức", "Máy tính phòng khám 150 bộ", "Báo giá & Hồ sơ thầu", 3.6, "Dell",
     ["Máy tính đầu cuối"], "Vốn doanh nghiệp", "Mua sắm doanh nghiệp", None, 40,
     "Đã gửi báo giá lần 2 sau khi khách xin giảm 3%."),
    ("Ngân hàng TMCP Sao Bắc Á", "Máy tính giao dịch viên 600 bộ", "Đàm phán HĐ 3 bên", 13.4, "HP",
     ["Máy tính đầu cuối"], "Vốn doanh nghiệp", "Mua sắm doanh nghiệp",
     "Công ty CP Giải pháp Tích hợp Thăng Long Tech", 20,
     "DEAL CHỦ LỰC: đang chốt điều khoản HĐ 3 bên Ngân hàng – Thăng Long Tech – Synnex FPT."),
    ("Tổng Công ty Cảng biển Đông Hải", "Máy chủ hệ thống điều hành cảng", "Đàm phán HĐ 3 bên", 8.7, "Dell",
     ["Hạ tầng máy chủ & lưu trữ"], "Vốn doanh nghiệp", "Chào hàng cạnh tranh",
     "Công ty TNHH Hệ thống Số Hưng Việt", 25,
     "Đã trúng chào hàng, đang thương thảo tiến độ thanh toán."),
    ("Sao Mai Telecom", "Bản quyền ảo hoá trung tâm dữ liệu", "Đàm phán HĐ 3 bên", 4.9, "Microsoft",
     ["Phần mềm bản quyền & Cloud"], "Vốn doanh nghiệp", "Mua sắm doanh nghiệp", None, 15,
     "Thống nhất giá, chờ pháp chế nhà mạng duyệt hợp đồng."),
]

DECISION_BY_TYPE = {
    "Cơ quan nhà nước": "Thủ trưởng đơn vị phê duyệt kế hoạch lựa chọn nhà thầu; phòng CNTT là đầu mối kỹ thuật; "
                        "Sở Tài chính thẩm định dự toán trước khi phát hành hồ sơ.",
    "Doanh nghiệp Enterprise": "Giám đốc CNTT đề xuất → Hội đồng mua sắm (CNTT, Tài chính, Pháp chế) thẩm định → "
                               "Tổng Giám đốc phê duyệt.",
    "System Integrator": "Giám đốc kinh doanh SI chốt phương án với chủ đầu tư; Synnex FPT báo giá back-to-back cho SI.",
    "Telco · Service Provider": "Khối Kỹ thuật đề xuất → Ban Mua sắm tập trung chấm thầu → Phó TGĐ Kỹ thuật phê duyệt.",
}

B2G_STAGES = ["Lead dự án", "Khảo sát & Tư vấn", "Đăng ký Deal Hãng", "Báo giá & Hồ sơ thầu", "Đàm phán HĐ 3 bên"]
B2G_PROB = {"Lead dự án": 10, "Khảo sát & Tư vấn": 25, "Đăng ký Deal Hãng": 40,
            "Báo giá & Hồ sơ thầu": 60, "Đàm phán HĐ 3 bên": 85}

NEXT_STEP = {
    "Lead dự án": "Hẹn buổi khảo sát hiện trạng với phòng CNTT",
    "Khảo sát & Tư vấn": "Gửi đề xuất cấu hình và dự toán sơ bộ",
    "Đăng ký Deal Hãng": "Theo dõi phản hồi bảo vệ giá từ Hãng",
    "Báo giá & Hồ sơ thầu": "Hoàn thiện hồ sơ năng lực và bảo lãnh dự thầu",
    "Đàm phán HĐ 3 bên": "Chốt điều khoản thanh toán với SI và chủ đầu tư",
}


def _passed(stage, mark):
    return B2G_STAGES.index(stage) >= B2G_STAGES.index(mark)


def build_b2g(accounts, contacts):
    acc_type = {a["Account name"]: a["Loại tài khoản"] for a in accounts}
    first_contact = {}
    for c in contacts:
        first_contact.setdefault(c["Account"], c)
    deals = []
    for i, (acc, sol, stage, val, hang, hm, von, ht, si, close, ov) in enumerate(B2G):
        c = first_contact[acc]
        bao_ve = None
        if _passed(stage, "Đăng ký Deal Hãng"):
            if stage == "Đăng ký Deal Hãng":
                bao_ve = ["Đang chờ Hãng duyệt", "Đã được bảo vệ", "Đang chờ Hãng duyệt"][i % 3]
            else:
                bao_ve = "Đã được bảo vệ"
        gia_db = None
        if _passed(stage, "Báo giá & Hồ sơ thầu"):
            gia_db = "Đang chờ duyệt" if "CHỦ LỰC: hồ sơ thầu" in ov else "Đã duyệt"
        deals.append({
            "Deal name": f"{acc} – {sol}",
            "Stage": stage,
            "Deal value": int(val * TY),
            "Currency": "VND",
            "Account": acc,
            "Contact": c["Contact name"],
            "Deal owner": "SALES_DUAN",
            "Probability": B2G_PROB[stage],
            "Expected close date": d(close),
            "Overview": ov,
            "Chủ đầu tư": acc,
            "Đơn vị SI / đối tác triển khai": si,
            "Hãng chính": hang,
            "Hạng mục dự án": hm,
            "Nguồn vốn": von,
            "Hình thức lựa chọn nhà thầu": ht,
            "Ngân sách dự kiến (VND)": round_m(val * TY * rnd.uniform(1.03, 1.15)),
            "Người quyết định và quy trình phê duyệt": DECISION_BY_TYPE[acc_type[acc]],
            "Mã đăng ký deal với Hãng": (f"DR-{hang[:3].upper()}-26{rnd.randint(10000, 99999)}"
                                         if _passed(stage, "Đăng ký Deal Hãng") else None),
            "Tình trạng bảo vệ dự án": bao_ve,
            "Ngày mở thầu": ((d(12) if "CHỦ LỰC" in ov else d(rnd.randint(-10, 20)))
                             if _passed(stage, "Báo giá & Hồ sơ thầu") else None),
            "Giá đặc biệt": gia_db,
            "Biên lợi nhuận dự kiến (%)": round(rnd.uniform(3.5, 9.0), 1),
            "Điều khoản thanh toán HĐ 3 bên": (
                "Tạm ứng 30% sau ký HĐ; 60% sau nghiệm thu lắp đặt; 10% sau bảo lãnh bảo hành. "
                "SI thanh toán cho Synnex FPT Net 30 kể từ ngày nhận tiền từ chủ đầu tư."
                if stage == "Đàm phán HĐ 3 bên" else None),
            "Bước tiếp theo": NEXT_STEP[stage],
            "Hạn bước tiếp theo": d(rnd.choice([-3, -1, 0, 2, 5, 7])),
        })
    return deals


# ---------------------------------------------------------------------------
# DEAL — pipeline Phat trien Dai ly & Ban cheo (12 deal: 3/4/3/2)
# ---------------------------------------------------------------------------
XSELL_STAGES = ["Phát hiện cơ hội", "Tư vấn ngành hàng", "Đại lý đặt thử", "Đặt hàng định kỳ"]
XSELL_PROB = {"Phát hiện cơ hội": 15, "Tư vấn ngành hàng": 35, "Đại lý đặt thử": 65, "Đặt hàng định kỳ": 90}
# (account, nganh muc tieu, hang, stage, nguon, loai, san luong trieu/thang, chuong trinh, close)
XSELL = [
    ("Chuỗi Điện máy Sao Việt", "Thiết bị mạng", "Cisco", "Phát hiện cơ hội", "AI gợi ý từ dữ liệu PO",
     "Bán chéo ngành hàng", 1800, "Cisco SMB Partner Q4", 75),
    ("Tin học Đức Trí", "Máy tính", "Dell", "Phát hiện cơ hội", "Đại lý hỏi qua Zalo OA",
     "Bán thêm sản lượng", 650, "Dell Back to School mở rộng", 40),
    ("Máy tính Hồng Phát", "Máy tính", "HP", "Phát hiện cơ hội", "AI gợi ý từ dữ liệu PO",
     "Kích hoạt lại đại lý", 300, "HP Partner First", 60),
    ("Chuỗi Laptop An Phát Digital", "Smart Device", "Xiaomi", "Tư vấn ngành hàng", "Chương trình của Hãng",
     "Bán chéo ngành hàng", 1200, "Xiaomi Ecosystem Corner", 55),
    ("Siêu thị Điện tử Hoàng Long", "Linh kiện & Ngoại vi", "Intel", "Tư vấn ngành hàng", "AI gợi ý từ dữ liệu PO",
     "Bán chéo ngành hàng", 900, "Intel AI PC Retail Kit", 50),
    ("Công ty TNHH Tin học Thành Đạt", "Phần mềm & Cloud", "Microsoft", "Tư vấn ngành hàng",
     "Sales phát hiện khi thăm", "Bán chéo ngành hàng", 250, "Microsoft 365 for SMB", 45),
    ("Tin học Hải Âu", "Thiết bị mạng", "Cisco", "Tư vấn ngành hàng", "Sales phát hiện khi thăm",
     "Bán chéo ngành hàng", 400, "Cisco SMB Partner Q4", 60),
    ("Chuỗi Di động Thế Hệ Mới", "Máy tính", "Apple", "Đại lý đặt thử", "Chương trình của Hãng",
     "Bán chéo ngành hàng", 3200, "Apple Mac cho chuỗi di động", 30),
    ("Tin học Ngọc Thịnh", "Thiết bị mạng", "Cisco", "Đại lý đặt thử", "AI gợi ý từ dữ liệu PO",
     "Bán chéo ngành hàng", 520, "Cisco SMB Partner Q4", 25),
    ("Máy tính Trường Sơn", "Smart Device", "Xiaomi", "Đại lý đặt thử", "Sales phát hiện khi thăm",
     "Mở rộng điểm bán", 380, "Xiaomi Ecosystem Corner", 30),
    ("Hệ thống Bán lẻ Công nghệ Nhật Minh", "Phần mềm & Cloud", "Microsoft", "Đặt hàng định kỳ",
     "Chương trình của Hãng", "Bán chéo ngành hàng", 1500, "Microsoft 365 bundle laptop", 10),
    ("Laptop Tâm An", "Linh kiện & Ngoại vi", "Intel", "Đặt hàng định kỳ", "AI gợi ý từ dữ liệu PO",
     "Bán thêm sản lượng", 700, "Intel AI PC Retail Kit", 7),
]

XSELL_NOTE = {
    "Phát hiện cơ hội": "Chưa tiếp cận, chờ Sales xác nhận gợi ý.",
    "Tư vấn ngành hàng": "Đã giới thiệu danh mục và chính sách; đại lý cần thêm demo sản phẩm tại cửa hàng.",
    "Đại lý đặt thử": "Đại lý đồng ý nhập lô thử, cần hỗ trợ POSM và đào tạo nhân viên bán hàng.",
    "Đặt hàng định kỳ": "Đã có 2 PO liên tiếp, chuyển sang theo dõi sản lượng hàng tháng.",
}


def build_xsell(accounts, contacts):
    by_name = {a["Account name"]: a for a in accounts}
    first_contact = {}
    for c in contacts:
        first_contact.setdefault(c["Account"], c)
    deals = []
    for acc, nganh, hang, stage, nguon, loai, sl, ct, close in XSELL:
        a = by_name[acc]
        owner = a["Account owner"] or ("SALES_BAC" if a["Khu vực"] != "Miền Nam" else "SALES_NAM")
        sl_vnd = sl * TR
        passed_trial = XSELL_STAGES.index(stage) >= XSELL_STAGES.index("Đại lý đặt thử")
        deals.append({
            "Deal name": f"{acc} – Mở ngành {nganh} {hang}",
            "Stage": stage,
            "Deal value": sl_vnd * 6,  # gia tri cam ket 6 thang dau
            "Currency": "VND",
            "Account": acc,
            "Contact": first_contact[acc]["Contact name"],
            "Deal owner": owner,
            "Probability": XSELL_PROB[stage],
            "Expected close date": d(close),
            "Overview": f"Đại lý chưa mua {nganh}. Mục tiêu sản lượng ~{sl} triệu/tháng qua chương trình {ct}.",
            "Loại cơ hội": loai,
            "Nguồn cơ hội": nguon,
            "Ngành hàng mục tiêu": nganh,
            "Hãng mục tiêu": hang,
            "Chương trình áp dụng": ct,
            "Sản lượng dự kiến/tháng (VND)": sl_vnd,
            "Kết quả thăm đại lý": XSELL_NOTE[stage],
            "Ngày đặt thử": d(-rnd.randint(5, 30)) if passed_trial else None,
            "Giá trị đơn đặt thử (VND)": round_m(sl_vnd * rnd.uniform(0.3, 0.6)) if passed_trial else None,
            "Mã PO đầu tiên": f"PO-26{rnd.randint(100000, 999999)}" if passed_trial else None,
            "Bước tiếp theo": NEXT_X[stage],
            "Hạn bước tiếp theo": d(rnd.choice([-2, 0, 1, 3, 6])),
        })
    return deals


NEXT_X = {
    "Phát hiện cơ hội": "Gọi chủ đại lý giới thiệu chương trình",
    "Tư vấn ngành hàng": "Mang hàng demo xuống cửa hàng",
    "Đại lý đặt thử": "Kiểm tra sell-out lô thử sau 2 tuần",
    "Đặt hàng định kỳ": "Đề xuất mức sản lượng cam kết quý sau",
}


# ---------------------------------------------------------------------------
# MA TRAN NGANH HANG (doanh so 12 thang theo Account x nganh) — nguon cho Dataset/Agent
# ---------------------------------------------------------------------------
def build_matrix(accounts):
    rows = []
    for a in accounts:
        if a["Mảng kinh doanh"] != "Kênh Đại lý":
            continue
        buys = a["Ngành hàng đang mua"]
        weights = [rnd.uniform(1, 4) for _ in buys]
        wsum = sum(weights)
        row = {"Account name": a["Account name"], "Hạng đại lý": a["Hạng đại lý"]}
        for n in NGANH:
            row[n] = round_m(a["Doanh số 12 tháng (VND)"] * weights[buys.index(n)] / wsum) if n in buys else 0
        rows.append(row)
    return rows


def build_all():
    accounts = build_accounts()
    contacts = build_contacts(accounts)
    return {
        "accounts": accounts,
        "contacts": contacts,
        "deals_b2g": build_b2g(accounts, contacts),
        "deals_xsell": build_xsell(accounts, contacts),
        "matrix": build_matrix(accounts),
    }
