import streamlit as st
import pandas as pd
import joblib

# Load model regresi
model = joblib.load('regresi.pkl')

# Judul aplikasi
st.title('Prediksi Income Berdasarkan Usia dan Pengalaman')

# Input data dari user
st.header('Masukkan Data')
new_age = st.number_input('Masukkan nilai Age (Usia):', min_value=0.0, step=1.0)
new_experience = st.number_input('Masukkan nilai Experience (Pengalaman):', min_value=0.0, step=1.0)

# Tombol prediksi
if st.button('Prediksi Income'):
    try:
        # Buat DataFrame dari input baru
        new_data_df = pd.DataFrame([[new_age, new_experience]], columns=['Age', 'Experience'])

        # Lakukan prediksi
        predicted_income = model.predict(new_data_df)

        # Tampilkan hasil prediksi
        st.success(f'Untuk Age = {new_age} dan Experience = {new_experience}, prediksi Income adalah: ${predicted_income[0][0]:,.2f}')
    
    except Exception as e:
        st.error(f'Terjadi kesalahan: {e}')
