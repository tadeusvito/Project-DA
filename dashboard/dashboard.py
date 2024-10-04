import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Set up custom layout
st.set_page_config(layout="wide", page_title="Data Analyst Bike Dataset")

# Custom CSS for styling
st.markdown("""
    <style>
    /* General Layout */
    .main {
        background-color: #f8f9fa;
        padding: 10px;
    }
    /* Header styling */
    .stApp h1 {
        font-family: 'Montserrat', sans-serif;
        font-size: 2.5rem;
        color: #264653;
        text-align: center;
        margin-top: 20px;
    }
    /* Custom Info box */
    .stAlert {
        background-color: #2a9d8f; /* Change background color to dark */
        color: white; /* Change text color to white for better readability */
        font-size: 1.5rem; /* Increase font size */
        text-align: center; /* Center the text */
        padding: 20px; /* Add more padding for space */
        border-radius: 8px; /* Rounded corners */
        border-left: 4px solid #264653; /* Custom border */
    }
    /* Table expander */
    .st-expander {
        background-color: #f1faee;
        border: 1px solid #a8dadc;
        padding: 10px;
        border-radius: 8px;
        margin-bottom: 15px;
    }
    /* Justify text */
    .justify {
        text-align: justify;
    }
    /* Plot styling */
    .matplotlib-plot {
        border: 1px solid #8d99ae;
        padding: 20px;
        background-color: #edf2f4;
        border-radius: 8px;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🚲 Data Analyst Bike Sharing Dataset")

# Info Box Styling
st.info("Analisis data sederhana dengan Google Colab menggunakan Bike Sharing Dataset")

# Layout setup with two columns for data and question
col1, col2 = st.columns([1, 2])

# Data Section in the first column
with col1:
    st.subheader("Data yang sudah bersih")

    with st.expander('Lihat Data day.csv'):
        day_df = pd.read_csv('dashboard/day.csv')
        st.dataframe(day_df, height=150)
    
    with st.expander('Lihat Data hour.csv'):
        hour_df = pd.read_csv('dashboard/hour.csv')
        st.dataframe(hour_df, height=150)

# Question and Visualization Section in the second column
with col2:
    st.subheader("Analisis dan Visualisasi")

    # Question Selector
    question = st.selectbox("Pilih Pertanyaan", ["Pertanyaan 1", "Pertanyaan 2"])

    # Question 1
    if question == "Pertanyaan 1":
        st.header("Bagaimana suhu mempengaruhi jumlah rental sepeda?")
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.regplot(x='temp', y='cnt', data=day_df, scatter_kws={'s':10}, line_kws={"color": "red"})
        ax.set_title('Hubungan antara Suhu dan Jumlah Rental Sepeda', fontsize=14)
        ax.set_xlabel('Suhu', fontsize=12)
        ax.set_ylabel('Jumlah Rental Sepeda', fontsize=12)
        ax.grid(True)
        st.pyplot(fig, clear_figure=True)

        # Display Conclusion directly
        st.subheader("Kesimpulan Pertanyaan 1")
        st.write("Berdasarkan plot hubungan antara suhu dan jumlah rental sepeda, terlihat bahwa terdapat korelasi positif antara suhu dan jumlah persewaan sepeda. Saat suhu meningkat, jumlah penyewaan sepeda cenderung meningkat, menunjukkan bahwa suhu yang lebih hangat mendorong lebih banyak orang untuk menyewa sepeda. Regresi linier dengan garis merah menunjukkan tren kenaikan yang konsisten, meskipun terdapat beberapa variasi di sekitar garis tersebut, yang menunjukkan adanya faktor lain yang mungkin juga memengaruhi jumlah penyewaan. Secara keseluruhan, suhu tampaknya menjadi salah satu faktor penting yang mempengaruhi keputusan orang untuk menyewa sepeda.")

    # Question 2
    elif question == "Pertanyaan 2":
        st.header("Bagaimana pola persewaan sepeda berdasarkan suhu dan waktu?")
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.scatterplot(x='hr', y='cnt', hue='temp', data=hour_df, palette="coolwarm", ax=ax)
        ax.set_title('Pola Persewaan Sepeda Berdasarkan Suhu dan Waktu', fontsize=14)
        ax.set_xlabel('Waktu Persewaan', fontsize=12)
        ax.set_ylabel('Jumlah Rental Sepeda', fontsize=12)
        ax.grid(True)
        st.pyplot(fig, clear_figure=True)

        # Display Conclusion directly
        st.subheader("Kesimpulan Pertanyaan 2")
        st.write("Persewaan sepeda cenderung mencapai puncaknya pada waktu tertentu, terutama pada sore hingga malam hari (sekitar pukul 17:00 hingga 19:00), yang kemungkinan terkait dengan waktu pulang kerja atau aktivitas rutin sore hari. Selain itu, suhu yang lebih tinggi (terlihat dari perbedaan warna) juga berhubungan dengan jumlah rental sepeda yang lebih besar. Persewaan sepeda pada suhu yang hangat dan pada jam sibuk (seperti sore hari) cenderung lebih tinggi, menegaskan bahwa faktor waktu dan kondisi cuaca memainkan peran penting dalam jumlah penyewaan sepeda.")
