import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score
import streamlit as st

# membaca model
obesitas_dataset =pd.read_csv('obesitas.csv')

# judul web
st.title('Data Mining Prediksi obesitas')

#memisahkan data dan label
X = obesitas_dataset.drop (columns = ['Index'], axis=1)
Y = obesitas_dataset['Index']

le = LabelEncoder()

# Menggunakan LabelEncoder untuk mengubah kolom 'Gender'
obesitas_dataset['Gender'] = le.fit_transform(obesitas_dataset['Gender'])

# Sekarang kolom 'Gender' berisi 0 dan 1
print(obesitas_dataset)

#membagi kolom
col1, col2 = st.columns(2)

with col1 :
    Weight = st.number_input ('input nilai weidth')

with col2 :
    Height = st.number_input ('input nilai height')

with col1 :
    Gender = st.text_input ('input gender')

# code untuk prediksi
diab_diagnosis = ' '

# membuat tombol untuk prediksi
if st.button ('Test prediksi Berat badan'):
   
        # Membuat objek StandardScaler
        scaler = StandardScaler()

        # Latih scaler pada data latih yang memiliki 3 fitur (Height, Weight, Gender)
        X_train = ['Height', 'Weight', 'Gender']
        scaler.fit(X_train)


        # Sekarang, gunakan scaler untuk mentransformasi data baru
        input_data_as_numpy_array = np.array([input_data])  # Memberikan nama fitur sesuai urutan
        std_data = scaler.transform(input_data_as_numpy_array)

        # Melakukan prediksi pada data yang telah di-scaling
        prediction = model.predict(std_data)

        # Mengekstraksi hasil prediksi
        predicted_class = prediction[0]

        # Menerjemahkan hasil prediksi menjadi label
        if predicted_class == 0:
            print('Sangat kurus')
        elif predicted_class == 1:
            print('kurus')
        elif predicted_class == 2:
            print('Normal')
        elif predicted_class == 3:
            print('Gemuk')
        elif predicted_class == 4:
            print('Obesitas')
        else:
            print('Obesitas akut')

st.success(diab_diagnosis)


