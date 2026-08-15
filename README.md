# Sensör Verileri ile Akıllı Yük Yönetimi ve Arıza Tespiti / Smart Load Management & Overload Detection

🌍 **[English version is available below](#-english-version)**

## 🇹🇷 Türkçe 

Bu proje, **Türkiye Yapay Zeka Akademisi** Makine Öğrenmesi Eğitimi final projesi olarak geliştirilmiştir. Proje, mikrodenetleyicilerden ve güç sensörlerinden (ör. INA219) alınan verileri kullanarak sistemin "Aşırı Yük" (Overload) durumunu tespit eden uçtan uca bir sınıflandırma modelidir.

### 📌 Projenin Amacı
Donanım dünyasının fiziksel gerçeklikleri ile makine öğrenmesinin tahmin gücünü birleştirerek, endüstriyel sistemlerde tehlike anını (aşırı yük) önceden tespit etmek ve akıllı yük yönetimi sağlamaktır.

### 🛠️ Uygulanan Adımlar
1. **Sentetik Sensör Verisi Üretimi (`veri_uret.py`):** Fiziksel kurallara (Güç = Akım x Gerilim) dayalı olarak akım, gerilim ve sıcaklık verileri üretildi. Gerçek dünyayı yansıtması için veriye bilinçli olarak sensör kopuklukları (NaN) ve imkansız değerler (Outliers) eklendi.
2. **Veri Temizleme:** Eksik veriler `median` ile dolduruldu, mantık dışı sensör hataları filtrelendi.
3. **Öznitelik Mühendisliği:** Sistemin zorlanma seviyesini ölçmek için `Termal Stres İndeksi` (Sıcaklık / Güç) üretildi.
4. **Dengesiz Veri Yönetimi:** Arızaların nadir (%15) olmasından kaynaklı sınıf dengesizliği (Imbalanced Data), `stratify` parametresi ve `class_weight="balanced"` teknikleri ile çözüldü.
5. **Model Eğitimi & Optimizasyon (`model_egit.py`):** `Logistic Regression`, `Random Forest` ve `Gradient Boosting` modelleri eğitildi. Accuracy yerine `ROC-AUC` ve `Recall` metrikleri baz alındı.
6. **Sonuç:** Model test setindeki gerçek tehlikelerin (Aşırı Yük) tamamını **%100 (Recall: 1.00)** başarıyla tespit etti ve hiçbir tehlikeyi gözden kaçırmadı.

### 🚀 Nasıl Çalıştırılır?
1. Sanal ortamı oluşturun ve aktif edin: `python -m venv venv`
2. Kütüphaneleri yükleyin: `pip install -r requirements.txt`
3. Önce veriyi üretin: `python veri_uret.py`
4. Modeli eğitin: `python model_egit.py`

---

## 🇬🇧 English Version

This project was developed as the final project for the Machine Learning Course provided by the **Turkish Artificial Intelligence Academy**. It is an end-to-end classification pipeline that detects "Overload" conditions in a system using simulated data from microcontrollers and power sensors (e.g., INA219).

### 📌 Project Objective
To combine the physical realities of hardware with the predictive power of machine learning to proactively detect danger (overloads) in industrial systems and enable smart load management.

### 🛠️ Applied Steps
1. **Synthetic Sensor Data Generation (`veri_uret.py`):** Generated voltage, current, and temperature data based on physical laws (Power = Current x Voltage). To simulate the real world, sensor disconnections (NaN) and impossible values (Outliers) were intentionally injected.
2. **Data Cleaning:** Imputed missing values using the `median` and filtered out illogical sensor errors.
3. **Feature Engineering:** Created a `Thermal Stress Index` (Temperature / Power) to measure the system's strain level.
4. **Imbalanced Data Management:** Addressed the class imbalance caused by the rarity of faults (15%) using the `stratify` split and `class_weight="balanced"` techniques.
5. **Model Training & Optimization (`model_egit.py`):** Trained `Logistic Regression`, `Random Forest`, and `Gradient Boosting` classifiers. Evaluated models based on `ROC-AUC` and `Recall` metrics instead of Accuracy.
6. **Conclusion:** The selected model successfully detected **100% (Recall: 1.00)** of the actual dangers (Overloads) in the test set without missing a single one.

### 🚀 How to Run
1. Create and activate a virtual environment: `python -m venv venv`
2. Install dependencies: `pip install -r requirements.txt`
3. Generate the data first: `python veri_uret.py`
4. Train the model: `python model_egit.py`