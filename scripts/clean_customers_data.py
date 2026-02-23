import pandas as pd
import dateparser
import re

# ===================== Read File =====================

df = pd.read_csv(r"2026-02_cleaning_customers-data\inputs\customers_raw.csv")

# ===================== Strip Spaces & Empty Strings =====================

df = df.map(lambda x: x.strip() if isinstance(x, str) else x)
df = df.map(lambda x: pd.NA if x == "" else x)

# ===================== Stats Before Cleaning =====================

original_row_count = len(df)
missing_cells_count = df.isna().sum().sum()

# ===================== Name =====================

df["Name"] = df["Name"].str.title()

# ===================== Phone =====================

def clean_phone(phone):
    if pd.isna(phone):
        return "invalid"
    digits = re.sub(r'\D', '', str(phone))   # أزل كل شيء غير رقم
    last_10 = digits[-10:]                    # خذ آخر 10 أرقام
    if len(last_10) == 10 and last_10[0] == '1':
        return f"+20{last_10}"
    return "invalid"

df["Phone"] = df["Phone"].map(clean_phone)

# ===================== Email =====================

def clean_email(email):
    if not isinstance(email, str):
        return "invalid"
    email = email.replace(" ", "").lower()
    if re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", email):
        return email
    return "invalid"

df["Email"] = df["Email"].map(clean_email)

# ===================== City =====================

city_map = {
    "alex": "Alexandria",
    "alexandria": "Alexandria",
    "الإسكندرية": "Alexandria",
    "الاسكندرية": "Alexandria",
    "asyut": "Asyut",
    "أسيوط": "Asyut",
    "اسيوط": "Asyut",
    "cairo": "Cairo",
    "القاهرة": "Cairo",
    "القاهره": "Cairo",
    "giza": "Giza",
    "الجيزة": "Giza",
    "الجيزه": "Giza",
    "mansoura": "Mansoura",
    "المنصورة": "Mansoura",
    "المنصوره": "Mansoura",
    "tanta": "Tanta",
    "طنطا": "Tanta",
}

df["City"] = df["City"].str.lower().map(city_map).fillna("unknown")

# ===================== Join_Date =====================

df["Join_Date"] = df["Join_Date"].apply(dateparser.parse)
df["Join_Date"] = pd.to_datetime(df["Join_Date"]).dt.strftime("%Y-%m-%d")

# ===================== Status =====================

df["Status"] = df["Status"].fillna("unknown")
df["Status"] = df["Status"].str.lower()

# ===================== Drop Duplicates =====================

df = df.drop_duplicates()
clean_row_count = len(df)

# ===================== Save =====================

df.to_csv(r"2026-02_cleaning_customers-data\outputs\customers_clean.csv", index=False)

# ===================== Report =====================

print(f'{"  Final Report  ":=^40}')
print(f"Original rows   : {original_row_count}")
print(f"Clean rows      : {clean_row_count}")
print(f"Deleted rows    : {original_row_count - clean_row_count}")
print(f"Missing cells   : {missing_cells_count}")
print("=" * 40)