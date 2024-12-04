# Dashboard Penyewaan Sepeda

Proyek ini menyediakan dashboard interaktif berbasis Streamlit untuk menganalisis data penyewaan sepeda. Dashboard ini mencakup berbagai visualisasi yang memungkinkan pengguna untuk mengeksplorasi hubungan antara penyewaan sepeda dengan berbagai faktor seperti musim, cuaca, hari dalam minggu, dan lainnya.

## Struktur Proyek

Struktur direktori proyek ini adalah sebagai berikut:

```
submission
├───dashboard
| └───dashboard.py
├───data
| ├───day.csv
| └───hour.csv
├───notebook.ipynb
├───README.md
└───requirements.txt
└───url.txt
```

- **dashboard**: Berisi skrip Python untuk dashboard Streamlit (`dashboard.py`) dan dataset utama (`main_data.csv`).
- **data**: Berisi file data mentah `day.csv` dan `hour.csv` yang digunakan untuk analisis.
- **notebook.ipynb**: Jupyter notebook yang berisi pemrosesan data, analisis, dan visualisasi.
- **requirements.txt**: Daftar semua dependensi Python yang diperlukan untuk menjalankan proyek.
- **url.txt**: Berisi URL untuk mengakses aplikasi Streamlit setelah dijalankan.

## Instalasi dan Setup

Untuk menjalankan proyek ini secara lokal, ikuti langkah-langkah berikut:

1. **Clone repositori**:

    ```
    git clone https://github.com/khalidziarabbani/project-dicoding.git
    cd <repository_name>
    ```

2. **Buat virtual environment** (opsional, tapi disarankan):

    Untuk Windows:
    ```
    python -m venv venv
    .\venv\Scripts\activate
    ```

    Untuk macOS/Linux:
    ```
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Instal dependensi**:

    ```
    pip install -r requirements.txt
    ```

4. **Jalankan dashboard Streamlit**:

    ```
    streamlit run dashboard.py
    ```

    Ini akan meluncurkan aplikasi Streamlit di browser default Anda.

## Fitur-Fitur Dashboard

- **Penyewaan Sepeda Berdasarkan Musim**: Memvisualisasikan distribusi penyewaan sepeda di berbagai musim.
- **Dampak Cuaca**: Menunjukkan bagaimana kondisi cuaca mempengaruhi penyewaan sepeda.
- **Pola Penyewaan Mingguan**: Menampilkan rata-rata jumlah penyewaan setiap hari dalam seminggu.
- **Penyewaan Berdasarkan Jam**: Menganalisis penyewaan sepeda berdasarkan jam dalam sehari.
- **Analisis RFM**: Memvisualisasikan recency, frequency, dan monetary berdasarkan data penyewaan per bulan.

## Analisis Data & Visualisasi

### 1. Distribusi Penyewaan Berdasarkan Musim
Boxplot yang menunjukkan bagaimana penyewaan sepeda bervariasi di setiap musim.

### 2. Pola Penyewaan Berdasarkan Hari dalam Minggu
Grafik batang yang menampilkan rata-rata jumlah penyewaan setiap hari dalam seminggu.

### 3. Pengaruh Cuaca terhadap Penyewaan
Grafik batang yang menunjukkan pengaruh kondisi cuaca terhadap penyewaan sepeda.

### 4. Pola Penyewaan Berdasarkan Jam
Grafik garis yang menunjukkan rata-rata penyewaan berdasarkan jam dalam sehari.

### 5. Analisis RFM
Analisis mengenai recency, frequency, dan monetary dari penyewaan sepeda berdasarkan bulan.

## Requirement:

- Python 3.x
- Streamlit
- Pandas
- Matplotlib
- Seaborn

Untuk menginstal dependensi Python yang diperlukan, jalankan:

```
pip install -r requirements.txt
```

## URL

Setelah aplikasi dijalankan, Anda dapat mengakses dashboard Streamlit di:

http://localhost:8501


Atau, URL akan disediakan dalam file [url.txt](url.txt).