# 🤖 Engelden Kaçan Robot

Ultrasonik sensörlerle çevresini algılayan, önündeki engelleri tespit edip otomatik olarak yön değiştiren **Arduino tabanlı otonom robot**. Proje, robotun çalışma prensiplerini ve devre şemasını anlatan bir **Streamlit tanıtım uygulamasıyla** birlikte sunulmaktadır.

> 🎓 Hitit Üniversitesi Bilgisayar Mühendisliği — Mikrodenetleyici Dersi Projesi

---

## 🎯 Proje Hakkında

Robot, önündeki engelleri **HC-SR04 ultrasonik mesafe sensörü** ile algılar. Belirlenen mesafenin altında bir engel tespit edildiğinde durur, etrafı tarayarak en uygun yönü belirler ve hareketine bu yönde devam eder. Tüm karar mekanizması Arduino üzerinde gerçek zamanlı olarak çalışır.

---

## 🔧 Donanım Bileşenleri

- **Arduino Uno** — ana mikrodenetleyici
- **HC-SR04 Ultrasonik Mesafe Sensörü** — engel algılama
- **L298N Motor Sürücü** — DC motor kontrolü
- **DC Motorlar (x2)** — tahrik sistemi
- **Servo Motor (SG90)** — sensörün yön taraması için
- **Li-ion Pil / Batarya** — güç kaynağı
- **Robot Şasi** — mekanik yapı

---

## 💻 Yazılım

| Bileşen | Açıklama |
|---------|----------|
| **Arduino C++** | Sensör okuma, motor kontrolü ve engel kaçınma algoritması |
| **Streamlit** | Projenin akademik sunum arayüzü (çalışma prensibi, devre şeması, kod açıklamaları) |
| **Python** | Tanıtım uygulamasının altyapısı |

---

## 🚀 Tanıtım Uygulamasını Çalıştırma

```bash
# Repoyu klonla
git clone https://github.com/RidvanKS/engelden-kacan-robot.git
cd engelden-kacan-robot

# Sanal ortam oluştur (önerilir)
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

# Bağımlılıkları yükle
pip install -r requirements.txt

# Streamlit uygulamasını başlat
streamlit run app.py
```

Tarayıcı otomatik olarak açılmazsa: **http://localhost:8501**

---
## Proje Linki: https://ridvan-kocak-mikrodenetleyici-244210071.streamlit.app/

## 📁 Proje Yapısı

```
.
├── app.py              # Streamlit tanıtım uygulaması
├── assets/             # Görsel kaynaklar (devre şeması, fotoğraflar)
├── requirements.txt    # Python bağımlılıkları
└── .gitignore
```

---

## ⚙️ Çalışma Mantığı

```
[Başlangıç]
     ↓
[İleri hareket]
     ↓
[Mesafe ölçümü] ──→ Engel yok ──→ [Dön]
     ↓
   Engel var
     ↓
[Dur]
     ↓
[Servo ile sağ-sol tara]
     ↓
[En uzak yönü seç]
     ↓
[Yön değiştir ve devam et]
```

---

## 👤 Geliştirici

**Rıdvan Koçak**
Hitit Üniversitesi — Bilgisayar Mühendisliği

- 📧 kocak.ridvan@hotmail.com
- 🐙 [github.com/RidvanKS](https://github.com/RidvanKS)
