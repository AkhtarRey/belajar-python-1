import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Judul Dashboard
st.title('Dashboard Analisis Kualitas Udara (Huairou)')

# Memanggil Data dari CSV lokal
df = pd.read_csv('all_data.csv')

# Menampilkan Head Data
if st.checkbox('Show DataFrame'):
    st.write(df)

# Analisis Data
st.header('Analisis Data')

# Korelasi antara CO dan TEMP
corr_co_temp = df[['CO', 'TEMP']].corr()
st.write('Korelasi antara CO dan TEMP adalah:', corr_co_temp.loc['CO', 'TEMP'])

# Visualisasi Korelasi
fig, ax = plt.subplots()

karbon = df.groupby("year").agg({"CO":"mean"})
suhu = df.groupby("year").agg({"TEMP": "mean"})

sns.regplot(x=karbon, y=suhu, data=df, ax=ax)
st.pyplot(fig)

# Analisis Trend CO dari Tahun 2013-2017
st.header('Trend Karbon Monoksida (CO) dari Tahun 2013-2017')
karbon = df.groupby("year").agg({"CO":"mean"})
suhu = df.groupby("year").agg({"TEMP": "mean"})

# Menampilkan Plot Tren CO
fig2, ax2 = plt.subplots()
sns.lineplot(data=karbon, x=karbon.index, y='CO', ax=ax2)
plt.xticks(df['year'].unique())
st.pyplot(fig2)

# Kesimpulan
st.header('Kesimpulan')
st.write("""
- Pengaruh Karbon Monoksida terhadap Temperatur/Suhu Udara di Huairou adalah -26%, yang berarti berpengaruh kecil dan negatif (apabila karbon meningkat maka suhu turun).
- Trend Karbon Monoksida di Huairou stabil dari Tahun 2013-2015 dan menurun signifikan pada 2016 lalu meningkat signifikan pada 2017.
""")