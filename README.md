# 🧹 Customer Data Cleaner — تنظيف بيانات العملاء

> **Python script that automatically cleans messy customer CSV files — names, phones, emails, cities, dates, duplicates.**

---

## 📌 المشكلة | The Problem

بيانات العملاء المجمّعة من مصادر متعددة تصبح فوضوية وغير قابلة للاستخدام:

| المشكلة | مثال |
|---------|------|
| مسافات زائدة في الأسماء | `··Ahmed Mohamed··` |
| أرقام هواتف بصيغ مختلفة | `002011234567` / `0111234567` / `+20111234567` |
| إيميلات غير موحدة | `AHMED@GMAIL.COM` / `ahmed @ gmail.com` |
| نفس المدينة بكتابات مختلفة | `cairo` / `Cairo` / `القاهره` / `القاهرة` |
| تواريخ بصيغ مختلفة | `5/3/2023` / `2023-03-05` / `03-05-2023` |
| خلايا فارغة وصفوف مكررة | — |

---

## ✅ الحل | The Solution

```
Input:  customers_raw.csv   (messy)
Output: customers_clean.csv (standardized) + cleaning_report.txt
```

| العمود | قبل | بعد |
|--------|-----|-----|
| Name | `··AHMED MOHAMED··` | `Ahmed Mohamed` |
| Phone | `002011234567` | `+20111234567` |
| Email | `AHMED@GMAIL.COM` | `ahmed@gmail.com` |
| City | `القاهره` | `Cairo` |
| Join_Date | `5/3/2023` | `2023-03-05` |
| Status | `ACTIVE` / _(empty)_ | `active` / `unknown` |

---

## 📂 Project Structure

```
2026-02_cleaning_customers-data/
├── inputs/
│   └── customers_raw.csv        ← dirty data (input)
├── outputs/
│   ├── customers_clean.csv      ← clean data (output)
│   └── cleaning_report.txt      ← what changed
└── scripts/
    └── clean_customers_data.py  ← main script
```

---

## ⚙️ How to Run

```bash
pip install pandas dateparser
python scripts/clean_customers_data.py
```

---

## 📊 Sample Report Output

```
========== Final Report ==========
Original rows   : 52
Clean rows      : 48
Deleted rows    : 4
Missing cells   : 11
==================================
```

---

## 🛠️ Tech Stack

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Pandas](https://img.shields.io/badge/Pandas-2.0-green)
![Dateparser](https://img.shields.io/badge/Dateparser-1.1-orange)

---

## 💼 هل عندك ملف مشابه؟

إذا كان عندك ملف بيانات يعاني من نفس المشاكل، أرسل لي:
- الملف (CSV أو Excel)
- وصف المشاكل الموجودة

وستحصل على ملف نظيف + تقرير بكل ما تغيّر.
