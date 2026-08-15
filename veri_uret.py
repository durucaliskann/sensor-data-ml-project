"""
Adim 1 
sensor verisi uretelim, STM32 ve guc sensorlerinden geliyormus gibi 
akim, gerilim ve sicaklik verileri uretecegim ve CSV olarak kaydedecegim
AMA gercek hayatta sensorler temiz veri vermediginden bilerek NaN ve hatali 
(aykiri) veriler serpistirecegim

"""

import pandas as pd
import numpy as np

print("Sensor verisi uretiliyor")
np.random.seed(42)
ornek_sayisi = 250

# Sensor okumalarini simule ediyorum

voltaj = np.random.normal(220, 5, ornek_sayisi)
akim = np.random.normal(5, 2, ornek_sayisi)
guc_tuketimi = voltaj * akim
sicaklik = 25 + (akim * 2.5) + np.random.normal(0, 2, ornek_sayisi)
asiri_yuk = np.where((akim > 8.5 ) | (sicaklik > 45), 1, 0)

df = pd.DataFrame({
    "voltaj_V" : voltaj,
    "akim_A" : akim, 
    "guc_W" : guc_tuketimi,
    "sicaklik_C" : sicaklik, 
    "asiri_yuk" : asiri_yuk
})

# Eksik veri eklemek icin 
df.loc[15:25, "akim_A"] = np.nan # 10 tane akim verisi eksiltildi
df.loc[100:110, "sicaklik_C"] = np.nan # 10 tane sicaklik verisi eksiltildi

df.loc[500, 'voltaj_V'] = -200.0       # Voltaj eksi olamaz (hata)
df.loc[999, 'sicaklik_C'] = 9999.0     # 10 bin derece sıcaklık imkansız (hata)

df.to_csv("sensor_verisi_kirli.csv", index = False)

