import streamlit as st

st.set_page_config(
    page_title="SGR Rice Scanner"
)

st.title('Smart Farm AR 🌱')

picture = st.camera_input('ถ่ายรูปข้าวที่ต้องการทำนาย')

if picture:
    st.image(picture)

st.button('submit')


cols = st.columns(4)
with cols[0]:
    st.page_link("Home.py", label="Home", icon="🌾")

with cols[1]:
    st.page_link("pages/Rice_Predict.py", label="Rice Prediction", icon="🌾")

with cols[2]:
    st.page_link("pages/Rice_Scanner.py", label="Rice Scanner", icon="🌾")
