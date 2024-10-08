import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Function to read CSV data
def read_data(filename):
    return pd.read_csv(filename)

# Function to plot temperature vs count
def plot_temp_vs_cnt(df):
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.regplot(x='temp', y='cnt', data=df, scatter_kws={'s':10}, line_kws={"color": "red"})
    ax.set_title('Hubungan antara Suhu dan Jumlah Rental Sepeda', fontsize=14)
    ax.set_xlabel('Suhu', fontsize=12)
    ax.set_ylabel('Jumlah Rental Sepeda', fontsize=12)
    ax.grid(True)
    return fig

# Function to plot rental pattern based on temperature and time
def plot_rental_pattern(df):
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.scatterplot(x='hr', y='cnt', hue='temp', data=df, palette="coolwarm", ax=ax)
    ax.set_title('Pola Persewaan Sepeda Berdasarkan Suhu dan Waktu', fontsize=14)
    ax.set_xlabel('Waktu Persewaan', fontsize=12)
    ax.set_ylabel('Jumlah Rental Sepeda', fontsize=12)
    ax.grid(True)
    return fig

# Set up custom layout
st.set_page_config(layout="wide", page_title="Data Analyst Bike Dataset")

# Custom CSS for styling
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
        font-family: 'Arial', sans-serif; /* Changed to Arial */
        font-size: 3rem; /* Increased font size */
        color: #2a9d8f; /* Changed header color */
        text-align: center;
        margin-top: 40px; /* Increased top margin */
        padding: 20px; /* Added padding around the header */
        background-color: #264653; /* Dark background for header */
        border-radius: 8px; /* Rounded corners for header */
    }
    /* Custom Info box */
    .stAlert {
        background-color: #2a9d8f;
        color: white;
        font-size: 1.5rem;
        text-align: center;
        padding: 20px;
        border-radius: 8px;
        border-left: 4px solid #264653;
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
        day_df = read_data('dashboard/day.csv')
        st.dataframe(day_df, height=150)
    
    with st.expander('Lihat Data hour.csv'):
        hour_df = read_data('dashboard/hour.csv')
        st.dataframe(hour_df, height=150)

# Question and Visualization Section in the second column
with col2:
    st.subheader("Analisis dan Visualisasi")

    # Question Selector
    question = st.selectbox("Pilih Pertanyaan", ["Pertanyaan 1", "Pertanyaan 2"])

    # Question 1
    if question == "Pertanyaan 1":
        st.header("Bagaimana suhu mempengaruhi jumlah rental sepeda?")
        fig = plot_temp_vs_cnt(day_df)
        st.pyplot(fig)

        # Display Conclusion directly
        st.subheader("Kesimpulan Pertanyaan 1")
        st.write("Berdasarkan plot hubungan antara suhu dan jumlah rental sepeda, terlihat bahwa terdapat korelasi positif antara suhu dan jumlah persewaan sepeda. Saat suhu meningkat, jumlah penyewaan sepeda cenderung meningkat, menunjukkan bahwa suhu yang lebih hangat mendorong lebih banyak orang untuk menyewa sepeda. Regresi linier dengan garis merah menunjukkan tren kenaikan yang konsisten, meskipun terdapat beberapa variasi di sekitar garis tersebut, yang menunjukkan adanya faktor lain yang mungkin juga memengaruhi jumlah penyewaan. Secara keseluruhan, suhu tampaknya menjadi salah satu faktor penting yang mempengaruhi keputusan orang untuk menyewa sepeda.")

    # Question 2
    elif question == "Pertanyaan 2":
        st.header("Bagaimana pola persewaan sepeda berdasarkan suhu dan waktu?")
        fig = plot_rental_pattern(hour_df)
        st.pyplot(fig)

        # Display Conclusion directly
        st.subheader("Kesimpulan Pertanyaan 2")
        st.write("Persewaan sepeda cenderung mencapai puncaknya pada waktu tertentu, terutama pada sore hingga malam hari (sekitar pukul 17:00 hingga 19:00), yang kemungkinan terkait dengan waktu pulang kerja atau aktivitas rutin sore hari. Selain itu, suhu yang lebih tinggi (terlihat dari perbedaan warna) juga berhubungan dengan jumlah rental sepeda yang lebih besar. Persewaan sepeda pada suhu yang hangat dan pada jam sibuk (seperti sore hari) cenderung lebih tinggi, menegaskan bahwa faktor waktu dan kondisi cuaca memainkan peran penting dalam jumlah penyewaan sepeda.")
