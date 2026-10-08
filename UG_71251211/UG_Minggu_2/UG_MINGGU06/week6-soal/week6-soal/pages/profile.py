import streamlit as st
from user import user_data_by_username

# CEK APAKAH SUDAH LOGIN
if "logged_in" not in st.session_state or not st.session_state.logged_in:
    st.switch_page("app.py")  

username = st.session_state.username
user = user_data_by_username()
user_data = user[username]

# hint untuk mematikan text input ada di -> https://docs.streamlit.io/develop/api-reference/widgets/st.text_input
# BUAT 2 INPUT TEXT 1 Username 1 Password namun disable/matikan field Username dan yang password harus tipe password
st.title("Profile")
username = st.text_input("Username", value=username, disabled=True)
password_lama = st.text_input("Password lama", type="password")
password_baru = st.text_input("Password baru", type="password")

# Silahkan kalau mau baca baca ini hehe ga wajib ya-> https://discuss.streamlit.io/t/buttons-alignment/51929
col1, space, col2 = st.columns([1,3,1])

with col1:
    # Buat tombol logout st.button("logout", type="primary") keluar ke app.py
    if st.button("logout", type="primary"):
        st.session_state.logged_in = False
        st.session_state.username = None
        st.session_state.password = None
        st.switch_page("app.py")
        st.rerun()
        
with col2:
    if st.button("Ganti data", type="secondary", width=400):

        # Kondisi -> Password lama harus sesuai dengan password yang tersimpan
        if password_lama != user_data["password"]:
            st.error("Password lama salah")

        # Kondisi -> Password baru dan lama ga boleh sama
        elif password_baru == password_lama:
            st.error("Password baru tidak boleh sama dengan password lama")

        # Password baru tidak boleh kosong
        elif password_baru == "":
            st.error("Password baru tidak boleh kosong")

        else:
            user_data["password"] = password_baru
            st.session_state.password = password_baru
            st.success("Berhasil")

    # Ini untuk ubah password st.button("Ganti Data", type="secondary", width=400)
    # Kondisi -> Password baru dan lama ga boleh sama 
    # Jika sama -> st.error("ga boleh sama wok")
    # jika beda ubah melalui variabel 'user' lalu tampilkan st.success("Berhasil")