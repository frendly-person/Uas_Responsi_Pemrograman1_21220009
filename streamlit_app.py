import streamlit as st

def hitung_luas(Panjang, lebar):
    return panjang * lebar

def hitung_keliling(panjang, lebar) :
    return 2 * panjang + lebar

st.title("Menghitung Luas dan Keliling persegi panjang")

panjang = st.number_input("masukan Panjang", min_value=0.0)
lebar = st.number_input("masukan Lebar", min_value=0.0)

if st.button("Hitung"):
    Luas = hitung_luas(panjang, lebar)
    Keliling = hitung_keliling(panjang, lebar)
    st.write(f"Luas: {Luas}")
    st.write(f"Keiling: {Keliling}")