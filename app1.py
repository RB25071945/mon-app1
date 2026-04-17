import streamlit as st

st.title("Ma première app")

col1, col2 = st.columns(2)

with col1:
    if st.button("🟢 Bouton vert"):
        st.success("Hello Word")

with col2:
    if st.button("🔴 Bouton rouge"):
        st.error("Bye")