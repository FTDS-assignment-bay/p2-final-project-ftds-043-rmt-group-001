import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter
import ast
from wordcloud import WordCloud

def run():
    st.markdown("""
        <h2 style='text-align: center; color: #0047AB;'>
            Exploratory Data Analysis (EDA)
        </h2>
        <p style='text-align: center; font-size:16px; color: gray; margin-top: -10px;'>
            Gain insights into the distribution, features, and sentiment of smartwatch products 
            based on real user reviews and product specifications.
        </p>
        <hr style='border: 1px solid #ccc;'>
    """, unsafe_allow_html=True)




    df = pd.read_csv("https://raw.githubusercontent.com/FTDS-assignment-bay/p2-final-project-ftds-043-rmt-group-001/main/Dataset/data_product.csv")
    ds = pd.read_csv("https://raw.githubusercontent.com/FTDS-assignment-bay/p2-final-project-ftds-043-rmt-group-001/main/Dataset/review_labelled.csv")  # ds = untuk analisis review/token

    # Hitung distribusi brand
    brand_counts = df['brand'].value_counts()

    # -------------------- Streamlit UI --------------------

    st.markdown("### 1️⃣ **Brand Distribution (Pie Chart)**")
    st.info("This chart shows how products are distributed across major smartwatch brands.")

    # Pie chart
    colors = sns.color_palette("pastel")
    fig, ax = plt.subplots(figsize=(7,7))
    ax.pie(
        brand_counts,
        labels=brand_counts.index,
        autopct='%1.1f%%',
        startangle=140,
        colors=colors,
        wedgeprops={'edgecolor': 'black'}
    )
    ax.set_title('Brand Distribution of Smartwatches', fontsize=16, fontweight='bold')
    st.pyplot(fig)
    st.markdown("""
    **Insight:** Brand Distribution of Smartwatches
    
    Dalam analisis distribusi merek smartwatch, terlihat bahwa **Apple Watch** mendominasi pasar dengan porsi hampir **30%** dari total produk. Hal ini menegaskan posisinya sebagai pemimpin pasar dalam kategori smartwatch.Di posisi kedua, **Samsung** mencatat sekitar **24%**, juga menunjukkan popularitas tinggi dan cakupan produk yang luas.
    
    Sementara itu, merek lain seperti **Garmin**, **Fitbit**, dan **Huawei** memiliki distribusi yang seimbang, berkisar antara **9% hingga 11%**. Di sisi lain, brand seperti **Xiaomi** dan **Google** menyumbang porsi yang jauh lebih kecil—masing-masing di bawah **5%**—menandakan bahwa mereka masih memiliki ruang untuk ekspansi lebih lanjut dalam pasar ini.
    """)


    # 2️⃣ Rata-rata Harga per Brand
    st.markdown("### 2️⃣ **Average Price per Brand**")
    st.info("This chart shows the average price of smartwatches for each brand to help compare affordability.")

    # Hitung rata-rata harga
    rerata_harga = df.groupby('brand')['price'].mean().round(2)

    # Bar chart
    fig2, ax2 = plt.subplots(figsize=(12, 6))
    sns.barplot(x=rerata_harga.index, y=rerata_harga.values, palette='Blues_d', ax=ax2)
    ax2.set_title('Average Price of Smartwatches per Brand', fontsize=14, fontweight='bold')
    ax2.set_xlabel('Brand')
    ax2.set_ylabel('Average Price ($)')
    ax2.set_ylim(0, 550)
    plt.xticks(rotation=45)
    plt.tight_layout()
    st.pyplot(fig2)
    st.markdown("""
    **Insight:** 
    
    Jika kita meninjau dari segi harga rata-rata per merek, Garmin menonjol dengan harga tertinggi di antara semua brand, bahkan lebih dari $500. Ini menunjukkan bahwa Garmin memosisikan produknya di segmen premium. Huawei dan Apple Watch juga tergolong mahal, berada di kisaran atas. Sebaliknya, Xiaomi menjadi brand dengan harga paling terjangkau
    """)

    # 3️⃣ Rata-rata Rating per Brand
    st.markdown("### 3️⃣ **Average Rating per Brand**")
    st.info("This chart highlights how users rate each brand based on product reviews.")

    # Hitung rata-rata rating
    rerata_rating = df.groupby('brand')['rating'].mean().round(2)

    # Bar chart
    fig3, ax3 = plt.subplots(figsize=(12, 6))
    sns.barplot(x=rerata_rating.index, y=rerata_rating.values, palette='Greens_d', ax=ax3)
    ax3.set_title('Average User Rating per Brand', fontsize=14, fontweight='bold')
    ax3.set_xlabel('Brand')
    ax3.set_ylabel('Average Rating')
    ax3.set_ylim(0, 5)
    plt.xticks(rotation=45)
    plt.tight_layout()
    st.pyplot(fig3)
    st.markdown("""
    **Insight:** 
    
    Dalam grafik rating pengguna rata-rata, justru Huawei mencatatkan skor tertinggi, diikuti oleh Garmin dan Xiaomi. Artinya, meskipun Xiaomi lebih murah, pengguna tetap memberikan rating tinggi, yang menunjukkan kepuasan terhadap fitur dan kualitasnya. Sebaliknya, Google justru memperoleh rating rata-rata terendah di antara brand lainnya. Meskipun membawa nama besar, produk dari Google tampaknya belum sepenuhnya memenuhi harapan pengguna, sebagaimana tercermin dalam rating yang diberikan
    """)



    # 4. Top 5 Connectivity
    st.markdown("### 4️⃣ **Top 5 Connectivity Types**")
    st.info("Explore the most common connectivity options found across smartwatch products.")

    # Hitung 5 konektivitas terbanyak
    all_connectivity = df['connectivity'].dropna().str.split(', ').sum()
    connectivity_counts = Counter(all_connectivity)
    connectivity_df = pd.DataFrame(connectivity_counts.most_common(5), columns=['Connectivity', 'Count'])

    # Bar chart horizontal
    fig4, ax4 = plt.subplots(figsize=(8, 5))
    sns.barplot(data=connectivity_df, x='Count', y='Connectivity', palette='Purples_d', ax=ax4)
    ax4.set_title('Top 5 Connectivity Types on Smartwatches', fontsize=14, fontweight='bold')
    ax4.set_xlabel('Number of Products')
    ax4.set_ylabel('Connectivity Type')
    plt.tight_layout()
    st.pyplot(fig4)
    st.markdown("""
    **Insight:** 
    
    Dari sisi konektivitas, fitur Bluetooth hampir hadir di semua produk, menjadi standar konektivitas utama. Sedangkan fitur seperti Wireless, Wi-Fi, dan USB tersedia dalam jumlah menengah. Menariknya, GPS—yang sering diandalkan untuk pelacakan aktivitas luar ruangan—hanya tersedia di sedikit produk, menjadikannya fitur yang cukup premium.
    """)

    # 5. Korelasi antara Price - Screen Size - Rating
    st.markdown("### 5️⃣ **Correlation Between Price, Screen Size, and Rating**")
    st.info("Understand how price, screen size, and customer ratings relate to each other.")

    # Heatmap korelasi
    fig5, ax5 = plt.subplots(figsize=(6, 5))
    sns.heatmap(df[['price', 'screen_size', 'rating']].corr(), annot=True, cmap='coolwarm', linewidths=0.5, fmt=".2f", ax=ax5)
    ax5.set_title('Correlation Heatmap', fontsize=14, fontweight='bold')
    st.pyplot(fig5)
    st.markdown("""
    **Insight:** 
    
    Berdasarkan heatmap korelasi di atas, terlihat bahwa hubungan antar variabel price, screen\_size, dan rating tergolong sangat lemah. Korelasi antara harga dan rating hanya 0.11, menunjukkan hampir tidak ada hubungan signifikan — artinya, smartwatch yang lebih mahal belum tentu mendapatkan rating yang lebih tinggi. Menariknya, screen\_size memiliki korelasi negatif terhadap rating sebesar -0.27, yang mungkin mengindikasikan bahwa pengguna justru cenderung memberi rating lebih rendah pada smartwatch dengan ukuran layar lebih besar, entah karena tidak nyaman, terlalu besar di pergelangan tangan. Secara keseluruhan, insight ini menunjukkan bahwa faktor-faktor seperti harga dan ukuran layar belum tentu menjadi penentu utama bagi user satisfaction.

    """)



    # 6️⃣ Top 10 Most Common Features
    st.markdown("### 6️⃣ **Top 10 Smartwatch Features**")
    st.info("These are the most frequently mentioned features across all smartwatch products.")

    # Hitung dan visualisasi fitur
    all_features = df['features'].dropna().str.split(', ').sum()
    feature_counts = Counter(all_features)
    feature_df = pd.DataFrame(feature_counts.most_common(10), columns=['Feature', 'Count'])

    # Horizontal bar chart
    fig6, ax6 = plt.subplots(figsize=(8, 5))
    sns.barplot(data=feature_df, x='Count', y='Feature', palette='Blues_d', ax=ax6)
    ax6.set_title('Top 10 Smartwatch Features', fontsize=14, fontweight='bold')
    ax6.set_xlabel('Number of Products')
    ax6.set_ylabel('Feature')
    plt.tight_layout()
    st.pyplot(fig6)
    st.markdown("""
    **Insight:** 
    Untuk fitur smartwatch secara umum, GPS, activity tracker, dan heart rate monitor menjadi fitur yang paling umum ditemukan. Ini menunjukkan fokus industri pada kesehatan dan kebugaran pengguna. Di sisi lain, fitur seperti voice control dan phone call masih jarang diimplementasikan, kemungkinan karena tidak semua pengguna membutuhkan fitur tersebut.
    """)


    # 7️⃣ Sentiment Distribution
    st.markdown("### 7️⃣ **Overall Sentiment Distribution**")
    st.info("This chart shows how users feel about their smartwatches based on review analysis.")

    # Pie chart sentimen
    sentimen_counts = ds['label'].value_counts()

    # Warna dinamis dan kontras berdasarkan label yang tersedia
    colors_map = {
        "Positive": "#f4d03f",  # kuning
        "Neutral": "#5dade2",   # biru muda
        "Negative": "#ec7063"   # merah
    }
    colors = [colors_map[label] for label in sentimen_counts.index if label in colors_map]

    # Plot
    fig7, ax7 = plt.subplots(figsize=(6, 6))
    ax7.pie(
        sentimen_counts,
        labels=sentimen_counts.index,
        autopct='%1.1f%%',
        startangle=140,
        colors=colors,
        wedgeprops={'edgecolor': 'black'}
    )
    ax7.set_title('Sentiment Breakdown from Reviews', fontsize=14, fontweight='bold')
    st.pyplot(fig7)
    st.markdown("""
    **Insight:** 
    Terakhir, dari analisis sentimen review pengguna, dapat disimpulkan bahwa pengalaman pengguna terhadap produk sangat positif. Lebih dari 86% review bersifat positif, sedangkan review negatif hanya sekitar 10%, dan netral sekitar 3.5%. Ini mencerminkan kepuasan umum terhadap smartwatch yang ada dalam dataset, baik dari segi performa, fitur, maupun kualitas.
    """)


    # === Wordcloud Function ===
    def generate_wordcloud(data, column_name, title):
        data[column_name] = data[column_name].apply(lambda x: ast.literal_eval(x) if isinstance(x, str) else x)
        all_tokens = sum(data[column_name], [])
        text = ' '.join(all_tokens)
        wordcloud = WordCloud(
            width=800,
            height=500,
            background_color='white',
            colormap='Set2',
            max_words=150
        ).generate(text)

        fig, ax = plt.subplots(figsize=(10, 5))
        ax.imshow(wordcloud, interpolation='bilinear')
        ax.axis('off')
        ax.set_title(title, fontsize=14, fontweight='bold')
        st.pyplot(fig)

    # ===== 8. Wordcloud All Sentiment =====
    st.markdown("### 8️⃣ **Word Cloud by Sentiment**")
    st.info("These visualizations show the most frequent words mentioned in positive and negative reviews.")

    col1, col2 = st.columns(2)
    with col1:
        generate_wordcloud(ds[ds['label'] == 'Positive'], 'token', '🟢 Positive Reviews Word Cloud')

    with col2:
        generate_wordcloud(ds[ds['label'] == 'Negative'], 'token', '🔴 Negative Reviews Word Cloud')


    # ===== 9. Per Brand Breakdown =====
    st.markdown("### 9️⃣ **Sentiment & Word Cloud by Brand**")
    st.info("See brand-specific sentiment distribution and most common words in reviews.")

    selected_brands = ['Amazfit', 'Apple', 'Fitbit', 'Garmin', 'Google', 'Huawei', 'Samsung', 'Xiaomi']
    for brand in selected_brands:
        st.markdown(f"#### 🔹 {brand}")

        brand_data = ds[ds['products'].str.contains(brand, case=False, na=False)]

        if not brand_data.empty:
            # Sentiment pie chart
            sent_count = brand_data['label'].value_counts()

            # Warna kontras untuk setiap label
            colors_map = {  
                "Positive": "#f4d03f",  # kuning terang
                "Neutral": "#5dade2",   # biru muda
                "Negative": "#ec7063"   # merah
            }
            # Ambil warna sesuai urutan label yang muncul
            colors = [colors_map[label] for label in sent_count.index if label in colors_map]

            fig, ax = plt.subplots(figsize=(5, 5))
            ax.pie(
                sent_count,
                labels=sent_count.index,
                autopct='%1.1f%%',
                startangle=140,
                colors=colors
            )
            ax.set_title(f'Sentiment Distribution for {brand}', fontsize=12)
            st.pyplot(fig)

            # Wordcloud side by side
            col1, col2 = st.columns(2)
            with col1:
                generate_wordcloud(brand_data[brand_data['label'] == 'Positive'], 'token', f'Positive Word Cloud - {brand}')
            with col2:
                generate_wordcloud(brand_data[brand_data['label'] == 'Negative'], 'token', f'Negative Word Cloud - {brand}')

            st.markdown("---")
        else:
            st.warning(f"⚠️ No review data found for **{brand}**.")

