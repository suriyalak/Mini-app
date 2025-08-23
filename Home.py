import streamlit as st


st.title('Smart Farm AR 🌱')
st.subheader("Welcome to my garden")
st.image('image2.png')


st.set_page_config(
    page_title="SFR home"
)

st.write(' ')
st.markdown(
    """
    ##### เกี่ยวกับเรา
    เว็บแอปพลิเคชัน Smart Garden AR ของเรา สร้างขึ้นมาเพื่อตอบปัญหาเกี่ยวกับโรคข้าวที่เกษตรกรต้องเผชิญ
    โดยเว็บของเรานั้นมีฟีเจอร์ที่สามารถระบุอาการข้าวเพื่อทำนายโรคที่เกิดขึ้นกับข้าวและสามารถเพิ่มรูปเพื่อ
    ทำการทำนายโรคข้าว หากไม่ต้องการถ่ายรูปให้เสียเวลา เรายังมีระบบสแกนเพื่อถ่ายรูปข้าวและทำนายผลได้แบบเรียลไทม์
    """
)

cols = st.columns(4)
with cols[0]:
    st.page_link("pages/Rice_Predict.py", label="Rice Prediction", icon="🌾")

with cols[1]:
    st.page_link("pages/Rice_Scanner.py", label="Rice Scanner", icon="🌾")
