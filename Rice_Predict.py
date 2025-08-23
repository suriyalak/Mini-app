import streamlit as st

st.set_page_config(
    page_title="SGR Rice Predict"
)

st.title('Smart Farm AR 🌱')
st.image('image2.png')

st.text('กรอกข้อมูลโรคข้าวที่ต้องการให้ทำนาย')
with st.form('โรคข้าว'):
    st.text('กรอกข้อมูลให้ครบถ้วน')
    st.text_input('สายพันธุ์')
    st.text_input('อายุข้าว (วัน)',max_chars=3)
    st.text_input('ลักษณะอาการ')
    st.text_input('ระยะเวลาที่เกิด (วัน)',max_chars=3)
    st.file_uploader('เลือกรูปภาพ',)
        
    st.form_submit_button('submit')

cols = st.columns(4)
with cols[0]:
    st.page_link("Home.py", label="Home", icon="🌾")

with cols[1]:
    st.page_link("pages/Rice_Predict.py", label="Rice Prediction", icon="🌾")

with cols[2]:
    st.page_link("pages/Rice_Scanner.py", label="Rice Scanner", icon="🌾")
