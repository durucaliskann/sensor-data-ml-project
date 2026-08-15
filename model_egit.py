"""
Adim 2 Veri temizleme ve model egitimi
Sensorlerden geldigini varsaydigimiz hatali verileri temizleyip
ozellikleri uretip en iyi sekilde makine ogrenmesi yapacagim 

"""
import pandas as pd
import numpy as np

# Egitimde kullandigim kutuphaneleri kullanacagim
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score

# Veriyi yukleyelim

df = pd.read_csv("sensor_verisi_kirli.csv")

print(f"Baslangictaki satir sayisi: {len(df)}")

# VERI TEMIZLEYELIM

# once eksik veriler var mi kontrol edelim
print("temizlemeden onceki bos veri sayilari: ")
print(df.isnull().sum())

# Akim ve sicakliktaki bosluklari o sutunun medyani ile dolduralim
df["akim_A"] = df["akim_A"].fillna(df["akim_A"].median())
df["sicaklik_C"] = df["sicaklik_C"].fillna(df["sicaklik_C"].median())

# Aykiri degerleri anlamsiz olanlari silecek sekilde temizleyelim
temiz_filtre = (df["voltaj_V"] > 0) & (df["sicaklik_C"] < 100)
df = df[temiz_filtre].reset_index(drop=True)
print(f"-> İmkansız hatalı veriler silindikten sonra temiz satır sayısı: {len(df)}")

# feature uretimi yapalim
df["termal_stres"] = df["sicaklik_C"] / (df["guc_W"] + 1)

y = df["asiri_yuk"]
X = df.drop(columns = ["asiri_yuk"])

# Veriyi %80 Eğitim ve %20 Test olarak bölüyorum. (Sınıf dengesini korumak için stratify kullandım)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# Değerlerin büyüklükleri birbirini ezmesin diye standartlaştırma (ölçekleme) yapıyorum
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train) 
X_test_scaled = scaler.transform(X_test)

modeller = {
    "Logistic Regression": LogisticRegression(class_weight="balanced", random_state=42),
    "Random Forest": RandomForestClassifier(class_weight="balanced", random_state=42),
    "Gradient Boosting": GradientBoostingClassifier(random_state=42)
}

en_iyi_skor = 0
secilen_model_adi = ""
secilen_model = None

for isim, model in modeller.items():
    model.fit(X_train_scaled, y_train)
    
    # Doğruluk (Accuracy) yerine tehlikeyi daha iyi ölçen ROC-AUC skoruna bakıyorum.
    y_tahmin_olasilik = model.predict_proba(X_test_scaled)[:, 1]
    auc_skoru = roc_auc_score(y_test, y_tahmin_olasilik)
    
    print(f"{isim} ROC-AUC Skoru: {auc_skoru:.4f}")
    
    if auc_skoru > en_iyi_skor:
        en_iyi_skor = auc_skoru
        secilen_model_adi = isim
        secilen_model = model

print(f"\nEn yüksek skoru veren model '{secilen_model_adi}' oldu. Buna karar verdim.")

y_tahmin = secilen_model.predict(X_test_scaled)

print("Karmaşıklık Matrisi (Confusion Matrix):")
cm = confusion_matrix(y_test, y_tahmin)
print(f"Normal durumu doğru bilme (True Negative): {cm[0,0]}")
print(f"Boş yere alarm verme (False Positive):      {cm[0,1]}")
print(f"Tehlikeyi gözden kaçırma (False Negative): {cm[1,0]}")
print(f"Tehlikeyi doğru bilme (True Positive):     {cm[1,1]}")

print("\nDetaylı Sınıflandırma Raporu:")
print(classification_report(y_test, y_tahmin))


# Seçtiğim model kararlarını neye göre almış ona bakıyorum
if hasattr(secilen_model, "feature_importances_"):
    onem_dereceleri = pd.Series(secilen_model.feature_importances_, index=X.columns)
    onem_dereceleri = onem_dereceleri.sort_values(ascending=False)
    print("Model 'Aşırı Yük' kararını verirken en çok hangi özelliklere baktı?")
    print(onem_dereceleri)