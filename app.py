import streamlit as st
import json

# Load data dari file JSON
def load_books():
    try:
        with open('data/books.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

# App title
st.title("📚 Book Search App")
st.subheader("Data hasil crawling dari Books to Scrape")

books = load_books()

# Search bar
search_term = st.text_input("Cari Judul Buku")

# Filter data
if search_term:
    filtered_books = [book for book in books if search_term.lower() in book['title'].lower()]
else:
    filtered_books = books

# Tampilkan hasil
for book in filtered_books:
    st.markdown(f"### [{book['title']}]({book['link']})")
    st.write(f"💰 **Harga:** {book['price']}")
    st.write(f"📦 **Stok:** {book['availability']}")
    st.write(f"⭐ **Rating:** {book['rating']}")
    st.markdown("---")
