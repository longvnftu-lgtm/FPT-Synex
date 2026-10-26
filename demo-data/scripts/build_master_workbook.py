# -*- coding: utf-8 -*-
"""Xuat bo du lieu demo goc ra 1 file Excel de doc/duyet (KHONG phai file import).

Chay: python demo-data/scripts/build_master_workbook.py
"""
import json
import os
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import demo_master as m  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "Dữ liệu setup", "CRM Sale", "Bộ dữ liệu demo Synnex FPT (dữ liệu gốc).xlsx")
SPEC = os.path.join(ROOT, "scripts", "_specs", "master.json")
WRITER = os.path.join(ROOT, "scripts", "write_import_excel.py")
LIST_SEP = "; "


def cell(v):
    return LIST_SEP.join(v) if isinstance(v, list) else v


def sheet(name, records, extra=None):
    keys = [k for k in records[0] if not k.startswith("_")]
    headers = keys + (list(extra) if extra else [])
    rows = []
    for r in records:
        row = [cell(r[k]) for k in keys]
        if extra:
            row += [fn(r) for fn in extra.values()]
        rows.append(row)
    return {"sheet_name": name, "headers": headers, "rows": rows}


STORY_LABEL = {
    "STORY_XSELL": "Câu chuyện 1 · Key Account chưa mua Thiết bị mạng",
    "STORY_CREDIT": "Cảnh báo công nợ sát hạn mức",
    "STORY_CHURN": "Agent cảnh báo sụt doanh số",
    "STORY_ZALO": "Câu chuyện 3 · Đại lý SME hỏi qua Zalo OA",
}


def main():
    data = m.build_all()
    personas = [{"Mã persona": k, "Vai trò": v, "Username Base (điền)": None} for k, v in m.PERSONAS.items()]
    spec = {
        "output": OUT,
        "profile": "crm",
        "sheets": [
            sheet("Accounts", data["accounts"],
                  {"Câu chuyện demo": lambda r: STORY_LABEL.get(r["_story"])}),
            sheet("Contacts", data["contacts"],
                  {"Liên hệ chính": lambda r: "Có" if r["_primary"] else None}),
            sheet("Deals Dự án B2G", data["deals_b2g"]),
            sheet("Deals Bán chéo", data["deals_xsell"]),
            sheet("Ma trận ngành hàng", data["matrix"]),
            sheet("Personas", personas),
        ],
    }
    os.makedirs(os.path.dirname(SPEC), exist_ok=True)
    with open(SPEC, "w", encoding="utf-8") as fh:
        json.dump(spec, fh, ensure_ascii=False, indent=1)
    sys.exit(subprocess.run([sys.executable, WRITER, "--spec", SPEC]).returncode)


if __name__ == "__main__":
    main()
