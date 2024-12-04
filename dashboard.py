import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# baca dataset
day_data = pd.read_csv('data/day.csv')
hour_data = pd.read_csv('data/hour.csv')

# ubah tipe data dteday menjadi datetime
day_data['dteday'] = pd.to_datetime(day_data['dteday'])
hour_data['dteday'] = pd.to_datetime(hour_data['dteday'])

# mengganti nilai numerik pada beberapa kolom di dataset (day_data dan hour_data) dengan label yang lebih mudah dipahami
season_mapping = {1: 'Spring', 2: 'Summer', 3: 'Fall', 4: 'Winter'}
weather_mapping = {1: 'Clear/Few Clouds', 2: 'Mist/Cloudy', 3: 'Light Snow/Rain', 4: 'Heavy Rain/Snow'}
weekday_mapping = {0: 'Sunday', 1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday', 5: 'Friday', 6: 'Saturday'}

day_data['season'] = day_data['season'].map(season_mapping)
hour_data['season'] = hour_data['season'].map(season_mapping)
day_data['weathersit'] = day_data['weathersit'].map(weather_mapping)
hour_data['weathersit'] = hour_data['weathersit'].map(weather_mapping)
day_data['weekday'] = day_data['weekday'].map(weekday_mapping)
hour_data['weekday'] = hour_data['weekday'].map(weekday_mapping)

# streamlit dashboard setup
st.title("Dashboard Analisis Sepeda")
st.sidebar.title("Menu")

# Fitur interaktif untuk filter data
st.sidebar.subheader("Filter Data")
start_date = st.sidebar.date_input("Pilih Tanggal Mulai", day_data['dteday'].min())
end_date = st.sidebar.date_input("Pilih Tanggal Akhir", day_data['dteday'].max())

# filter data berdasarkan tanggal
filtered_data = day_data[(day_data['dteday'] >= pd.to_datetime(start_date)) & (day_data['dteday'] <= pd.to_datetime(end_date))]

# pilihan untuk memilih visualisasi
visualization = st.sidebar.selectbox("Pilih Visualisasi", (
    "Distribusi Penyewaan Sepeda Berdasarkan Musim",
    "Pola Penyewaan Sepeda Berdasarkan Hari",
    "Pengaruh Cuaca terhadap Penyewaan Sepeda",
    "Penyewaan Sepeda Berdasarkan Jam",
    "Analisis RFM"
))

# menambahkan filter tambahan untuk visualisasi lainnya (Season, Weather, Weekday)
if visualization != "Penyewaan Sepeda Berdasarkan Jam":
    season_filter = st.sidebar.multiselect("Pilih Musim", options=filtered_data['season'].unique(), default=filtered_data['season'].unique())
    weather_filter = st.sidebar.multiselect("Pilih Cuaca", options=filtered_data['weathersit'].unique(), default=filtered_data['weathersit'].unique())
    weekday_filter = st.sidebar.multiselect("Pilih Hari dalam Minggu", options=filtered_data['weekday'].unique(), default=filtered_data['weekday'].unique())
    
    filtered_data = filtered_data[
        (filtered_data['season'].isin(season_filter)) & 
        (filtered_data['weathersit'].isin(weather_filter)) &
        (filtered_data['weekday'].isin(weekday_filter))
    ]

# menampilkan subjudul yang berubah sesuai pilihan
if visualization == "Distribusi Penyewaan Sepeda Berdasarkan Musim":
    st.subheader("Distribusi Penyewaan Sepeda Berdasarkan Musim")
elif visualization == "Pola Penyewaan Sepeda Berdasarkan Hari":
    st.subheader("Pola Penyewaan Sepeda Berdasarkan Hari dalam Seminggu")
elif visualization == "Pengaruh Cuaca terhadap Penyewaan Sepeda":
    st.subheader("Pengaruh Kondisi Cuaca terhadap Penyewaan Sepeda")
elif visualization == "Penyewaan Sepeda Berdasarkan Jam":
    st.subheader("Penyewaan Sepeda Berdasarkan Jam dalam Sehari")
elif visualization == "Analisis RFM":
    st.subheader("Analisis Recency, Frequency, dan Monetary (RFM)")

# visualisasi sesuai pilihan
if visualization == "Distribusi Penyewaan Sepeda Berdasarkan Musim":
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.boxplot(data=filtered_data, x='season', y='cnt', palette='Set3', ax=ax)
    ax.set_title('Distribusi Penyewaan Sepeda Berdasarkan Musim')
    ax.set_ylabel('Jumlah Penyewaan')
    ax.set_xlabel('Musim')
    st.pyplot(fig)

elif visualization == "Pola Penyewaan Sepeda Berdasarkan Hari":
    fig, ax = plt.subplots(figsize=(10, 6))
    weekday_counts = filtered_data.groupby('weekday')['cnt'].mean().reindex(
        ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    )
    weekday_counts.plot(kind='bar', color='skyblue', ax=ax)
    ax.set_title('Rata-rata Penyewaan Sepeda Berdasarkan Hari')
    ax.set_ylabel('Rata-rata Penyewaan')
    ax.set_xlabel('Hari dalam Minggu')
    ax.tick_params(axis='x', rotation=45)
    st.pyplot(fig)

elif visualization == "Pengaruh Cuaca terhadap Penyewaan Sepeda":
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(data=filtered_data, x='weathersit', y='cnt', palette='coolwarm', ci=None, ax=ax)
    ax.set_title('Pengaruh Kondisi Cuaca terhadap Penyewaan Sepeda')
    ax.set_ylabel('Jumlah Penyewaan')
    ax.set_xlabel('Kondisi Cuaca')
    ax.tick_params(axis='x', rotation=45)
    st.pyplot(fig)

elif visualization == "Penyewaan Sepeda Berdasarkan Jam":
    fig, ax = plt.subplots(figsize=(10, 6))
    hourly_avg = hour_data.groupby('hr')['cnt'].mean()
    hourly_avg.plot(color='orange', ax=ax)
    ax.set_title('Rata-rata Penyewaan Sepeda Berdasarkan Jam dalam Sehari')
    ax.set_ylabel('Jumlah Penyewaan')
    ax.set_xlabel('Jam')
    ax.grid()
    ax.set_xticks(range(0, 24))
    st.pyplot(fig)

elif visualization == "Analisis RFM":
    rfm_data = filtered_data.groupby('mnth').agg(
        recency=('dteday', lambda x: (filtered_data['dteday'].max() - x.max()).days),
        frequency=('cnt', 'count'),
        monetary=('cnt', 'sum')
    ).reset_index()

    # visualisasi RFM
    fig, axes = plt.subplots(1, 3, figsize=(12, 6))

    # Recency
    sns.barplot(data=rfm_data, x='mnth', y='recency', palette='viridis', ax=axes[0])
    axes[0].set_title('Recency Berdasarkan Bulan')
    axes[0].set_xlabel('Bulan')
    axes[0].set_ylabel('Recency (Hari)')

    # Frequency
    sns.barplot(data=rfm_data, x='mnth', y='frequency', palette='viridis', ax=axes[1])
    axes[1].set_title('Frequency Berdasarkan Bulan')
    axes[1].set_xlabel('Bulan')
    axes[1].set_ylabel('Frequency (Jumlah Hari)')

    # Monetary
    sns.barplot(data=rfm_data, x='mnth', y='monetary', palette='viridis', ax=axes[2])
    axes[2].set_title('Monetary Berdasarkan Bulan')
    axes[2].set_xlabel('Bulan')
    axes[2].set_ylabel('Monetary (Jumlah Penyewaan)')

    plt.tight_layout()
    st.pyplot(fig)

    # clustering monetary
    bins = [0, 200000, 300000, rfm_data['monetary'].max() + 1]
    labels = ['Low', 'Medium', 'High']
    rfm_data['monetary_cluster'] = pd.cut(rfm_data['monetary'], bins=bins, labels=labels)

    fig, ax = plt.subplots(figsize=(8, 6))
    sns.countplot(data=rfm_data, x='monetary_cluster', palette='cool', ax=ax)
    ax.set_title('Clustering Berdasarkan Monetary Value')
    ax.set_xlabel('Cluster')
    ax.set_ylabel('Jumlah Bulan')
    st.pyplot(fig)