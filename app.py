import streamlit as st

st.title("GIẢI PHƯƠNG TRÌNH BẬC NHẤT")
a = st.number_input("Tham số a")
b = st.number_input("Tham số b")
if st.button("Giải"):
  st.success(f"Phương trình có nghiệm {-b/a}")
