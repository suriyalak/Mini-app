import streamlit as st
import pandas as pd
import numpy as np
import time
import os

##First Page
#Title name
st.title('โปรแกรมแสดงตำแหน่งบนแผนที่')

#์Name Age and School
column_name, column_age = st.columns(2)
column_name.text_input("ชื่อ", key="name")

with column_age:
     column_age.text_input('อายุ', key='age')

st.text_input('โรงเรียน', key='school')

# สร้างปุ่มสำหรับบันทึกข้อมูล
if st.button('ต่อไป'):
    # ตรวจสอบว่ามีข้อมูลครบถ้วนหรือไม่
    if st.session_state.name and st.session_state.age and st.session_state.school:
        # สร้าง DataFrame จากข้อมูลที่ผู้ใช้ป้อน
        student_data = {
            'ชื่อ': [st.session_state.name],
            'อายุ': [st.session_state.age],
            'โรงเรียน': [st.session_state.school]
        }
        
        student_df = pd.DataFrame(student_data)
        
        # --- จัดการไฟล์ CSV และการกำหนดลำดับ ---
        # กำหนดชื่อโฟลเดอร์และชื่อไฟล์
        test_app = 'student_data'
        csv_file_path = os.path.join(test_app, 'student_data.csv')
        
        # สร้างโฟลเดอร์ 'data' ถ้ายังไม่มี
        if not os.path.exists(test_app):
            os.makedirs(test_app)
        
        # ตรวจสอบว่าไฟล์ CSV มีอยู่แล้วหรือไม่
        if os.path.exists(csv_file_path):
            # ถ้ามีอยู่แล้ว ให้อ่านไฟล์เดิมและหาค่าลำดับสูงสุด
            existing_df = pd.read_csv(csv_file_path)
            next_id = existing_df['ลำดับ'].max() + 1
        else:
            # ถ้ายังไม่มีไฟล์ ให้เริ่มลำดับที่ 1
            next_id = 1
            
        # เพิ่มคอลัมน์ 'ลำดับ' และจัดเรียงคอลัมน์ใหม่
        student_df['ลำดับ'] = next_id
        final_df = student_df[['ลำดับ', 'ชื่อ', 'อายุ', 'โรงเรียน']]
        
        # บันทึกข้อมูลลงในไฟล์ CSV โดยการเพิ่มต่อท้าย
        # mode='a' คือการเพิ่มข้อมูลต่อท้าย
        # header=not os.path.exists(csv_file_path) คือการเพิ่มหัวคอลัมน์เฉพาะตอนสร้างไฟล์ครั้งแรก
        final_df.to_csv(csv_file_path, mode='a', header=not os.path.exists(csv_file_path), index=False, encoding='utf-8-sig')
        
        st.success("บันทึกข้อมูลเรียบร้อยแล้ว! ✅")
        
        # แสดงตารางข้อมูลทั้งหมดที่อ่านมาจากไฟล์ CSV
        full_df = pd.read_csv(csv_file_path)
        st.write("---")
        st.write("ข้อมูลนักเรียนทั้งหมด")
        st.dataframe(full_df)
        
    else:
        st.warning("กรุณากรอกข้อมูลให้ครบถ้วนครับ ⚠️")


   
##Secound Page
#Location
st.subheader("ใส่ค่าพิกัดที่ต้องการ")

# สร้าง input field สำหรับรับค่า latitude และ longitude
lat = st.number_input('Latitude', min_value=-90.0, max_value=90.0, value=19.11)
lon = st.number_input('Longitude', min_value=-180.0, max_value=180.0, value=99.52)

# ส่วนของปุ่ม
if st.button('ตกลง'):
    # Loading Bar
    latest_iteration = st.empty()
    bar = st.progress(0)
    
    # สร้าง DataFrame จากค่าที่ผู้ใช้ป้อน
    map_data = pd.DataFrame(
        np.random.randn(1, 2) / [50, 50] + [lat, lon],
        columns=['lat', 'lon']
    )
    
    # แสดงแผนที่
    st.map(map_data)