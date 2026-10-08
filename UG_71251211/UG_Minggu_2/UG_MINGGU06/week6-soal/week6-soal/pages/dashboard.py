import streamlit as st
from user import user_data_by_username

st.set_page_config(page_title="DwTix - Dashboard")

# cek apakah sudah login -> JIKA BELUM ALIHKAN KE app.py

# JANGAN PERNAH RAGU UNTUK CEK DATA PAKAI st.write() ya dari pada ngawang
data = user_data_by_username()
# ambil role yang login dari data
# role = ??

# JIKA YANG LOGIN PESERTA -> ALIHKAN KE PAGE EVENT

st.title(f"Welcome, {role} 👋")

# JIKA YANG LOGIN ADMIN TAMPILKAN SELURUH DATA TERSERAH MAU BENTUKNYA APAPUN st.table, st.write boleh aja