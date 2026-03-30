# 📚 Book API (FastAPI)

Bu proje, **Python ve FastAPI kullanılarak geliştirilmiş basit bir REST API uygulamasıdır.**
API sayesinde kitapları ekleyebilir, listeleyebilir, güncelleyebilir, silebilir ve arayabilirsiniz.

Projenin amacı **REST API mantığını öğrenmek ve modern Python backend geliştirme araçlarını kullanmayı göstermektir.**

---

# 🚀 Kullanılan Teknolojiler

* Python
* FastAPI
* Pydantic
* Uvicorn

FastAPI frameworkü: FastAPI

---

# 📂 Proje Yapısı

book-api/

main.py → API endpointlerinin bulunduğu ana dosya
requirements.txt → Gerekli Python paketleri
README.md → Proje açıklaması

---

# ⚙️ Kurulum

Projeyi çalıştırmak için:

pip install -r requirements.txt

---

# ▶️ API'yi Çalıştırma

python -m uvicorn main:app --reload

Sunucu çalıştıktan sonra aşağıdaki adresler kullanılabilir:

Ana adres:

http://127.0.0.1:8000

API dokümantasyonu:

http://127.0.0.1:8000/docs

---

# 📚 API Endpointleri

### 1️⃣ Kitapları Listeleme

GET /books

Tüm kitapları döndürür.

---

### 2️⃣ Kitap Ekleme

POST /books

Örnek JSON:

{
"title": "Frankenstein",
"author": "Mary Shelley",
"year": 1818
}

---

### 3️⃣ Kitap Güncelleme

PUT /books/{book_id}

Belirli bir kitabı günceller.

---

### 4️⃣ Kitap Silme

DELETE /books/{book_id}

Belirli bir kitabı siler.

---

### 5️⃣ Kitap Arama

GET /books/search/{title}

Kitap başlığına göre arama yapar.

---

# 🎯 Projenin Amacı

Bu proje aşağıdaki backend kavramlarını göstermek için geliştirilmiştir:

* REST API tasarımı
* HTTP metodları (GET, POST, PUT, DELETE)
* JSON veri kullanımı
* FastAPI frameworkü
* API endpoint tasarımı

---