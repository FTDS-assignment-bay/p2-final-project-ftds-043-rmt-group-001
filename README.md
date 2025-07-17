<h3 style="text-align: center;">
        <img src="https://readme-typing-svg.herokuapp.com/?font=Winky+Rough&weight=700&color=0047AB&size=50&center=true&vCenter=true&width=1000&height=70&duration=3000&lines=Hai!+Welcome+to+SWARM!;">
    </h3>

---

# SWARM - Smart Watch Application Recomendation Model

<p align="center">
  <img src="./logo.png" width=400 align="center">
</p>


**SWARM**  adalah aplikasi yang dapat memberikan rekomendasi kepada pengguna untuk menentukan jenis Smart Watch / jam tangan yang paling cocok berdasarkan spesifikasi dan kebutuhan pelanggan. SWARM memerikan rekomendasi berdasarkan masukan teks yang diberikan pengguna dan membandingkan dengan reviews dari pembeli sebelumnya untuk menentukan produk yang paling sesuai dengan keinginan pelanggan.

---

## 📖 Problem Background 

Perkembangan teknologi telah melahirkan berbagai perangkat pintar yang dapat menunjang aktivitas harian, salah satunya adalah smartwatch. Perangkat ini tidak hanya berfungsi sebagai penunjuk waktu, tetapi juga dilengkapi fitur-fitur seperti penghitung langkah, pemantauan detak jantung, pelacakan tidur, dan pemantauan aktivitas olahraga. Sebuah studi yang diterbitkan dalam Journal of Medical Internet Research menyebutkan bahwa penggunaan smartwatch dapat meningkatkan kesadaran kesehatan pengguna dengan fitur-fitur yang ada.

Menurut Wikipedia(2025), terdapat lebih dari 50 brand elektronik/startup yang memproduksi berbagai jenis dan merk smart watch. Banyaknya merek dan jenis smartwatch di pasaran terutama di e-commerce membuat konsumen bingung untuk menentukan smartwatch yang sesuai. Terdapat banyak aspek seperti fitur, kualitas, rating pengguna, dan harga yang harus dipertimbangkan oleh pembeli sebelum menentukan smartwatch yang sesuai.
Oleh karena itu, dibutuhkan sebuah aplikasi yang dapat memberikan rekomendasi smartwatch berdasarkan kebutuhan dan preferensi pengguna, dengan mempertimbangkan spesifikasi dan harga yang ditawarkan.

## 🎯 Objective

Berdasarkan permasalahan yang terjadi, project ini memiliki beberapa tujuan antara lain:
- Membuat aplikasi yang dapat membantu pengguna untuk menentukan  jenis smartwatch yang sesuai dengan spesifikasi dan kebutuhan.
- Memberikan rekomendasi (top 3) device yang paling sesuai, beserta reviews produk berdasarkan pembelian sebelumnya.
- Memberikan rekomendasi kepada brand mengenai improvement produk yang dapat dilakukan berdasarkan hasil analisis sentimen pelanggan.
- Mengurangi biaya marketing dengan menekan cost per acquisition dan conversion lag

## 📦 Data

Dataset yang digunakan dalam project ini diperoleh dari hasil scraping pada sebuah website ecommerce dengan menggunakan kata kunci *"smart watch"*. Proses scraping menghasilkan dua buah dataset yaitu dataset produk dan dataset reviews.

Dataset produk terdiri dari 10 kolom dan 281 baris data.

| Index | Nama Kolom | Tipe Data |
| --- | --- | --- |
| 1 | Nama produk | String |
| 2 | Rating | Float | 
| 3 | Price | String |
| 4 | Features | String |
| 5 | Battery | Int |
| 6 | Connectivity | String |
| 7 | GPS | Boolean |
| 8 | Screen Size | Float |
| 9 | img_url | String |
| 10 | Brand | String |

Data set reviews terdiri dari 3 kolom dan 1104 baris data

| Index | Nama Kolom | Tipe Data |
| --- | --- | --- |
| 1 | Nama Produk | String |
| 2 | Reviews | String | 
| 3 | Rating | Float |

## ⚙️ Methods

Pada project ini terdapat beberapa proses pengolahan dan analisis data untuk mengembangkan sebuah model rekomendasi dan report analisis data berdasarkan objective yang ditentukan. Tahapan proses tersebut antara lain:

```
1. ETL : Proses Akuisisi Data
    ├── Scraping Data
    ├── Data Cleaning
    ├── Data Saving
    └── Data Testing (Great Expectation)

2. Data Analysis : Proses Analisis Data untuk membuat visualisasi dan mendapatkan insight
    ├── Data Exploration
    ├── Data Visualization
    └── Report

3. Modelling : Proses membuat model aplikasi rekomendasi smarwatch
    ├── Text Pre-processing
    ├── Data Transformation
    ├── Model Definition (Word2Vec)
    ├── Model Training (Cosine Similarity)
    ├── Model Deployment (Streamlit)
    └── Model Evaluation (USEQuesionnaire)
```

## 🛠️ Stack

Dalam pembuatan project ini terdapat beberapa tools atau library yang digunakan, yaitu:

| No | Programming Language |
| --- | --- |
| 1 | Python |
| 2 | SQL | 

| No | Library | Fungsi |
| --- | --- | --- |
| 1 | Pandas | Mengolah data |
| 2 | Numpy | Perhitungan matematis |
| 3 | Seaborn | Visualisasi Data |
| 4 | Wordcloud | Visualisasi Kata |
| 5 | NLTK | Text Pre-processing |
| 6 | SK-Learn | Modelling |
| 7 | Gensim | Vectorization |
| 8 | Streamlit | Deployment |
| 9 | ScraperAPI | Data Scraping |
| 10 | BS4 | Data Scraping |

| No | Tools | Fungsi |
| --- | --- | --- |
| 1 | VSCode | Text Editor |
| 2 | Huggin Face | Model Deployment |
| 3 | Tableau | Visualisasi Data |

## 🚀 Result
Berdasarkan objective yang sudah ditentukan, project ini menghasilkan beberapa dokumen atau halaman yang dapat digunakan oleh pengguna. Hasil yang didapatkan dari project ini antara lain

1. Aplikasi Rekomendasi Smart Watch (SWARM)
Aplikasi ini diluncurkan pada website Hugging Face dan dapat diakses melalui link berikut: \
https://huggingface.co/spaces/anismarsela32/swarm-app

Contoh tampilan aplikasi

![Streamlit](./images/streamlit.PNG)

2. Visualisasi Data
Hasil visualisasi data dari dataset yang didapatkan dapat diakses pada link berikut : \
https://public.tableau.com/app/profile/mustika.tri.utami/viz/FinalProject_17526552446080/Dashboard1?publish=yes

3. Notebook Hasil Analisis
Hasil analisis data dan rekomendasi yang diberikan dapat diakes pada link berikut: \
https://github.com/FTDS-assignment-bay/p2-final-project-ftds-043-rmt-group-001/blob/main/eda.ipynb


## 🧠 Project Member
| Nama | Role | Contact |
| --- | --- | --- |
| Ilham Wahdini | Data Engineer | [email](mailto:ilhamwahdini8@gmail.com) |
| Mustika Tri U. | Data Analyst | email |
| Pujo Prasetyo Aji | Data Scientist 1 | [email](mailto:anismarsela36854@gmail.com) |
| Anis Marsela | Data Scientist 2 | [email](mailto:pujo.prasetyoaji@gmail.com) |

---

