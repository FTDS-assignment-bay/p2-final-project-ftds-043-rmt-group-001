# Import library yang dibutuhkan
import streamlit as st
import pandas as pd
import numpy as np
import json, re, string, os
import nltk
from nltk.tokenize import word_tokenize
from gensim.models import Word2Vec
from nltk.util import ngrams
from sklearn.metrics.pairwise import cosine_similarity


# Setup direktori untuk menyimpan resource NLTK (dibutuhkan untuk tokenisasi dan preprocessing)
nltk_path = "/tmp/nltk_data"
os.makedirs(nltk_path, exist_ok=True)
nltk.data.path.append(nltk_path)

# Download resource NLTK yang dibutuhkan
nltk.download('punkt', download_dir=nltk_path)
nltk.download('punkt_tab', download_dir=nltk_path)
nltk.download('stopwords', download_dir=nltk_path)
nltk.download('wordnet', download_dir=nltk_path)
nltk.download('averaged_perceptron_tagger', download_dir=nltk_path)


# ======== FUNGSI PREPROCESS ========

# Lowercase + tokenisasi kata
def simple_preprocess(text):
    return word_tokenize(text.lower())

# Ubah token menjadi trigrams (untuk menangkap konteks 3 kata berurutan)
def to_trigrams(tokens):
    return ['_'.join(gram) for gram in ngrams(tokens, 3)]

# Gabungkan token dan trigram
def preprocessing_with_trigram(text_series):
    result = []
    for text in text_series:
        tokens = simple_preprocess(text)
        trigrams = to_trigrams(tokens)
        combined = tokens + trigrams
        result.append(combined)
    return result

# Ubah token menjadi vektor kalimat (rata-rata semua word vector)
def get_sentence_vector(tokens, model):
    vectors = [model.wv[token] for token in tokens if token in model.wv]
    return np.mean(vectors, axis=0) if vectors else np.zeros(model.vector_size)


# ======== LOAD DATA & MODEL ========

# Load data review + produk (data.csv = hasil preprocessing)
df = pd.read_csv("data.csv")

# Data produk mentah (informasi produk saja)
df_product = pd.read_csv("https://raw.githubusercontent.com/FTDS-assignment-bay/p2-final-project-ftds-043-rmt-group-001/main/Dataset/data_product.csv")

# Data review mentah yang sudah diberi label sentimen
df_review = pd.read_csv("https://raw.githubusercontent.com/FTDS-assignment-bay/p2-final-project-ftds-043-rmt-group-001/main/Dataset/review_labelled.csv")


# Load model Word2Vec
w2v_model = Word2Vec.load("w2v_model.model")

# Convert kolom 'spect' dari string ke list (kalau datanya serialized list)
if isinstance(df['spect'].iloc[0], str):
    df['spect'] = df['spect'].apply(eval)

# Simpan vektor spesifikasi produk (supaya nggak dihitung ulang tiap pencarian)
df['spect_vector'] = df['spect'].apply(lambda x: get_sentence_vector(x, w2v_model))


def run():
        # Judul aplikasi
        st.markdown("""
            <h1 style='text-align: center; color: #0047AB; margin-top: 5px;'>SWARM</h1>
            <h4 style='text-align: center; color: gray; margin-top: -10px;'>
                <i>Smart Watch Application Recommendation Model</i>
            </h4>
            <p style='text-align: center; font-size:16px;'>
                Discover the perfect smartwatch tailored to your needs, powered by real user reviews and intelligent filtering.
            </p>
            <hr style='border: 1px solid #ccc;'>
        """, unsafe_allow_html=True)


        # Filter: Pilih brand
        brand_options = ["All Brands"] + sorted(df['brand'].dropna().unique().tolist())
        brand = st.selectbox("Choose a brand", options=brand_options)

        # Filter: Batas harga (opsional)
        use_price_limit = st.checkbox("Set price limit?")
        if use_price_limit:
            budget = st.slider("Maximum price ($)", int(df['price'].min()), int(df['price'].max()), 200)
        else:
            budget = None

        # Keyword input
        keyword = st.text_input("Enter keyword (e.g., health, GPS, sleep tracking):")

        # Tombol pencarian
        if st.button("🔍 Search"):
            # ===== Vectorisasi User Query =====

            # Gabungkan input jadi satu kalimat pencarian
            user_query = f"{brand if brand != 'All Brands' else ''} {budget if budget else ''} {keyword}"

            # Tokenisasi input user + ubah jadi vektor
            user_tokens = simple_preprocess(user_query)
            user_vector = get_sentence_vector(user_tokens, w2v_model)

            # Vectorisasi review + Hitung kemiripan review terhadap user query
            df['review_tokens'] = df['clean_text'].apply(simple_preprocess)
            df['review_vector'] = df['review_tokens'].apply(lambda x: get_sentence_vector(x, w2v_model))
            df['review_similarity'] = df['review_vector'].apply(lambda x: cosine_similarity([user_vector], [x])[0][0])

            # ===== Filtering =====

            # Mulai dari seluruh data
            filtered = df.copy()

            # Filter by brand (jika dipilih)
            if brand != "All Brands":
                filtered = filtered[filtered['brand'].fillna('').str.lower() == brand.lower()]
            
            # Filter by budget
            if budget is not None:
                filtered = filtered[filtered['price'].fillna(0) <= budget]

             # ====== Ambil Top 3 Produk Terbaik ======

            # Urutkan berdasarkan similarity dan rating
            result = filtered.sort_values(by=["review_similarity", "rating"], ascending=False)
            result = result.drop_duplicates(subset='products', keep='first').head(3)

            if result.empty:
                st.warning("⚠️ No matching products found.")
                st.stop()

            top3_products = result['products'].tolist()

            # ===== Distribusi Sentiment =====
            
            # Ambil review dari data asli untuk total sentimen
            filtered_sentiment = df_review[df_review['products'].isin(top3_products)].copy()

            # Hitung sentimen positif dan negatif berdarkan top 3 produk
            pos_count = filtered_sentiment[filtered_sentiment['label'] == 'Positive'].shape[0]
            neg_count = filtered_sentiment[filtered_sentiment['label'] == 'Negative'].shape[0]

            # Tampilkan ke UI
            st.subheader("Total Sentiment Distribution")
            col1, col2 = st.columns(2)
            col1.metric("🟢 Positive", pos_count)
            col2.metric("🔴 Negative", neg_count)


            # ===== Tampilkan Rekomendasi =====
            st.subheader("🏆 Top 3 Recommended Smartwatches")
            for idx, (_, row) in enumerate(result.iterrows(), start=1):
                st.markdown(f"## {idx}. {row['products']}")

                col1, col2 = st.columns([1, 2])
                with col1:
                    # Tampilkan gambar produk
                    if isinstance(row['img_url'], str) and row['img_url'].startswith("http"):
                        st.image(row['img_url'], width=160)
                    else:
                        st.warning("⚠️ No image available for this product.")

                with col2:
                    # Info detail produk
                    price = f"${row['price']:.2f}" if pd.notnull(row['price']) else "Unknown"
                    battery = f"{row['battery']} mAh" if pd.notnull(row['battery']) else "Not specified"
                    features = row['features'] if pd.notnull(row['features']) else "Not available"
                    connectivity = row['connectivity'] if pd.notnull(row['connectivity']) else "Unknown"
                    gps = row['gps'] if pd.notnull(row['gps']) else "Unknown"
                    rating = row['rating'] if pd.notnull(row['rating']) else "N/A"

                    st.markdown(f"**💰 Price**: {price}")
                    st.markdown(f"🔋 **Battery**: {battery}")
                    st.markdown(f"⚙️ **Features**: {features}")
                    st.markdown(f"📡 **Connectivity**: {connectivity} | GPS: {gps}")
                    st.markdown(f"⭐ **Rating**: {rating} | 🧠 **Relevance**: {row['review_similarity']:.2f}")

                # Tampilkan 3 review positif terbaik dari data asli
                top_reviews = df_review[
                    (df_review['products'] == row['products']) &
                    (df_review['label'] == 'Positive')
                ] \
                .sort_values(by='individual_rating', ascending=False) \
                .drop_duplicates(subset='individual_review') \
                .head(3)


                st.markdown("#### 💬 Top 3 Reviews")
                for _, r in top_reviews.iterrows():
                    emoji = "🟢" if r['label'] == 'Positive' else "🔴"
                    st.markdown(
                        f"""
                        <div style='
                            padding:8px;
                            background-color:#f9f9f9;
                            border-left: 4px solid {"green" if r['label']=="Positive" else "red"};
                            margin-bottom:10px;
                            color: black;
                        '>
                            {emoji} {r['individual_review']}
                        </div>
                        """,
                        unsafe_allow_html=True
                    )

                st.markdown("---")
